from gai.lib.common.generators_utils import chat_string_to_list
from gai.lib.common.logging import getLogger
logger = getLogger(__name__)
from gai.lib.config import GaiClientConfig


from openai.types.chat_model import ChatModel
from openai import OpenAI
from typing import get_args,Union, Optional,Callable
from gai.openai.attach_extractor import attach_extractor

# This class is used by the monkey patch to override the openai's chat.completions.create() function.
# This is also the class responsible for for GAI's text-to-text completion.
# The main driver is the create() function that can be used to generate or stream completions as JSON output.
# The output from create() should be indisguishable from the output of openai's chat.completions.create() function.
#
# Example:
# from openai import OpenAI
# client = OpenAI()
# from gai.ttt.client.completions import Completions
# client = Completions.PatchOpenAI(client)
# client.chat.completions.create(model="exllamav2-mistral7b",messages=[{"role":"user","content":"Tell me a one sentence story"}])

# override_get_client_from_model is meant to be used for unit testing
def patch_chatcompletions(openai_client:OpenAI, file_path:str=None):

    # Save the original openai functions
    openai_create = openai_client.chat.completions.create
    openai_parse = openai_client.beta.chat.completions.parse
    
    # Replace openai.completions.create with a wrapper over the original create function
    def patched_create(**kwargs):
        # The model is required to determine the client type patched to the openai_client so it should be determined first.
        model = kwargs.get("model", None)
        if not model:
            raise Exception("completions.patched_create: Model not provided")

        # Based on the model name, determine the client used to generate completions, eg. "gai" uses ttt_client.
        client_config = GaiClientConfig.from_name(model)
        if file_path:
            client_config = GaiClientConfig.from_name(model,file_path)
        
        if client_config and client_config.client_type == "gai":

            from gai.ttt.client.ttt_client import TTTClient
            ttt = TTTClient(client_config)
            
            # Remove the model from the kwargs as it is not required by the TTTClient
            kwargs.pop("model")
            
            stream = kwargs.get("stream",False)
            kwargs["stream"] = stream
            
            response = ttt(**kwargs)
            return response
        
        # If the model is an openai model, route to openai's chat.completions.create() function.            
        if client_config and client_config.client_type == "openai" and client_config.model in get_args(ChatModel):
            stream=kwargs.get("stream",False)
            response = openai_create(**kwargs)
            response = attach_extractor(response,stream)
            return response
        
        # If the model is an ollama model, route to ollama chat() function.
        if client_config and client_config.client_type == "ollama":
            from ollama import chat
            
            # Extract the required parameters from the kwargs
            model = kwargs.get("model", None)
            messages = kwargs.get("messages", None)
            temperature = kwargs.get("temperature", None)
            top_k = kwargs.get("top_k", None)
            top_p = kwargs.get("top_p", None)
            max_tokens = kwargs.get("max_tokens", None)
            stream = kwargs.get("stream", False)
            tools = kwargs.get("tools", None)
            if tools:
                stream = False
            
            # Recreate kwargs for the ollama chat() function
            kwargs={
                "model": model,
                "messages": messages,
                "options": {
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                    "max_tokens": max_tokens,
                },
                "stream": stream,
                "tools": tools,
            }
            response = chat(**kwargs)
            
            # Format Output
            from gai.openai.ollama_response_builders.completions_factory import CompletionsFactory
            factory = CompletionsFactory()
            if stream and not tools:
                response = factory.chunk.build_stream(response)
                response = attach_extractor(response,stream)  
                response = (chunk for chunk in response)
            else:
                if tools:
                    response = factory.message.build_toolcall(response)
                else:
                    response = factory.message.build_content(response)
                response = attach_extractor(response,stream)
            return response
            
        
        raise Exception(f"completions.patched_create: Model {model} not found in config")
    
    def patch_parse(**kwargs):
        # The model is required to determine the client type patched to the openai_client so it should be determined first.
        model = kwargs.get("model", None)
        if not model:
            raise Exception("completions.patched_create: Model not provided")

        # Based on the model name, determine the client used to generate completions, eg. "gai" uses ttt_client.
        client_config = GaiClientConfig.from_name(model)
        if file_path:
            client_config = GaiClientConfig.from_name(model,file_path)
        
        if client_config and client_config.client_type == "gai":

            from gai.ttt.client.ttt_client import TTTClient
            ttt = TTTClient(client_config)
            
            # Remove the model from the kwargs as it is not required by the TTTClient
            kwargs.pop("model")        

            # If response_format is provided, use it as the json_schema for the response.
            if kwargs.get("response_format"):
                from pydantic import BaseModel
                schema = kwargs.pop("response_format")
                kwargs["json_schema"] = schema
                if issubclass(schema,BaseModel):
                    kwargs["json_schema"] = schema.model_json_schema()

            stream = kwargs.get("stream",False)
            kwargs["stream"] = stream
            
            response = ttt(**kwargs)
            return response
        
        # If the model is an ollama model, route to ollama chat() function.
        if client_config and client_config.client_type == "ollama":
            from ollama import chat
            
            # Extract the required parameters from the kwargs
            model = kwargs.get("model", None)
            messages = kwargs.get("messages", None)
            temperature = kwargs.get("temperature", None)
            top_k = kwargs.get("top_k", None)
            top_p = kwargs.get("top_p", None)
            max_tokens = kwargs.get("max_tokens", None)

            json_schema=None
            if kwargs.get("response_format"):
                from pydantic import BaseModel
                schema = kwargs.pop("response_format")
                if type(schema) is dict:                
                    json_schema = schema
                else:
                    import inspect
                    if inspect.isclass(schema):
                        if issubclass(schema,BaseModel):
                            json_schema = schema.model_json_schema()
                    else:
                        raise Exception("completions.patched_create: response_format must be a dict or a pydantic BaseModel")

            stream = False
            
            # Recreate kwargs for the ollama chat() function
            kwargs={
                "model": model,
                "messages": messages,
                "options": {
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                    "max_tokens": max_tokens,
                },
                "stream": stream,
                "format": json_schema,
            }
            response = chat(**kwargs)
            
            # Format Output
            from gai.openai.ollama_response_builders.completions_factory import CompletionsFactory
            factory = CompletionsFactory()
            response = factory.message.build_content(response)
            response = attach_extractor(response,stream)
            return response        
        
        # If the model is an openai model, route to openai's chat.completions.create() function.            
        if client_config and client_config.client_type == "openai" and client_config.model in get_args(ChatModel):
            stream=kwargs.pop("stream",False)
            response = openai_parse(**kwargs)
            response = attach_extractor(response,stream)
            return response

    openai_client.chat.completions.create = patched_create    
    openai_client.beta.chat.completions.parse = patch_parse
    
    return openai_client    





from gai.lib.common.generators_utils import chat_string_to_list
from gai.lib.common.logging import getLogger
logger = getLogger(__name__)
from gai.lib.config import GaiClientConfig


from openai.types.chat_model import ChatModel
from openai import OpenAI
from typing import get_args,Union, Optional,Callable
from gai.ttt.client.attach_extractor import attach_extractor

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
def patch_chatcompletions(openai_client:OpenAI):

    # Save the original openai.completions.create function
    openai_create = openai_client.chat.completions.create

    # Replace openai.completions.create with a wrapper over the original create function
    def patched_create(**kwargs):
        
        # The model is required to determine the client type patched to the openai_client so it should be determined first.
        model = kwargs.get("model", None)
        if not model:
            raise Exception("completions.patched_create: Model not provided")

        # Based on the model name, determine the client used to generate completions, eg. "gai" uses ttt_client.
        client_config = GaiClientConfig.from_name(model)
        
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
                    kwargs["json_schema"] = schema.schema()
            
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
        
        raise Exception(f"completions.patched_create: Model {model} not found in config")

    openai_client.chat.completions.create = patched_create    
    return openai_client    





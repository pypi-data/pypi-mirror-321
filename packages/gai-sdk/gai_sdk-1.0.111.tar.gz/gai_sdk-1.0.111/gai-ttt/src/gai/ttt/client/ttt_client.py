
import os
import json
from dotenv import load_dotenv
load_dotenv()
from typing import Union, Optional

from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk

from gai.lib.common.generators_utils import chat_string_to_list
from gai.lib.common.http_utils import http_post
from gai.lib.common.errors import ApiException
from gai.lib.config import GaiClientConfig
from gai.lib.common.logging import getLogger
from gai.ttt.client.attach_extractor import attach_extractor
logger = getLogger(__name__)

class TTTClient:

    # config is either a string path or a component config
    def __init__(self, config: Optional[Union[GaiClientConfig|dict]]=None,name:Optional[str]="ttt", file_path:str=None):
        
        # Load from default config file
        self.config:GaiClientConfig = None
        
        # Convert to ClientLLMConfig
        if isinstance(config, dict):
            # Load default config and patch with provided config
            self.config = GaiClientConfig.from_dict(config)
        elif isinstance(config, GaiClientConfig):
            self.config = config
        elif name:
            # If path is provided, load config from path
            self.config = GaiClientConfig.from_name(name=name,file_path=file_path)
        else:
            raise ValueError("Invalid config or path provided")

    # Generate non stream dictionary response for easier unit testing
    def _generate_dict(self, **kwargs):
        response=None
        url = kwargs.pop("url")
        timeout = kwargs.pop("timeout",30.0)
        try:
            response = http_post(url, data={**kwargs},timeout=timeout)
            jsoned=response.json()
            completion = ChatCompletion(**jsoned)
        except ApiException as he:
                raise he
        except Exception as e:
            logger.error(f"completions._generate_dict: error={e} response={response}")
            raise e

        return completion

    # Generate streamed dictionary response for easier unit testing
    def _stream_dict(self, **kwargs):
        response=None
        url = kwargs.pop("url")
        timeout = kwargs.pop("timeout",30.0)
        try:
            response = http_post(url, data={**kwargs},timeout=timeout)
        except ApiException as he:
                raise he
        except Exception as e:
            logger.error(f"completions._stream_dict: error={e}")
            raise e

        for chunk in response.iter_lines():
            try:
                chunk = chunk.decode("utf-8")
                if type(chunk)==str:
                    yield ChatCompletionChunk(**json.loads(chunk))
            except Exception as e:
                # Report the error and continue
                logger.error(f"completions._stream_dict: error={e}")
                pass


    """
    Description:
    This function is a monkey patch for openai's chat.completions.create() function.
    It will override the default completions.create() function to call the local llm instead of gpt-4.
    Example:
    openai_client.chat.completions.create = create
    """

    def __call__(self, 
                messages: str | list, 
                stream: bool = True, 
                max_tokens: int = None, 
                temperature: float = None, 
                top_p: float = None, 
                top_k: float = None,
                tools: list = None,
                tool_choice: str = None,
                stop: list = None,
                timeout: float = 30.0,
                json_schema: dict = None):
        
        # Prepare messages
        if not messages:
            raise Exception("Messages not provided")
        if isinstance(messages, str):
            messages = chat_string_to_list(messages)
        if messages[-1]["role"] != "assistant":
            messages.append({"role": "assistant", "content": ""})

        # Prepare payload
        kwargs = {
            "url": self.config.url,
            "messages": messages,
            "stream": stream,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "json_schema": json_schema,
            "tools": tools,
            "tool_choice": tool_choice,
            "stop": stop,
            "timeout": timeout
        }

        if not stream:
            response = self._generate_dict(**kwargs)
        else:
            response = (chunk for chunk in self._stream_dict(**kwargs))

        response = attach_extractor(response, stream)
        return response

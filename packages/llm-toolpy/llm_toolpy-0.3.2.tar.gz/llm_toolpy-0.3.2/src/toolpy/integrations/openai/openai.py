import time
import os
from typing import Optional, List, Tuple

import openai

from toolpy.llm import LLMInterface, Role

class OpenAIInterface(LLMInterface):
    _client : openai.OpenAI | None = None 

    def __init__(self, model:str, n_retry:int = 0, 
                 api_key:Optional[str] = None, 
                 base_url:Optional[str]=None,
                 client:openai.OpenAI|None = None) -> None:
        super().__init__(support_json_mode=True, support_multi_thread=True, n_retry=n_retry)

        if client is not None:
            OpenAIInterface._client = client
        elif OpenAIInterface._client is None:

            if api_key is None:
                api_key = os.environ.get("OPENAI_API_KEY")

            if api_key is None:
                api_key = "token"

            OpenAIInterface._client = openai.OpenAI(
                    base_url="http://localhost:8000/v1",
                    api_key="token",
                )

        self._model = model

    def query(self, prompt: List[Tuple[Role, str]], json_mode: bool, json_schema:Optional[str] = None) -> str:
        messages = []
        for p in prompt:
            if p[0] == Role.SYSTEM:
                role = "system"
            else:
                role = "user"

            message = {"role":role, "content":p[1]}
            messages.append(message)

        extra_body = None
        response_format = None
        if json_mode:
            if json_schema is None: 
                response_format = {"type": "json_object"}
            else:
                extra_body = {"guided_json":json_schema}

        chat_completion = None
        while chat_completion is None:
            try:
                chat_completion = OpenAIInterface._client.chat.completions.create(
                                messages=messages,
                                model=self._model,
                                response_format=response_format,
                                extra_body=extra_body
                            )
                
            except openai.RateLimitError as e:
                print(e)
                time.sleep(2)
        
        return chat_completion.choices[0].message.content
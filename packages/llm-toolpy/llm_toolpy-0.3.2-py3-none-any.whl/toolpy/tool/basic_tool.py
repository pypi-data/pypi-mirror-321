import copy
from types import MappingProxyType
from typing import Optional, Dict, Tuple

from toolpy.llm import Role
from .tool import Tool, TextLike

class BasicTool(Tool):

    def __init__(self, description:str, input_description:Dict[str, str], prompt_template:str, return_description:Dict[str,str],
                 system_message:Optional[str] = None, 
                 model_name: Optional[str] = None,
                 json_mode:bool=False,
                 json_schema:Optional[str]=None) -> None:
        
        super().__init__(description=description, input_description=input_description, model_name=model_name)
    
        self._prompt_template = prompt_template
        self._return_description = return_description #MappingProxyType(return_description)
        self._system_message = system_message
        self._json_mode = json_mode
        self._json_schema = json_schema

    def _execute(self, query:Dict[str, str], 
                context:str) -> Tuple[Dict[str, TextLike], Dict[str, str]]:

        prompt = []

        if self._system_message is not None:
            prompt.append((Role.SYSTEM, self._system_message))

        user_message = ""
        if context is not None:
            user_message += context +"\n"
        user_message += self._prompt_template.format(**query)

        prompt.append((Role.USER, user_message))

        return self._query(prompt, self._json_mode, self._json_schema), copy.deepcopy(self._return_description)
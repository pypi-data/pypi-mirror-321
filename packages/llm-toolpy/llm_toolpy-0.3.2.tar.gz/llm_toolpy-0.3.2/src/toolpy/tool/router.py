from typing import Any, List, Optional

from .tool import Tool
from .basic_tool import BasicTool
from .adapter import Adapter

class Router(BasicTool):
    _description = '''Selects the next tool to use.'''

    _system_message = '''You are a tool selector that outputs in JSON.
For each selection, you must provide a throught about the previous content and why you are selecting this tool.

The JSON object must use the schema: {'throught':'str',
'tool_name':'str',
'query':'object'}

Please use a valid JSON format.
'''

    _base_prompt = '''
You have available the following tools:
{avaiable_tools}

Your goal is:
{goal}

Considering all this context, select the next tool to use.
'''
    
    _input_description = {"goal":"the final goal",
        "avaiable_tools":"list of avaiable tools, with name, description and input description"}

    _return_description = {'throught':'why use this tool',
                            'tool_name':'which tool to use',
                            'query':'what send to the tool'}

    def __init__(self, model_name:Optional[str] = None) -> None:

        super().__init__(self._description, self._input_description, self._base_prompt, 
                         self._return_description, self._system_message,  model_name,
                         json_mode=True)
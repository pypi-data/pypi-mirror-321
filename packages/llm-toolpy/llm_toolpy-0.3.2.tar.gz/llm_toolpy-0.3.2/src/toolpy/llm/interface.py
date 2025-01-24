import abc
import enum
import threading
import warnings
from typing import List, Union, Dict, final, Tuple, Optional

class Role(enum.Enum):
    SYSTEM = 1
    USER = 2

class FakeLock:
    def acquire(self) -> bool:
        return True
    
    def release(self):
        pass

QueryLike = Union[str, List[Tuple[Role, str]]]

class LLMInterface(abc.ABC):
    
    def __init__(self, support_json_mode:bool=False, support_multi_thread:bool=False, n_retry:int=0) -> None:
        super().__init__()
        
        self._support_json_mode = support_json_mode
        self._support_multi_thread = support_multi_thread
        self._n_retry = n_retry

        if self._support_multi_thread:
            self._query_lock = FakeLock()
        else:
            self._query_lock = threading.Lock()
            
            


    @final
    def __call__(self, prompt:QueryLike, json_mode:bool=False, json_schema:Optional[str]=None) -> str:

        if json_mode and not self._support_json_mode:
            warnings.warn(f"JSON mode is not supported by this LLM \
                        {self.__class__.__name__}, option will be \
                        ignored (json_mode=True is not valid).")

        if isinstance(prompt, str):
            prompt = [(Role.USER, prompt)]

        self._query_lock.acquire()
        
        result = None

        if self._n_retry == 0:
            try:
                result = self.query(prompt, json_mode, json_schema)
            except:
                self._query_lock.release()

                raise RuntimeError(f"Query could not be executed. Model \
                               failed with prompt:\n---\n{prompt}\n---")
        else:
            for _ in range(self._n_retry):
                try:
                    result = self.query(prompt, json_mode, json_schema)

                except KeyboardInterrupt as e:
                    raise e
                
                except Exception as e:
                    print(e)
                    pass

                if result is not None:
                    break

            else:
                self._query_lock.release()

                raise RuntimeError(f"Query could not be executed. Model \
                                failed with prompt:\n---\n{prompt}\n---")

        self._query_lock.release()

        return result
    
    @abc.abstractmethod
    def query(self, prompt:List[Tuple[Role, str]], json_mode:bool, json_schema:Optional[str]=None) -> str:
        ...

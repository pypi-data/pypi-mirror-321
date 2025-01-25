from typing import TypeVar
from fwdi.Utilites.waitable_event import WaitableEvents


_T = TypeVar('_T')

class JobTask():
    def __init__(self, fn:callable, args:list) -> None:
        self._fn:callable = fn
        self._args:dict = args
        self._event:WaitableEvents = WaitableEvents()
    
    def wait(self)->_T:
        ret, result = self._event.wait()
        return result if ret else None
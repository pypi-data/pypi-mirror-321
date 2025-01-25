from typing import TypedDict
from appier import API as BaseAPI

from .job import JobAPI
from .node import NodeAPI

BASE_URL: str = ...

class Ping(TypedDict):
    time: float

class API(BaseAPI, JobAPI, NodeAPI):
    def ping(self) -> Ping: ...

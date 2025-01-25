from typing import Type

from fastapi import APIRouter
from frf.endpoints.base_endpoint import BaseEndpoint

class BaseAPIRouter(APIRouter):
    def include_endpoint(self, endpoint_cls: Type[BaseEndpoint]):
        """
        Include a BaseEndpoint-derived class into the router.
        """
        endpoint_cls.register(self)

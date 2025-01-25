from typing import Type

from fastapi import APIRouter
from frf.endpoints.base_endpoint import BaseEndpoint

class BaseAPIRouter(APIRouter):
    def include_endpoints(self, *endpoint_classes: Type[BaseEndpoint]):
        """
        Include a BaseEndpoint-derived class into the router.
        """
        for endpoint_cls in endpoint_classes:
            endpoint_cls.register(self)

from fastapi import APIRouter, Depends
from inspect import isfunction, ismethod
from typing import Callable, List, Type, TypeVar, Any

T = TypeVar("T", bound="BaseEndpoint")

class BaseEndpoint:
    prefix: str = ""
    tags: List[str] = []

    @classmethod
    def register(cls: Type[T], router: APIRouter):
        """
        Registers the class-based endpoint with the router.
        """
        instance = cls()  # Create an instance of the class
        for attr_name in dir(instance):
            method = getattr(instance, attr_name)
            if not isfunction(method) and not ismethod(method):
                continue

            route_info = getattr(method, "_route_info", None)
            if route_info:
                path = route_info["path"]
                http_method = route_info["method"]
                dependencies = route_info["dependencies"]
                extra_kwargs = route_info["extra_kwargs"]  # <= new

                full_path = f"{cls.prefix}{path}"
                router.add_api_route(
                    path=full_path,
                    endpoint=method,
                    methods=[http_method],
                    dependencies=[Depends(lambda: instance)] + (dependencies or []),
                    tags=cls.tags,
                    **extra_kwargs,
                )

    @staticmethod
    def route(
            path: str,
            method: str,
            *,
            dependencies: List[Callable] = None,
            **extra_kwargs: Any
    ):
        """
        Decorator to define route metadata on a method.
        Allows additional FastAPI kwargs (like response_model, status_code, etc.).
        """

        def decorator(func: Callable):
            func._route_info = {
                "path": path,
                "method": method.upper(),
                "dependencies": dependencies or [],
                "extra_kwargs": extra_kwargs,  # store everything else
            }
            return func

        return decorator

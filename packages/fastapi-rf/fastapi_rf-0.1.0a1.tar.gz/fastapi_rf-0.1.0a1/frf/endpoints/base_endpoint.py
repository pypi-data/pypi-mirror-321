from fastapi import Request, Response
from fastapi.responses import JSONResponse
from typing import Any


class BaseEndpoint:
    def __init__(self):
        # Set the __name__ attribute for FastAPI's OpenAPI generation
        self.__name__ = self.__class__.__name__

    async def get(self, request: Request) -> Any:
        """
        Handle GET requests. Override to provide custom behavior.
        """
        raise NotImplementedError("GET method not implemented.")

    async def post(self, request: Request) -> Any:
        """
        Handle POST requests. Override to provide custom behavior.
        """
        raise NotImplementedError("POST method not implemented.")

    async def __call__(self, request: Request) -> Response:
        """
        Dispatch the request to the appropriate HTTP method handler.
        """
        method = request.method.lower()
        handler = getattr(self, method, None)

        if not handler:
            return JSONResponse(
                content={"error": f"Method {method.upper()} not allowed"},
                status_code=405,
            )

        # Await the handler to resolve the coroutine
        result = await handler(request)

        # If the result is already a Response, return it directly
        if isinstance(result, Response):
            return result

        # Ensure the result is JSON-serializable
        if not isinstance(result, (dict, list, str, int, float, bool, type(None))):
            raise ValueError(
                f"Handler method returned an unsupported type: {type(result)}"
            )

        return JSONResponse(content=result)

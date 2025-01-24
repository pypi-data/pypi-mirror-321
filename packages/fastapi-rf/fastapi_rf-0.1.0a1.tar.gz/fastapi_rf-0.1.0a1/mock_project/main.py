from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from frf.endpoints.base_endpoint import BaseEndpoint

app = FastAPI()


class HelloWorldEndpoint(BaseEndpoint):
    async def get(self, request: Request):
        return {"message": "Hello, World!"}  # Valid JSON-serializable data

    async def post(self, request: Request):
        data = await request.json()
        return JSONResponse(content=data)  # Valid FastAPI Response


app.add_api_route(
    "/hello",
    HelloWorldEndpoint(),
    methods=["GET", "POST"],
    summary="Greeting Endpoint",
    description="This endpoint supports both GET and POST requests."
)

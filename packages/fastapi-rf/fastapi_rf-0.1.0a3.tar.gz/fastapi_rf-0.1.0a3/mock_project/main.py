from fastapi import FastAPI
from frf.endpoints.base_endpoint import BaseEndpoint
from frf.routers.base_router import BaseAPIRouter

app = FastAPI()
router = BaseAPIRouter()

class MyEndpoint(BaseEndpoint):
    prefix = "/items"
    tags = ["Items"]

    @BaseEndpoint.route("/list", "GET")
    async def get_items(self):
        return {"message": "List of items"}

    @BaseEndpoint.route("/create", "POST")
    async def create_item(self, data: dict):
        return {"message": "Item created", "data": data}


class SecondEndpoint(BaseEndpoint):
    prefix = "/users"
    tags = ["Users"]

    @BaseEndpoint.route("/list", "GET")
    async def get_users(self):
        return {"message": "List of users"}

    @BaseEndpoint.route("/create", "POST")
    async def create_user(self, data: dict):
        return {"message": "User created", "data": data}

# Register the endpoint
router.include_endpoints(MyEndpoint, SecondEndpoint)
app.include_router(router)

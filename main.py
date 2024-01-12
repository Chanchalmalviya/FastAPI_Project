from fastapi import FastAPI
from user import api as UserAPI
from user import router as APIRouter

from tortoise.contrib.fastapi import register_tortoise

app =FastAPI()

app.include_router(APIRouter.router)
app.include_router(UserAPI.app, tags=["api"])

JWT_SECRET = 'myjwtsecret'

register_tortoise(
    app,
    db_url="postgres://postgres:12345@127.0.0.1/fastapi",
    modules={'models': ['user.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)




# app =FastAPI()

# @app.get('/')
# async def index():
#     return("This is a Python")


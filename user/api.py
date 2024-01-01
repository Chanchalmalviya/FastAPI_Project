from fastapi import APIRouter
from .models import *
from .pydantic_models import Persone

app = APIRouter()



@app.post("/create_user")
async def user_post(data:Persone):
    if await User.filter(email=data.email).exists():
        return {"status":True,"message":"Email Already Exists"}
    
    elif await User.filter(phone=data.phone).exists():
        return {"status":True,"message":"Phone Already Exists"}
    
    else:
        user_obj = await User.create(name=data.name,email=data.email,phone=data.phone,id=data.id,password=data.password)
        return user_obj
    
# @app.get("/")
# async def getdata():
#     user_obj = await User.all()
#     return user_obj
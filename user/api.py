from fastapi import APIRouter
from .models import *
from .pydantic_models import Persone,deleteuser,getdata,updateuser
from .pydantic_models import user,get_user,delete_user
from passlib.context import CryptContext
app = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")

def verify_password(plan_password,hashed_password):
    return pwd_context.verify(plan_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)



@app.post("/ragistration/")
async def create_user(data:user):
    phone_number = str(data.phone)

    if len(phone_number) !=10:
        return {"status":False, "message":"invalid Phone Number"}
    if await User.exists(phone=phone_number):
        return {"status":False, "message":"Phone Number already Exista"}
    elif await User.exists(email=data.email):
        return {"status":False, "message":"email Number already Exista"}
    else:
        user_obj = await User.create(name=data.name,email=data.email,
                                     phone=phone_number,
                                     password=get_password_hash(data.password))
        return user_obj


@app.post("/get_user_info/")
async def get_info(data:get_user):
    user_obj = await User.get(id=data.id)
    return user_obj


@app.delete("/delete_info/")
async def delete_info(data:delete_user):
    user_obj = await User.get(id=data.id).delete()
    return user_obj







@app.post("/create_user")
async def user_post(data:Persone):
    if await Person.filter(email=data.email).exists():
        return {"status":True,"message":"Email Already Exists"}
    
    elif await Person.filter(phone=data.phone).exists():
        return {"status":True,"message":"Phone Already Exists"}
    
    else:
        user_obj = await Person.create(name=data.name,email=data.email,phone=data.phone,password=data.password)
        return user_obj
    


@app.post("/")
async def usedata(data:getdata):
    user_obj = await Person.get(id=data.user_id)
    return user_obj



@app.delete("/delete/")
async def delete_user(data:deleteuser):
    user = await Person.get(id=data.id).delete()
    return user


@app.put("/updateuser/")
async def update_data(data:updateuser):
    user = await Person.get(id=data.id)
    if not user:
        return {"status":False,"message":"user not Found"}
    else:
        user_obj = await Person.filter(id=data.id).update(name=data.name,email=data.email,
                                                    phone=data.phone)
        return  {"status":True,"message":"User Update sucessfully"}
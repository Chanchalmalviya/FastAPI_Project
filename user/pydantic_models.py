from pydantic import BaseModel



class user(BaseModel):
    name:str
    email:str
    phone:int
    password:str

class get_user(BaseModel):
    id:int

class delete_user(BaseModel):
    id:int    

class Persone(BaseModel):
    name:str
    email:str
    phone:int
    password:str


class deleteuser(BaseModel):
    id:int  


class getdata(BaseModel):
    user_id:int      


class updateuser(BaseModel):
    id :int
    name:str
    email:str
    phone:int    
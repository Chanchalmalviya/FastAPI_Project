from pydantic import BaseModel



class Persone(BaseModel):
    name:str
    email:str
    phone:int
    password:str
    id:int
from fastapi import APIRouter,Request,Form
from .models import *
from fastapi.responses import HTMLResponse,RedirectResponse
from .pydantic_models import Persone,deleteuser,getdata,updateuser
from .pydantic_models import user,get_user,delete_user,update_user
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates
router = APIRouter()
SECRET = "your-secret-key"

pwd_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")
templates = Jinja2Templates(directory = "user/templates")

def verify_password(plan_password,hashed_password):
    return pwd_context.verify(plan_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


@router.get("/", response_class=HTMLResponse)
async def read_iteam(request:Request):
    return templates.TemplateResponse("index.html",
                                      {"request":request}
                                      )


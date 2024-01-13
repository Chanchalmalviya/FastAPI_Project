from fastapi import APIRouter,Request,Form,status
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

@router.post("/ragistration/",response_class=HTMLResponse)
async def read_item(request:Request,full_name: str = Form(...),
                    Email: str = Form(...),
                    Phone: str = Form(...),
                    Password: str = Form(...)):
    if await User.filter(email=Email).exists():
       
        return RedirectResponse("/",status_code=status.HTTP_302_FOUND)
    
    elif await User.filter(phone=Phone).exists():
      
        return RedirectResponse("/",status_code=status.HTTP_302_FOUND)
    
    else:
        await User.create(email=Email,
                          name=full_name,
                          phone=Phone,
                          password=get_password_hash(Password))
        return RedirectResponse("/login/",status_code=status.HTTP_302_FOUND)
    
@router.get("/login/",response_class=HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("login.html",{
        "request":request,
    })

@router.get("/table/",response_class=HTMLResponse)
async def read_item(request:Request):
    person = await User.all()
    return templates.TemplateResponse("table.html",{
        "request":request,
        "person":person
    })


from pydantic import BaseModel
from typing import Optional

class adduser(BaseModel):
    user_name : str
    user_email : str
    user_password : str
    user_role : str
    user_status : str


class Login(BaseModel):
    user_email : str
    user_password : str


class Updateuser(BaseModel):
    new_role : Optional[str] = None
    new_status : Optional[str] = None

class GetUsers(BaseModel):
    role : Optional[str] = None
    status : Optional[str] = None
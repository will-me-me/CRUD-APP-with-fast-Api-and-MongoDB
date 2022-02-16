from datetime import datetime, timedelta
from dataclasses import field
import email
from typing import Optional
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Dict
import time 
from pydantic import BaseModel, EmailStr, Field

class Admin(BaseModel):
    username:str=Field(...)
    email:EmailStr=Field(...)
    password:str=Field(...)

class Config():
    schema_extra={
         "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
    }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


    
from lib2to3.pgen2 import token
from os import access
import time
from typing import Dict


import jwt
from decouple import config 

JWT_SECRET= config('secret')
JWT_ALGORTHM= config('algorithm')

def token_responses():
    return{
        'access_token':token
    }

def sign_jwt(admin_id:str)->Dict[str,str]:
    payload={
        'admin_id':admin_id,
        'epiries':time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORTHM)
    return token_responses()

def decodeJWT(token: str)->dict:
    try:
        decoded_token=jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORTHM])
        return decoded_token if decoded_token['expires']>=time.time() else None
    except:
        return { }


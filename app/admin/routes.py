from ast import Return
from asyncio.unix_events import _UnixSelectorEventLoop
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder


from app.admin.auth import sign_jwt

from app.admin.model import(
    add_new_admin,
    admin_helper,
    check_user,
    update_admin
)

from app.admin.schema import(
    Admin,
    UserLoginSchema
    
)
from app.auth_bearer import JWTBearer
from app.server.models.student import ResponsModel

router = APIRouter()

# admin login
@router.post('/login',response_description='admin sigin')
async def admin_login(admin:UserLoginSchema = Body(...)):
    if check_user(admin):
        return sign_jwt(admin.email)
    return {'message': 'Wrong login details'}


# add admin
@router.post('/add', response_description='admin added into db', dependencies=[Depends(JWTBearer())])
async def create_admin(admin: Admin =Body(...)):
    admin=jsonable_encoder(admin)
    new_admin=await add_new_admin(admin)
    return ResponsModel(new_admin, 'Admin added successfully')
    # return {ResponsModel(new_admin, 'Admin added succesfully'),sign_jwt(admin.email)}

from unittest import async_case
from bson.objectid import ObjectId
import motor.motor_asyncio
from app.admin.schema import UserLoginSchema
from app.server.database import admin_collection

def admin_helper(admin):
    pass



# get all admins
async def retrive_admin():
    admins=[]
    async for admin in admin_collection.find():
        admins.append(admin_helper(admin))
    return admin

    # add a new admin

async def add_new_admin(admin_data: dict)->str:
    admin=await admin_collection.insert_one(admin_data)
    new_admin =await admin_collection.find_one({'_id': admin.inserted_id})
    return admin_helper(new_admin)

# update admin

async def update_admin(id:str, data:dict):
    if len(data)<1:
        return False
    admin = await admin_collection.find_one({'_id': ObjectId(id)})
    if admin:
        updated_admin = await admin_collection.update_one(
            {'_id':ObjectId(id)},{'$set':data}
        )
        if updated_admin:
            return True
        return False

# check user

async def check_user(data: UserLoginSchema):
    admins=[]
    async for user in admin_collection.find_one():
        admins.append(user)
        if user.email==data.email and user.password==data.password:
            return True
        return False 


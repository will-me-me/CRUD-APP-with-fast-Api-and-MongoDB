from pkgutil import ImpImporter
from fastapi import FastAPI
from app.server.routes.student import router as StudentRouter
from app.admin.routes import router as AdminRouter

app=FastAPI()
app.include_router(AdminRouter,tags=['admin'], prefix='/admin')
app.include_router(StudentRouter, tags=["Students"], prefix="/student")

@app.get('/',tags=['Root'])
async def read_root():
    return{'messsage':"Welcome to this fantastic app!!"}


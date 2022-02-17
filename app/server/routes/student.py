from ast import Return
from asyncio.unix_events import _UnixSelectorEventLoop
from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from app.auth_bearer import JWTBearer
from app.admin.auth import sign_jwt
from app.server.database import(
    add_student,
    delete_student,
    retrive_student,
    retrive_students,
    student_helper,
    update_student,
    
)
from app.server.models.student import(
    ErrorResponseModel,
    StudentSchema,
    UpdateStudentModel,
    ResponsModel
)

router = APIRouter()

#add student
@router.post('/',response_description='student data dded into the database')
async def add_student_data(student:StudentSchema=Body(...)):
    student=jsonable_encoder(student)
    new_student=await add_student(student)
    return ResponsModel(new_student, 'Student added successfully')

#get all added student
@router.get('/',dependencies=[Depends(JWTBearer())], response_description='students retrived')
async def get_students():
    students = await retrive_students()
    if students:
        return ResponsModel(students, 'Students data retrived succesfully')
    return ResponsModel(students, 'Empty list Returned')

# get student by id
@router.get('/{id}', response_description='student with a given id is returned')
async def get_student_data(id):
    student = await retrive_student(id)
    if student:
        return ResponsModel(student, 'Student data retrived succesfully')
    return ErrorResponseModel('An error occured', 404, 'Student does not exist')

# Update Student
@router.put('/id',dependencies=[Depends(JWTBearer())], response_description='Updates the student with a given id')
async def update_student_data(id:str, req:UpdateStudentModel=Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student=await update_student(id, req)
    if updated_student:
        return ResponsModel(
            'Student with ID: {} name update is successful'.format(id),
            'Student Updated suceesfully'

        )
    return ErrorResponseModel(
        'An error occured',
        404,
        "There was an error updating the student data",
    )

#Delete student with a given id

@router.delete('/{id}',dependencies=[Depends(JWTBearer())], response_description='Student data deleted from the database')
async def delete_student_data(id: str):
    deleted_student= await delete_student(id)
    if deleted_student:
        return ResponsModel(
            'Student with ID: {} removed'.format(id), 'Student deleted succesfully'
        )
    return ErrorResponseModel(
        'An error Occured', 404, 'Student with id {0} does not exist'.format(id)
    )

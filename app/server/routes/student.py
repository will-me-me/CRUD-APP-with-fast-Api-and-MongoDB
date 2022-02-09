from ast import Return
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

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
@router.post('/', response_description='student data dded into the database')
async def add_student_data(student:StudentSchema=Body(...)):
    student=jsonable_encoder(student)
    new_student=await add_student(student)
    return ResponsModel(new_student, 'Student addes successfully')

#get all added student
@router.get('/', response_description='students retrived')
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
from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("students_collection")


#helpers

def student_helper(student) -> dict:
    return{
         "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"]
    }

# get all students from the database
async def retrive_students():
    students=[]
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

# Add new student
async def add_student(student_data: dict)->dict:
    student=await student_collection.insert_one(student_data)
    new_student=await student_collection.find_one({'_id': student.inserted_id})
    return student_helper(new_student)

# get a student with a matching id
async def retrive_student(id:str)->dict:
    student=await student_collection.find_one({'_id': ObjectId(id)})
    if student:
        return student_helper(student)

# update student with a matcing id

async def update_student(id:str, data:dict):
    # return false if empty request body
    if len(data)<1:
        return False
    student= await student_collection.find_one({'_id': ObjectId(id)})
    if student:
        updated_student=await student_collection.update_one(
            {'_id':ObjectId(id)}, {'$set': data}

        )
        if updated_student:
            return True
        return False
    
# Delete a student from the database
async def delete_student(id:str):
    student= await student_collection.find_one({'_id':ObjectId(id)})
    if student:
        await student_collection.delete_one({'_id': ObjectId})
        return True
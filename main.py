from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import create_connection, create_student, get_students, get_student_by_id, update_student, delete_student, MyMongoDB

app = FastAPI()
connection = create_connection()
mongodb_connector = MyMongoDB() 

class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.post("/students/")
def api_create_student(student: Student):
    create_student(connection, student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/students/")
def api_get_students():
    students = get_students(connection)
    return students

@app.get("/students/{student_id}")
def api_get_student(student_id: int):
    student = get_student_by_id(connection, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}")
def api_update_student(student_id: int, student: Student):
    update_student(connection, student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def api_delete_student(student_id: int):
    delete_student(connection, student_id)
    return {"message": "Student deleted successfully"}

## MongoDB
'''
POST http://127.0.0.1:8000/mongo/students
{"name":"Raju","age":23,"grade":"A-"}
'''
@app.post("/mongo/students/")
def api_mongo_create_student(student: Student):
    mongodb_connector.create_student(student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

'''
GET http://127.0.0.1:8000/mongo/students/
'''
@app.get("/mongo/students/")
def api_mongo_get_students():
    students = mongodb_connector.get_students()
    students = mongodb_connector.serialize(students)
    print(students,"Students List")
    return students

'''
GET http://127.0.0.1:8000/mongo/students/6693dcdd0ea3e664e16fb9ed
'''
@app.get("/mongo/students/{student_id}")
def api_mongo_get_student(student_id: str):
    student = mongodb_connector.get_student_by_id(student_id)
    student = mongodb_connector.serialize([student])
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

'''
PUT http://127.0.0.1:8000/mongo/students/6693dcdd0ea3e664e16fb9ed
{"name":"Raju","age":23,"grade":"A-"}
'''
@app.put("/mongo/students/{student_id}")
def api_mongo_update_student(student_id: str, student: Student):
    mongodb_connector.update_student(student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

'''
DELETE http://127.0.0.1:8000/mongo/students/6693dcdd0ea3e664e16fb9ed
'''
@app.delete("/mongo/students/{student_id}")
def api_mongo_delete_student(student_id: str):
    mongodb_connector.delete_student(student_id)
    return {"message": "Student deleted successfully"}

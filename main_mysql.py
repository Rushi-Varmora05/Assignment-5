from fastapi import FastAPI, HTTPException
from models import Student
from database_mysql import create_connection, create_student, get_students, get_student_by_id, update_student, delete_student

app = FastAPI()
connection = create_connection()

@app.post("/sql/students/")
def api_create_student(student: Student):
    create_student(connection, student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/sql/students/")
def api_get_students():
    students = get_students(connection)
    return students

@app.get("/sql/students/{student_id}")
def api_get_student(student_id: int):
    student = get_student_by_id(connection, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/sql/students/{student_id}")
def api_update_student(student_id: int, student: Student):
    update_student(connection, student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/sql/students/{student_id}")
def api_delete_student(student_id: int):
    delete_student(connection, student_id)
    return {"message": "Student deleted successfully"}

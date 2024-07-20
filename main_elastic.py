#elastic search
from fastapi import FastAPI
from models import Student
from database_elastic import MyElasticSearch

app = FastAPI()
es = MyElasticSearch()
@app.post("/elastic/students/")
def create_student(student: Student):
    es.create_student(student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/elastic/students/")
def get_students():
    students = es.get_students()
    return students

@app.get("/elastic/students/{student_id}")
def get_student(student_id: str):
    student = es.get_student_by_id(student_id)
    return student

@app.put("/elastic/students/{student_id}")
def update_student(student_id: str, student: Student):
    es.update_student(student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/elastic/students/{student_id}")
def delete_student(student_id: str):
    es.delete_student(student_id)
    return {"message": "Student deleted successfully"}

#elastic search
from fastapi import FastAPI
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from typing import List
from models import Student

app = FastAPI()
es = Elasticsearch(hosts=["https://localhost:9200"], 
                   http_auth=('elastic', '+7xrtpKUptYvMP*q5=sO'),
                   verify_certs=False)

@app.post("/elastic/students/")
def create_student(student: Student):
    es.index(index="students", body={"name": student.name, "age": student.age, "grade": student.grade})
    return {"message": "Student created successfully"}

@app.get("/elastic/students/")
def get_students():
    students = es.search(index="students")
    return students

@app.get("/elastic/students/{student_id}")
def get_student(student_id: str):
    student = es.get(index="students", id=student_id)
    return student

@app.put("/elastic/students/{student_id}")
def update_student(student_id: str, student: Student):
    es.update(index="students", id=student_id, body={"doc": {"name": student.name, "age": student.age, "grade": student.grade}})
    return {"message": "Student updated successfully"}

@app.delete("/elastic/students/{student_id}")
def delete_student(student_id: str):
    es.delete(index="students", id=student_id)
    return {"message": "Student deleted successfully"}

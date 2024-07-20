from fastapi import FastAPI, HTTPException
from models import Student
from database_neo4j import MyNeo4jDB

app = FastAPI()

neo4j_connector = MyNeo4jDB()

'''
POST http://127.0.0.1:8000/neo4j/students/
'''
@app.post("/neo4j/students/")
def api_neo4j_create_student(student: Student):
    neo4j_connector.create_student(student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

'''
GET http://127.0.0.1:8000/neo4j/students
'''
@app.get("/neo4j/students/")
def api_neo4j_get_students():
    students = neo4j_connector.get_students()
    students = neo4j_connector.serialize(students)
    return students

'''
GET http://127.0.0.1:8000/neo4j/students/{student_id}
'''
@app.get("/neo4j/students/{student_id}")
def api_neo4j_get_student(student_id: int):
    student = neo4j_connector.get_student_by_id(student_id)
    student = neo4j_connector.serialize([student])
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

'''
PUT http://127.0.0.1:8000/neo4j/students/{student_id}
'''
@app.put("/neo4j/students/{student_id}")
def api_neo4j_update_student(student_id: int, student: Student):
    neo4j_connector.update_student(student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

'''
DELETE http://127.0.0.1:8000/neo4j/students/{student_id}
'''
@app.delete("/neo4j/students/{student_id}")
def api_neo4j_delete_student(student_id: int):
    neo4j_connector.delete_student(student_id)
    return {"message": "Student deleted successfully"}


from fastapi import FastAPI
from database_faiss import MyFAISS
from models import Student

app = FastAPI()
my_faiss = MyFAISS()

#faiss 

'''
POST http://
'''
@app.post("/faiss/students/")
def api_faiss_create_student(student: Student):
    student_vector = my_faiss.vectorize_student(student.name)
    my_faiss.add_student(student_vector)
    return {"message": "Student added successfully"}


'''
POST http://
'''
@app.post("/faiss/students/search")
def api_faiss_get_student(student: Student):
    student_vector = my_faiss.vectorize_student(student.name)
    students = my_faiss.search_student(student_vector, 5)
    return students

'''
DELETE http://
'''
@app.delete("/faiss/students/{student_id}")
def api_faiss_delete_student(student_id: str):
    my_faiss.remove_student(student_id)
    return {"message": "Student removed successfully"}

'''
PUT http://
'''
@app.put("/faiss/students/{student_id}")
def api_faiss_update_student(student_id: str, student: Student):
    student_vector = my_faiss.vectorize_student(student.name)
    my_faiss.update_student(student_vector)
    return {"message": "Student updated successfully"}

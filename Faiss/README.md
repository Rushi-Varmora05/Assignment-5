**# FAISS CRUD API**
Implement CRUD operations 

**Run app** - python -m uvicorn main:app --reload

**Create new student - POST request**
http://127.0.0.1:8000/faiss/student/create/
body :
{
  "name": "Rushi"
}

**Read data : GET request**
http://127.0.0.1:8000/faiss/student/read/0

**Update data : PUT request**
http://127.0.0.1:8000/faiss/student/update/0
body :
{
  "name": "Rahil"
}

**Delete data : DELETE request**
http://127.0.0.1:8000/faiss/student/delete/0



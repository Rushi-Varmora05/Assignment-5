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

@app.post("/students/")
def create_student(student: Student):
    es.index(index="students", body={"name": student.name, "age": student.age, "grade": student.grade})
    return {"message": "Student created successfully"}

@app.get("/students/")
def get_students():
    students = es.search(index="students")
    return students

@app.get("/students/{student_id}")
def get_student(student_id: str):
    student = es.get(index="students", id=student_id)
    return student

@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):
    es.update(index="students", id=student_id, body={"doc": {"name": student.name, "age": student.age, "grade": student.grade}})
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    es.delete(index="students", id=student_id)
    return {"message": "Student deleted successfully"}

'''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  f2f8e01c0c9d43399372a0fe5abeb79ff0e62a72e99df6a2bf363eebd8f95103

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTcyLjE4LjAuMjo5MjAwIl0sImZnciI6ImYyZjhlMDFjMGM5ZDQzMzk5MzcyYTBmZTVhYmViNzlmZjBlNjJhNzJlOTlkZjZhMmJmMzYzZWViZDhmOTUxMDMiLCJrZXkiOiJGaXc2c3BBQnRpWF83b1FJdDhuQzpsTjgwRWxCQ1F2S3BUaUZ4VU5rcFNBIn0=

ℹ️ Configure other nodes to join this cluster:
• Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTcyLjE4LjAuMjo5MjAwIl0sImZnciI6ImYyZjhlMDFjMGM5ZDQzMzk5MzcyYTBmZTVhYmViNzlmZjBlNjJhNzJlOTlkZjZhMmJmMzYzZWViZDhmOTUxMDMiLCJrZXkiOiJGU3c2c3BBQnRpWF83b1FJdDhuQzpkendoX3pyYlJaR21JT1kxZVp0TnB3In0=

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.14.3`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

openssl s_client -connect localhost:9200 -showcerts </dev/null 2>/dev/null | openssl x509 -outform PEM > elasticsearch_cert.pem

/Library/Java/JavaVirtualMachines/adoptopenjdk-16.jdk/Contents/Home/lib/security/cacerts

'''

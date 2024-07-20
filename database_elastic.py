
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class MyElasticSearch:
    def __init__(self):
        self.client = Elasticsearch(hosts=["https://localhost:9200"], 
                   http_auth=('elastic', '+7xrtpKUptYvMP*q5=sO'),
                   verify_certs=False)
        print("Connection to Elastic Search successful")

    def check_connection(self):
        return self.client.ping()

    def create_student(self, name, age, grade):
        if not self.check_connection():
            return {"message": "Connection to Elastic Search failed"}
        self.client.index(index="students", body={"name": name, "age": age, "grade": grade})
        
    def get_students(self):
        if not self.check_connection():
            return {"message": "Connection to Elastic Search failed"}
        return self.client.search(index="students")

    def get_student_by_id(self, student_id):
        if not self.check_connection():
            return {"message": "Connection to Elastic Search failed"}
        return self.client.get(index="students", id=student_id)

    def update_student(self, student_id, name, age, grade):
        if not self.check_connection():
            return {"message": "Connection to Elastic Search failed"}
        self.client.update(index="students", id=student_id, body={"doc": {"name": name, "age": age, "grade": grade}})

    def delete_student(self, student_id):
        if not self.check_connection():
            return {"message": "Connection to Elastic Search failed"}
        self.client.delete(index="students", id=student_id)
     

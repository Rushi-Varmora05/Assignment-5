
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from bson.objectid import ObjectId

class MyElasticSearch:
    def __init__(self):
        self.client = Elasticsearch(hosts=["https://localhost:9200"], 
                   http_auth=('elastic', '+7xrtpKUptYvMP*q5=sO'),
                   verify_certs=False)
        print("Connection to Elastic Search successful")

    def create_student(self, name, age, grade):
        self.client.index(index="students", body={"name": name, "age": age, "grade": grade})
        
    def get_students(self):
        return self.client.search(index="students")

    def get_student_by_id(self, student_id):
        return self.client.get(index="students", id=student_id)

    def update_student(self, student_id, name, age, grade):
        self.client.update(index="students", id=student_id, body={"doc": {"name": name, "age": age, "grade": grade}})

    def delete_student(self, student_id):
        self.client.delete(index="students", id=student_id)
     

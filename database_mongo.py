
import pymongo
from bson.objectid import ObjectId

class MyMongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["school"]
        self.collection = self.db["students"]
        print("Connection to MongoDB successful")

    def create_student(self, name, age, grade):
        student = {"name": name, "age": age, "grade": grade}
        self.collection.insert_one(student)

    def get_students(self):
        return list(self.collection.find())

    def get_student_by_id(self, student_id):
        return self.collection.find_one({"_id": ObjectId(student_id)})

    def update_student(self, student_id, name, age, grade):
        query = {"_id": ObjectId(student_id)}
        new_values = {"$set": {"name": name, "age": age, "grade": grade}}
        self.collection.update_one(query, new_values)

    def delete_student(self, student_id):
        query = {"_id": ObjectId(student_id)}
        self.collection.delete_one(query)
        
    def serialize(self, data):
        for student in data:
            student["_id"] = str(student["_id"])
        return data
        

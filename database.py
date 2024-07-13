import mysql.connector
from mysql.connector import Error
import pymongo
from mongoose import ObjectId

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  # Add your password if required
            database="school"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def fetch_query(connection, query, values=None):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
    return result

def create_student(connection, name, age, grade):
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    execute_query(connection, query, values)

def get_students(connection):
    query = "SELECT * FROM students"
    return fetch_query(connection, query)

def get_student_by_id(connection, student_id):
    query = "SELECT * FROM students WHERE id = %s"
    values = (student_id,)
    return fetch_query(connection, query, values)

def update_student(connection, student_id, name, age, grade):
    query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
    values = (name, age, grade, student_id)
    execute_query(connection, query, values)

def delete_student(connection, student_id):
    query = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    execute_query(connection, query, values)

class MyMongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["school"]
        self.collection = self.db["students"]

    def create_student(self, name, age, grade):
        student = {"name": name, "age": age, "grade": grade}
        self.collection.insert_one(student)

    def get_students(self):
        return self.collection.find()

    def get_student_by_id(self, student_id):
        return self.collection.find_one({"_id": ObjectId(student_id)})

    def update_student(self, student_id, name, age, grade):
        query = {"_id": ObjectId(student_id)}
        new_values = {"$set": {"name": name, "age": age, "grade": grade}}
        self.collection.update_one(query, new_values)

    def delete_student(self, student_id):
        query = {"_id": ObjectId(student_id)}
        self.collection.delete_one(query)
        

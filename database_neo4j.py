#neo4j
from neo4j import GraphDatabase

class MyNeo4jDB:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4j@123"))
        self.session = self.driver.session()
        print("Connection to Neo4j successful")

    def create_student(self, name, age, grade):
        query = "CREATE (s:Student {name: $name, age: $age, grade: $grade})"
        self.session.run(query, name=name, age=age, grade=grade)

    def get_students(self):
        query = "MATCH (s:Student) RETURN s"
        result = self.session.run(query)
        students = []
        for record in result:
            student = record["s"]
            students.append(student)
        return students

    def get_student_by_id(self, student_id):
        query = "MATCH (s:Student) WHERE ID(s) = $student_id RETURN s"
        result = self.session.run(query, student_id=student_id)
        
        record = result.single()
        print("Record: ", record)
        if record:
            student = record["s"]
            return student
        else:
            return None

    def update_student(self, student_id, name, age, grade):
        query = "MATCH (s:Student) WHERE ID(s) = $student_id SET s.name = $name, s.age = $age, s.grade = $grade"
        self.session.run(query, student_id=student_id, name=name, age=age, grade=grade)

    def delete_student(self, student_id):
        query = "MATCH (s:Student) WHERE ID(s) = $student_id DELETE s"
        self.session.run(query, student_id=student_id)

    def serialize(self, data):
        serialized_data = []
        if len(data)==0 or data[0] is None:
            return []
        for student in data:
            serialized_student = {
                "_id": student.id,
                "name": student["name"],
                "age": student["age"],
                "grade": student["grade"]
            }
            serialized_data.append(serialized_student)
        return serialized_data
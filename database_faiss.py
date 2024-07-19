# Facebook AI Similarity Search
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

class MyFAISS:
    #sentence-transformers/all-MiniLM-L6-v2
    def __init__(self,model_name = "sentence-transformers/all-MiniLM-L6-v2"):
        modelPath = "models/"
        self.index = faiss.IndexFlatL2(256)
        print("Configuring FAISS")
        if not os.path.exists(modelPath+model_name):
            self.Vectorizer_model = SentenceTransformer(model_name)
            model.save(modelPath)
        model = SentenceTransformer(modelPath+model_name)
        print("Transformer Configured Successfully")

    def add_student(self, student_vector):
        self.index.add(student_vector)
        print("Student added successfully")

    def search_student(self, student_vector, k):
        print("Searching for similar students")
        return self.index.search(student_vector, k)

    def remove_student(self, student_id):
        print("Removing student from FAISS")
        self.index.remove(student_id)

    def update_student(self, student_vector):
        print("Updating student in FAISS")
        self.index.update(student_vector)
    
    def save_index(self, filename):
        faiss.write_index(self.index, filename)
        
    def load_index(self, filename):
        self.index = faiss.read_index(filename)
    
    def vectorize_student(self, student):
        return self.model.encode(student)
    
'''
print("Before class")
my_faiss = MyFAISS()

# Add student to FAISS

student_vector = my_faiss.vectorize_student("This is a student")
print(student_vector)

my_faiss.add_student(1, student_vector)

# Search for similar students

my_faiss.search_student(student_vector, 5)

# Remove student from FAISS

my_faiss.remove_student(1)

# Update student in FAISS

my_faiss.update_student(1, student_vector)

# Save and load index

my_faiss.save_index("index.faiss")

my_faiss.load_index("index.faiss")

'''
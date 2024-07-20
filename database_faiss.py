# Facebook AI Similarity Search
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

class MyFAISS:
    model =''
    #sentence-transformers/all-MiniLM-L6-v2
    def __init__(self,model_name = "all-MiniLM-L6-v2"):
        modelPath = "models2/"
        self.index = faiss.IndexFlatL2(256)
        print("Configuring FAISS")
        if not os.path.exists(modelPath+"all-MiniLM-L6-v2"):
            self.Vectorizer_model = SentenceTransformer(model_name)
            self.Vectorizer_model.save(modelPath)
        self.Vectorizer_model = SentenceTransformer(modelPath+"all-MiniLM-L6-v2")
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
    
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from faiss_crud import FAISSCRUD
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
faiss_crud = FAISSCRUD()

class TextData(BaseModel):
    name: str

@app.get("")
def status():
    return "Alive"

@app.post("/faiss/student/create/")
def create_item(data: TextData):
    embedding = model.encode([data.name])[0]
    item_id = faiss_crud.create(embedding)
    return {"id": item_id, "name": data.name}

@app.get("/faiss/student/read/{item_id}")
def read_item(item_id: int):
    embedding = faiss_crud.read(item_id)
    if embedding is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "text": "Texts are not stored, embedding retrieved.", "embedding": embedding.tolist()}

@app.put("/faiss/student/update/{item_id}")
def update_item(item_id: int, data: TextData):
    embedding = model.encode([data.name])[0]
    success = faiss_crud.update(item_id, embedding)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": data.name, "embedding": embedding.tolist()}

@app.delete("/faiss/student/delete/{item_id}")
def delete_item(item_id: int):
    success = faiss_crud.delete(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item is deleted successfully"}
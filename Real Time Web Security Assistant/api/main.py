from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_text

app = FastAPI()

class Request(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Cyber Guard Running"}

@app.post("/predict")
def predict(request: Request):
    result = predict_text(request.text)
    return result
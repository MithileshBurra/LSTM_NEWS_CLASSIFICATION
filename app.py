from fastapi import FastAPI
from Prediction import Predict
from pydantic import BaseModel

app = FastAPI(title = "News Classification API")

class Request(BaseModel):
    texts : list[str]

@app.post("/predict")
def predict(req : Request):
    return Predict(req.texts)

@app.get("/")
def root():
    return {"Stauts":"API Running"}
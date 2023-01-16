from fastapi import FastAPI
from api.predict import Inference

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predict")
def api_predict():
    model_path = "api/rf.pkl"
    data_path = "data/test.csv"
    predictions = Inference(model_path, data_path).predict()
    return predictions[0]


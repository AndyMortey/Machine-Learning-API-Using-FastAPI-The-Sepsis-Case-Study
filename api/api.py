from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd


app = FastAPI()

class DataFeatures(BaseModel):
    Plasma_Glucose: int
    Blood_Work_Result-1: int
    Blood_Pressure: int
    Blood_Work_Result-2: int
    Blood_Work_Result-3: int
    Body_Mass_Index: float
    Blood_Work_Result-4: float
    Age: int
    Insurance: int


@app.get('/')
def status_check():
    return {"Status": "API is Online..."}


logistic_regression = joblib.load('../Models/logistic_regression_pipeline.pkl')
encoder = joblib.load('../Models/label_encoder.pkl')

@app.post('/logistic_prediction')
def predict_sepsis(data: DataFeatures):

    df = pd.DataFrame([data.model_dump()])

    prediction = logistic_regression.predict(df)

    prediction = int(prediction)

    return {"prediction": prediction}


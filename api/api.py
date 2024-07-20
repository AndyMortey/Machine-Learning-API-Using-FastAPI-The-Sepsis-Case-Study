from fastapi import FastAPI
import joblib


app = FastAPI()


@app.get('/')
def status_check():
    return {"Status": "API is Online..."}


logistic_regression = joblib.load('../Models/logistic_regression_pipeline.pkl')
encoder = joblib.load('../Models/label_encoder.pkl')


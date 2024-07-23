from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class DataFeatures(BaseModel):
    plasma_glucose: int
    blood_work_result_1: int
    blood_pressure: int
    blood_work_result_2: int
    blood_work_result_3: int
    body_mass_index: float
    blood_work_result_4: float
    age: int
    insurance: int

@app.get('/')
def status_check():
    return {"Status": "API is Online..."}

# Load models and encoder
logistic_regression = joblib.load('../Models/logistic_regression_pipeline.pkl')
random_forest = joblib.load('../Models/random_forest_pipeline.pkl')
encoder = joblib.load('../Models/label_encoder.pkl')

@app.post('/predict')
def predict_sepsis(data: DataFeatures):
    # Convert input data to DataFrame
    df = pd.DataFrame([data.model_dump()])

    # Make predictions
    prediction_log = logistic_regression.predict(df)
    prediction_ran = random_forest.predict(df)
    
    # Get prediction probabilities
    prob_log = logistic_regression.predict_proba(df)
    prob_ran = random_forest.predict_proba(df)
    
    # Convert predictions to int
    prediction_log = int(prediction_log)
    prediction_ran = int(prediction_ran)
    
    # Inverse transform predictions
    prediction_log = encoder.inverse_transform([prediction_log])[0]
    prediction_ran = encoder.inverse_transform([prediction_ran])[0]

    return {
        "logistic_regression_prediction": prediction_log,
        "random_forest_prediction": prediction_ran,
        "logistic_regression_probability": prob_log.tolist(),
        "random_forest_probability": prob_ran.tolist()
    }

import streamlit as st
import requests
from pydantic import BaseModel
import pandas as pd

# Define the URL of your FastAPI backend
backend_url = "https://machine-learning-api-using-fastapi.onrender.com"

# Create a class for the data features to ensure consistency with the FastAPI model
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

# Initialize session state for predictions history
if 'predictions' not in st.session_state:
    st.session_state['predictions'] = []

# Function to get prediction from FastAPI backend
def get_prediction(data: DataFeatures):
    response = requests.post(f"{backend_url}/predict", json=data.dict())
    return response.json()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Main", "Predict", "History"])

if page == "Main":
    st.title("Sepsis Prediction App")
    st.write("Use the Navigation Bar to Access the Other Pages.")
    st.image("Frontend/Sepsis Prediction.png", caption="Sepsis Prediction", use_column_width=True)

elif page == "Predict":
    st.title("Sepsis Prediction Page")
    st.write("Enter the Following Features to Predict Sepsis:")

    # Collect input data from the user
    plasma_glucose = st.number_input("Plasma Glucose", min_value=0, max_value=500, step=1)
    blood_work_result_1 = st.number_input("Blood Work Result 1", min_value=0, max_value=500, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=300, step=1)
    blood_work_result_2 = st.number_input("Blood Work Result 2", min_value=0, max_value=500, step=1)
    blood_work_result_3 = st.number_input("Blood Work Result 3", min_value=0, max_value=500, step=1)
    body_mass_index = st.number_input("Body Mass Index", min_value=0.0, max_value=100.0, step=0.1)
    blood_work_result_4 = st.number_input("Blood Work Result 4", min_value=0.0, max_value=100.0, step=0.1)
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    insurance = st.number_input("Insurance", min_value=0, max_value=1, step=1)

    # Create a DataFeatures object with the input data
    data = DataFeatures(
        plasma_glucose=plasma_glucose,
        blood_work_result_1=blood_work_result_1,
        blood_pressure=blood_pressure,
        blood_work_result_2=blood_work_result_2,
        blood_work_result_3=blood_work_result_3,
        body_mass_index=body_mass_index,
        blood_work_result_4=blood_work_result_4,
        age=age,
        insurance=insurance
    )

    # When the user clicks the button, make a request to the FastAPI backend
    if st.button("Predict Sepsis"):
        prediction = get_prediction(data)
        st.write(f"Logistic Regression Prediction: {prediction['logistic_regression_prediction']}")
        st.write(f"Random Forest Prediction: {prediction['random_forest_prediction']}")

        # Display probabilities as percentages
        prob_log = [round(p * 100, 2) for p in prediction['logistic_regression_probability'][0]]
        prob_ran = [round(p * 100, 2) for p in prediction['random_forest_probability'][0]]

        st.write(f"Logistic Regression Prediction Probability: {prob_log[0]}%, {prob_log[1]}%")
        st.write(f"Random Forest Prediction Probability: {prob_ran[0]}%, {prob_ran[1]}%")

        # Add the prediction to the session state history
        st.session_state['predictions'].append({
            "input": data.dict(),
            "logistic_regression_prediction": prediction['logistic_regression_prediction'],
            "random_forest_prediction": prediction['random_forest_prediction'],
            "logistic_regression_probability": f"{prob_log[0]}%, {prob_log[1]}%",
            "random_forest_probability": f"{prob_ran[0]}%, {prob_ran[1]}%"
        })

elif page == "History":
    st.title("Prediction History")
    if st.session_state['predictions']:
        for i, pred in enumerate(st.session_state['predictions']):
            st.write(f"Prediction {i + 1}:")
            st.json(pred)
    else:
        st.write("No predictions made yet.")

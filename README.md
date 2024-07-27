# Machine-Learning-API-Using-FastAPI-The-Sepsis-Case-Study

## Project Description
Sepsis is a life-threatening medical condition that arises when the body's response to infection causes injury to its own tissues and organs. It occurs when chemicals released into the bloodstream to fight an infection trigger inflammatory responses throughout the body. This inflammation can lead to a cascade of changes that damage multiple organ systems, leading them to fail, and can be fatal if not promptly treated.
This project aims to leverage machine learning models and FastAPI to predict sepsis, thereby enabling timely interventions and enhancing clinical decision-making. It utilizes the CRISP-DM methodology, incorporating data analysis, model development, and deployment via Docker containers thus leveraging both the backend API and the frontend client for interaction.

## Project Overview
- **Objective:** Build a robust API to predict sepsis risk based on patient medical data.
- **Methodology:** Follows CRISP-DM, a structured process for data mining projects.
- **Tools:**
    - **FastAPI:** A modern, high-performance Python web framework for building APIs.
    - **Machine Learning Models:** Leverages Logistic Regression and Random Forest classifiers.
    - **Docker:** For containerization and deployment of the API and Frontend (Streamlit).

## Dataset Description
| Column Name | Description                                                |
|-------------|------------------------------------------------------------|
| ID          | Unique number to represent patient ID                      |
| PRG         | Plasma glucose                                             |
| PL          | Blood Work Result-1 (mu U/ml)                              |
| PR          | Blood Pressure (mm Hg)                                     |
| SK          | Blood Work Result-2 (mm)                                   |
| TS          | Blood Work Result-3 (mu U/ml)                              |
| M11         | Body mass index (weight in kg/(height in m)^2)             |
| BD2         | Blood Work Result-4 (mu U/ml)                              |
| Age         | Patients age (years)                                       |
| Insurance   | If a patient holds a valid insurance card                  |
| Sepssis     | Positive: if a patient in ICU will develop sepsis, and Negative: otherwise |


## Repository Structure
├── api/

│   ├── Dockerfile &nbsp;&nbsp;&nbsp;  Dockerfile for building the API image
│   ├── api.py     &nbsp;&nbsp;&nbsp;  Main FastAPI application code
│   ├── models/    &nbsp;&nbsp;&nbsp;  Directory for storing trained models
│   └── requirements.txt &nbsp;&nbsp;&nbsp; Python dependencies for the API
├── Frontend/
│   ├── Dockerfile &nbsp;&nbsp;&nbsp;  Dockerfile for building the frontend image
│   ├── main.py    &nbsp;&nbsp;&nbsp;  Main Streamlit application code
│   └── requirements.txt &nbsp;&nbsp;&nbsp; Python dependencies for the frontend
├── docker-compose.yml &nbsp;&nbsp;&nbsp;   Configuration for Docker Compose
└── README.md          &nbsp;&nbsp;&nbsp;   This file


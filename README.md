![image](https://github.com/user-attachments/assets/10373352-ee0d-41ff-b571-ee0d63bb2e34)


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

│   ├── Dockerfile &nbsp;&nbsp;&nbsp;          Dockerfile for building the API image

│   ├── api.py     &nbsp;&nbsp;&nbsp;          Main FastAPI application code

│   ├── models/    &nbsp;&nbsp;&nbsp;          Directory for storing trained models

│   └── requirements.txt &nbsp;&nbsp;&nbsp;    Python dependencies for the API

├── Frontend/

│   ├── Dockerfile &nbsp;&nbsp;&nbsp;          Dockerfile for building the frontend image

│   ├── main.py    &nbsp;&nbsp;&nbsp;          Main Streamlit application code

│   └── requirements.txt &nbsp;&nbsp;&nbsp;    Python dependencies for the frontend

├── docker-compose.yml &nbsp;&nbsp;&nbsp;      Configuration for Docker Compose

└── README.md          &nbsp;&nbsp;&nbsp;      This file


## Usage
### API Backend
The FastAPI application provides several endpoints to interact with the sepsis prediction model. Here are some images of the App:
* This is the Homepage showing the Datafeatures;
![image](https://github.com/user-attachments/assets/66aa2f11-46f8-41b4-8d04-4a2f30a7d8d7)

* This shows the Predict Page which takes the inputs and shows the predictions;
![image](https://github.com/user-attachments/assets/ed9a49b5-298d-49ba-924b-98424186e52f)
![image](https://github.com/user-attachments/assets/7e91df18-1917-4a0e-8970-1dbce745630a)

### Frontend
The frontend is built using Streamlit and provides a user-friendly interface to interact with the API. Here are some images of the App:
* This is the Homepage with the Side panel.
![image](https://github.com/user-attachments/assets/9ede6723-67d4-4938-8738-ca2de3bb54ac)

* This shows the Predict Page with Values and the Prediction.
![image](https://github.com/user-attachments/assets/9b2454fd-1f72-4660-991d-b207183bbe9a)
![image](https://github.com/user-attachments/assets/5168d68a-bc43-46d6-85de-7ed79077d467)

* This is the History Page that shows Predictions made by the App.
![image](https://github.com/user-attachments/assets/13ebd304-ab8a-4e56-8e2d-53b43223c88a)
### Docker
* This shows the Docker container and Images on Docker Desktop
![image](https://github.com/user-attachments/assets/ab4aa317-c36e-41ba-9537-4dff1bd2e531)
![image](https://github.com/user-attachments/assets/cac68c33-0256-45aa-9523-84ef33c0df6c)

## Resources
**Access the API:** Open your browser and navigate to [this link](https://machine-learning-api-using-fastapi.onrender.com/docs)

**Access the Streamlit App:** Open your browser and navigate to [this link](https://machine-learning-api-using-fastapi-the.onrender.com/)

**Article** published on Medium can be accessed via [this link]().

## Appreciation

I highly recommend Azubi Africa for their comprehensive and effective programs. Read more articles about [Azubi Africa here](https://medium.com/@azubiafrica) and take a few minutes to visit this link to learn more about Azubi Africa life-changing [programs](https://bit.ly/41CGCwK).

## Tags

[Azubi Data Science](https://bit.ly/3ARq742)












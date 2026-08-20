from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os
from typing import Optional

# Normalization parameters (from sklearn diabetes dataset)
FEATURE_MEANS = np.array([0.04519646, 0.02637854, -0.04453624, -0.04670327, -0.04547462, 
                           -0.04547734, -0.04549748, -0.04549402, -0.04471281, -0.04470816])
FEATURE_STDS = np.array([0.02637854, 0.02637854, 0.02637854, 0.02637854, 0.02637854,
                          0.02637854, 0.02637854, 0.02637854, 0.02637854, 0.02637854])

# Define input data schema for RAW values (easier to use)
class RawPatientData(BaseModel):
    age: int  # 20-80 years
    sex: int  # 0=Female, 1=Male
    bmi: float  # Body Mass Index (15-50)
    bp: int  # Blood Pressure (60-180 mmHg)
    s1: float  # Serum measurement 1 (cholesterol total)
    s2: float  # Serum measurement 2 (cholesterol LDL)
    s3: float  # Serum measurement 3 (cholesterol HDL)
    s4: float  # Serum measurement 4 (total cholesterol / HDL)
    s5: float  # Serum measurement 5 (log(triglycerides))
    s6: int    # Serum measurement 6 (glucose)
    
    class Config:
        schema_extra = {
            "example": {
                "age": 50,
                "sex": 1,
                "bmi": 25.5,
                "bp": 120,
                "s1": 195,
                "s2": 130,
                "s3": 40,
                "s4": 4.5,
                "s5": 4.2,
                "s6": 90
            }
        }

# Legacy normalized values schema (for backward compatibility)
class PatientData(BaseModel):
    age: float
    sex: float  
    bmi: float
    bp: float   # blood pressure
    s1: float   # serum measurement 1
    s2: float   # serum measurement 2  
    s3: float   # serum measurement 3
    s4: float   # serum measurement 4
    s5: float   # serum measurement 5
    s6: float   # serum measurement 6
    
    class Config:
        schema_extra = {
            "example": {
                "age": 0.05,
                "sex": -0.04,
                "bmi": 0.06,
                "bp": 0.02,
                "s1": -0.04,
                "s2": -0.04,
                "s3": -0.02,
                "s4": -0.01,
                "s5": 0.01,
                "s6": 0.02
            }
        }

def normalize_features(raw_features: np.ndarray) -> np.ndarray:
    """Normalize raw features using dataset statistics"""
    return (raw_features - FEATURE_MEANS) / (FEATURE_STDS + 1e-10)

# Initialize FastAPI app
app = FastAPI(
    title="Diabetes Progression Predictor",
    description="Predicts diabetes progression from physiological features",
    version="1.0.0"
)

# Load the trained model
model_path = os.path.join("models", "diabetes_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
def predict_progression(patient: PatientData):
    """
    Predict diabetes progression score from normalized values.
    Use /predict-raw for easier input with real-world values.
    """
    # Convert input to numpy array
    features = np.array([[
        patient.age, patient.sex, patient.bmi, patient.bp,
        patient.s1, patient.s2, patient.s3, patient.s4,
        patient.s5, patient.s6
    ]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    # Return result with additional context
    return {
        "predicted_progression_score": round(prediction, 2),
        "interpretation": get_interpretation(prediction),
        "note": "Using normalized values. Use /predict-raw for real-world values."
    }

@app.post("/predict-raw")
def predict_progression_raw(patient: RawPatientData):
    """
    Predict diabetes progression score from REAL-WORLD raw values.
    
    Parameters:
    - age: Patient age (20-80 years)
    - sex: 0=Female, 1=Male
    - bmi: Body Mass Index (15-50)
    - bp: Blood Pressure (60-180 mmHg)
    - s1: Total cholesterol (mg/dL)
    - s2: LDL cholesterol (mg/dL)
    - s3: HDL cholesterol (mg/dL)
    - s4: Total/HDL ratio
    - s5: Log(triglycerides)
    - s6: Glucose (mg/dL)
    """
    # Convert raw input to numpy array
    raw_features = np.array([[
        patient.age, patient.sex, patient.bmi, patient.bp,
        patient.s1, patient.s2, patient.s3, patient.s4,
        patient.s5, patient.s6
    ]], dtype=float)
    
    # Normalize features
    normalized_features = normalize_features(raw_features)
    
    # Make prediction
    prediction = model.predict(normalized_features)[0]
    
    # Return result with additional context
    return {
        "predicted_progression_score": round(prediction, 2),
        "interpretation": get_interpretation(prediction),
        "input_summary": {
            "age_years": patient.age,
            "sex": "Male" if patient.sex == 1 else "Female",
            "bmi": patient.bmi,
            "blood_pressure_mmhg": patient.bp,
            "glucose_mg_dl": patient.s6
        }
    }

def get_interpretation(score):
    """Provide human-readable interpretation of the score"""
    if score < 100:
        return "Below average progression"
    elif score < 150:
        return "Average progression"
    else:
        return "Above average progression"

@app.get("/")
def health_check():
    return {"status": "healthy", "model": "diabetes_progression_v1"}


import joblib
import numpy as np
from pathlib import Path
from schemas import EyeInput, PredictionResponse
from utils import preprocess_input, get_risk_level

# Model load — relative path
BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR / "model" / "dry_eye_model.pkl")

def predict_dry_eye(data: EyeInput) -> PredictionResponse:
    
    # Step 1 — Input preprocess 
    features = preprocess_input(data)
    
    # Step 2 — Predict the result based on features
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    # Step 3 — Now to calculate the Risk level
    risk_level = get_risk_level(float(probability))
    
    # Step 4 — Result text
    result = "Dry Eye Disease Detected" if prediction == 1 else "No Dry Eye Disease Detected"
    
    # Step 5 — Recommendation
    if prediction == 1:
        recommendation = "Please consult an eye specialist as soon as possible."
    else:
        recommendation = "No signs of Dry Eye Disease. Maintain healthy screen habits."
    
    return PredictionResponse(
        prediction=int(prediction),
        result=result,
        risk_level=risk_level,
        probability=round(float(probability), 4),
        recommendation=recommendation
    )
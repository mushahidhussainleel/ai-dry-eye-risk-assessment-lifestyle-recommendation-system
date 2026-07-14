from pydantic import BaseModel , Field
from typing import Literal

class EyeInput(BaseModel):
    
    # --- Numeric Fields ---
    Age: int = Field(..., ge=1, le=100)
    Sleep_duration: float = Field(..., ge=0, le=24)
    Sleep_quality: int = Field(..., ge=1, le=4)
    Stress_level: int = Field(..., ge=1, le=8)
    Heart_rate: int = Field(..., ge=40, le=200)
    Daily_steps: int = Field(..., ge=0, le=50000)
    Physical_activity: int = Field(..., ge=0, le=300)
    Height: int = Field(..., ge=100, le=250)
    Weight: int = Field(..., ge=30, le=200)
    Average_screen_time: float = Field(..., ge=0, le=24)
    Systolic_BP: int = Field(..., ge=70, le=200)
    Diastolic_BP: int = Field(..., ge=40, le=130)
    # --- Gender ---
    Gender: Literal["M", "F"]
    
    # --- Y/N Fields ---
    Sleep_disorder: Literal["Y", "N"]
    Wake_up_during_night: Literal["Y", "N"]
    Feel_sleepy_during_day: Literal["Y", "N"]
    Caffeine_consumption: Literal["Y", "N"]
    Alcohol_consumption: Literal["Y", "N"]
    Smoking: Literal["Y", "N"]
    Medical_issue: Literal["Y", "N"]
    Ongoing_medication: Literal["Y", "N"]
    Smart_device_before_bed: Literal["Y", "N"]
    Blue_light_filter: Literal["Y", "N"]
    Discomfort_Eye_strain: Literal["Y", "N"]
    Redness_in_eye: Literal["Y", "N"]
    Itchiness_Irritation_in_eye: Literal["Y", "N"]

class PredictionResponse(BaseModel):
    prediction: int
    result: str
    risk_level: str      
    probability: float
    recommendation: str
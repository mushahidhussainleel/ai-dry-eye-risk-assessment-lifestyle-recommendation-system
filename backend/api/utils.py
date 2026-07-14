import pandas as pd

def preprocess_input(data):
    """
    Convert user input into a numeric format for the model.
    """
    def yn(val):
        """
        Return 1 if value is 'Y', otherwise 0.
        """
        return 1 if val == "Y" else 0
    
    gender = 1 if data.Gender == "M" else 0
    
    features = pd.DataFrame([{
        "Gender": gender,
        "Age": data.Age,
        "Sleep duration": data.Sleep_duration,
        "Sleep quality": data.Sleep_quality,
        "Stress level": data.Stress_level,
        "Heart rate": data.Heart_rate,
        "Daily steps": data.Daily_steps,
        "Physical activity": data.Physical_activity,
        "Height": data.Height,
        "Weight": data.Weight,
        "Sleep disorder": yn(data.Sleep_disorder),
        "Wake up during night": yn(data.Wake_up_during_night),
        "Feel sleepy during day": yn(data.Feel_sleepy_during_day),
        "Caffeine consumption": yn(data.Caffeine_consumption),
        "Alcohol consumption": yn(data.Alcohol_consumption),
        "Smoking": yn(data.Smoking),
        "Medical issue": yn(data.Medical_issue),
        "Ongoing medication": yn(data.Ongoing_medication),
        "Smart device before bed": yn(data.Smart_device_before_bed),
        "Average screen time": data.Average_screen_time,
        "Blue-light filter": yn(data.Blue_light_filter),
        "Discomfort Eye-strain": yn(data.Discomfort_Eye_strain),
        "Redness in eye": yn(data.Redness_in_eye),
        "Itchiness/Irritation in eye": yn(data.Itchiness_Irritation_in_eye),
        "Systolic_BP": data.Systolic_BP,
        "Diastolic_BP": data.Diastolic_BP
    }])
    
    return features

def get_risk_level(probability: float) -> str:
    """
    Determine risk level based on the probability.
    """
    if probability >= 0.75:
        return "High"
    elif probability >= 0.50:
        return "Moderate"
    else:
        return "Low"
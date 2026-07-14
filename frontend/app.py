import streamlit as st
import requests
from PIL import Image

# ─── Page Config ───
st.set_page_config(
    page_title="AI Dry Eye Risk Assessment",
    page_icon="👁️",
    layout="wide"
)

# ─── Custom CSS ───
st.markdown("""
    <style>
        .main { background-color: #0f172a; }
        .stButton>button {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
            border: none;
            padding: 12px 40px;
            border-radius: 50px;
            font-size: 1.1em;
            font-weight: 600;
            width: 100%;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
        }
        .result-box {
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-top: 20px;
        }
        .high-risk {
            background: rgba(239, 68, 68, 0.15);
            border: 2px solid #ef4444;
        }
        .moderate-risk {
            background: rgba(245, 158, 11, 0.15);
            border: 2px solid #f59e0b;
        }
        .low-risk {
            background: rgba(16, 185, 129, 0.15);
            border: 2px solid #10b981;
        }
        .section-title {
            font-size: 1.1em;
            font-weight: 600;
            color: #60a5fa;
            margin-bottom: 10px;
            padding-bottom: 5px;
            border-bottom: 1px solid rgba(96,165,250,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# ─── Banner ───
banner = Image.open("../backend/assets/banner.png")
st.image(banner, use_container_width=True)

st.markdown("---")

# ─── Title ───
st.markdown("<h2 style='text-align:center; color:#60a5fa;'>👁️ AI Dry Eye Risk Assessment System</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8;'>Fill in your lifestyle and health details to assess your Dry Eye Disease risk</p>", unsafe_allow_html=True)

st.markdown("---")

# ─── Input Form ───
with st.form("prediction_form"):

    # Group 1 — Personal Info
    st.markdown("<div class='section-title'>👤 Personal Information</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("Gender", ["M", "F"])
    with col2:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
    with col3:
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=165)
    with col4:
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=65)

    st.markdown("<br>", unsafe_allow_html=True)

    # Group 2 — Sleep & Lifestyle
    st.markdown("<div class='section-title'>🌙 Sleep & Lifestyle</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sleep_duration = st.number_input("Sleep Duration (hrs)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
    with col2:
        sleep_quality = st.selectbox("Sleep Quality (1-4)", [1, 2, 3, 4])
    with col3:
        stress_level = st.slider("Stress Level (1-8)", min_value=1, max_value=8, value=3)
    with col4:
        sleep_disorder = st.selectbox("Sleep Disorder", ["N", "Y"])

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        wake_up = st.selectbox("Wake Up During Night", ["N", "Y"])
    with col2:
        feel_sleepy = st.selectbox("Feel Sleepy During Day", ["N", "Y"])
    with col3:
        caffeine = st.selectbox("Caffeine Consumption", ["N", "Y"])
    with col4:
        alcohol = st.selectbox("Alcohol Consumption", ["N", "Y"])

    col1, col2 = st.columns(4)[:2]
    with col1:
        smoking = st.selectbox("Smoking", ["N", "Y"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Group 3 — Eye & Screen
    st.markdown("<div class='section-title'>👁️ Eye & Screen Habits</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        screen_time = st.number_input("Avg Screen Time (hrs)", min_value=0.0, max_value=24.0, value=6.0, step=0.5)
    with col2:
        blue_light = st.selectbox("Blue Light Filter", ["N", "Y"])
    with col3:
        smart_device = st.selectbox("Smart Device Before Bed", ["N", "Y"])
    with col4:
        discomfort = st.selectbox("Discomfort/Eye Strain", ["N", "Y"])

    col1, col2 = st.columns(4)[:2]
    with col1:
        redness = st.selectbox("Redness in Eye", ["N", "Y"])
    with col2:
        itchiness = st.selectbox("Itchiness/Irritation", ["N", "Y"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Group 4 — Health Info
    st.markdown("<div class='section-title'>🏥 Health Information</div>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=72)
    with col2:
        daily_steps = st.number_input("Daily Steps", min_value=0, max_value=50000, value=5000)
    with col3:
        physical_activity = st.number_input("Physical Activity (min)", min_value=0, max_value=300, value=30)
    with col4:
        medical_issue = st.selectbox("Medical Issue", ["N", "Y"])

    col1, col2, col3 = st.columns(3)
    with col1:
        ongoing_med = st.selectbox("Ongoing Medication", ["N", "Y"])
    with col2:
        systolic_bp = st.number_input("Systolic BP", min_value=70, max_value=200, value=120)
    with col3:
        diastolic_bp = st.number_input("Diastolic BP", min_value=40, max_value=130, value=80)

    st.markdown("<br>", unsafe_allow_html=True)

    # Submit Button
    submitted = st.form_submit_button("🔍 Predict Dry Eye Risk")

# ─── Result ───
if submitted:
    payload = {
        "Gender": gender,
        "Age": age,
        "Sleep_duration": sleep_duration,
        "Sleep_quality": sleep_quality,
        "Stress_level": stress_level,
        "Heart_rate": heart_rate,
        "Daily_steps": daily_steps,
        "Physical_activity": physical_activity,
        "Height": height,
        "Weight": weight,
        "Sleep_disorder": sleep_disorder,
        "Wake_up_during_night": wake_up,
        "Feel_sleepy_during_day": feel_sleepy,
        "Caffeine_consumption": caffeine,
        "Alcohol_consumption": alcohol,
        "Smoking": smoking,
        "Medical_issue": medical_issue,
        "Ongoing_medication": ongoing_med,
        "Smart_device_before_bed": smart_device,
        "Average_screen_time": screen_time,
        "Blue_light_filter": blue_light,
        "Discomfort_Eye_strain": discomfort,
        "Redness_in_eye": redness,
        "Itchiness_Irritation_in_eye": itchiness,
        "Systolic_BP": systolic_bp,
        "Diastolic_BP": diastolic_bp
    }

    with st.spinner("Analyzing your data..."):
        try:
            response = requests.post(
                "https://dry-eye-api-naci.onrender.com/predict",
                json=payload
            )
            result = response.json()

            # Risk Level
            risk = result["risk_level"]
            if risk == "High":
                css_class = "high-risk"
                emoji = "🔴"
            elif risk == "Moderate":
                css_class = "moderate-risk"
                emoji = "🟡"
            else:
                css_class = "low-risk"
                emoji = "🟢"

            # Result Display
            st.markdown(f"""
                <div class='result-box {css_class}'>
                    <h2>{emoji} {risk} Risk</h2>
                    <h3>{result['result']}</h3>
                    <p style='color:#94a3b8; font-size:1.1em;'>
                        Probability: <strong>{round(result['probability']*100, 1)}%</strong>
                    </p>
                </div>
            """, unsafe_allow_html=True)

            st.progress(result["probability"])

            st.info(f"💡 {result['recommendation']}")

        except Exception as e:
            st.error(f"API Error: {str(e)}\nMake sure backend is running!")

# ─── Footer ───
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#475569; font-size:0.85em;'>"
    "Built with ❤️ using FastAPI + Streamlit + Scikit-learn | "
    "⚠️ This is not a substitute for professional medical advice"
    "</p>",
    unsafe_allow_html=True
)
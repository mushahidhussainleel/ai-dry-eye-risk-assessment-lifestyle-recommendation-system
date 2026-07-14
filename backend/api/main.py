from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from schemas import EyeInput, PredictionResponse
from predict import predict_dry_eye

app = FastAPI(
    title="AI Dry Eye Risk Assessment & Lifestyle Recommendation System",
    description="Predicts Dry Eye Disease risk based on lifestyle and health data.",
    version="1.0.0"
)


@app.get("/", response_class=HTMLResponse, tags=["Root"])
def home():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dry Eye Risk Assessment API</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 700px;
            width: 100%;
            text-align: center;
        }
        .icon { font-size: 60px; margin-bottom: 15px; }
        h1 {
            font-size: 1.9em;
            font-weight: 700;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #94a3b8;
            font-size: 1em;
            margin-bottom: 30px;
        }
        .status {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(30,41,59,0.8);
            padding: 8px 20px;
            border-radius: 50px;
            border: 1px solid rgba(96,165,250,0.2);
            margin-bottom: 40px;
            font-size: 0.9em;
        }
        .dot {
            width: 8px; height: 8px;
            background: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10b981;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .cards {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 30px;
        }
        .card {
            background: rgba(30,41,59,0.6);
            border: 1px solid rgba(96,165,250,0.15);
            border-radius: 14px;
            padding: 20px;
        }
        .card-icon { font-size: 1.8em; margin-bottom: 8px; }
        .card-title { font-size: 0.95em; font-weight: 600; color: #60a5fa; margin-bottom: 5px; }
        .card-desc { font-size: 0.85em; color: #94a3b8; }
        .endpoint {
            display: flex;
            align-items: center;
            gap: 10px;
            background: rgba(15,23,42,0.6);
            border-radius: 8px;
            padding: 10px 15px;
            margin-bottom: 8px;
            text-align: left;
        }
        .method {
            font-size: 0.75em;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 5px;
            min-width: 55px;
            text-align: center;
        }
        .get { background: #3b82f6; color: white; }
        .post { background: #10b981; color: white; }
        .path {
            font-family: monospace;
            font-size: 0.9em;
            color: #94a3b8;
        }
        .buttons {
            display: flex;
            gap: 12px;
            justify-content: center;
            margin-top: 25px;
        }
        .btn {
            padding: 12px 30px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95em;
            transition: all 0.3s ease;
        }
        .btn-primary {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
        }
        .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(59,130,246,0.4); }
        .btn-secondary {
            background: rgba(30,41,59,0.8);
            color: #60a5fa;
            border: 1px solid rgba(96,165,250,0.3);
        }
        .btn-secondary:hover { transform: translateY(-3px); }
        .footer { margin-top: 30px; color: #475569; font-size: 0.85em; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">👁️</div>
        <h1>AI Dry Eye Risk Assessment</h1>
        <p class="subtitle">Lifestyle-based Dry Eye Disease Prediction System</p>

        <div class="status">
            <div class="dot"></div>
            <span>API Live</span>
            <span style="color:#475569">|</span>
            <span>v1.0.0</span>
            <span style="color:#475569">|</span>
            <span>⚡ FastAPI</span>
        </div>

        <div class="cards">
            <div class="card">
                <div class="card-icon">🤖</div>
                <div class="card-title">ML Model</div>
                <div class="card-desc">Random Forest Classifier trained on lifestyle & health data</div>
            </div>
            <div class="card">
                <div class="card-icon">📊</div>
                <div class="card-title">Risk Assessment</div>
                <div class="card-desc">High / Moderate / Low risk prediction with probability</div>
            </div>
        </div>

        <div class="card" style="margin-bottom: 25px; text-align: left;">
            <div class="card-title" style="margin-bottom: 12px;">🔗 API Endpoints</div>
            <div class="endpoint">
                <span class="method get">GET</span>
                <span class="path">/</span>
            </div>
            <div class="endpoint">
                <span class="method post">POST</span>
                <span class="path">/predict</span>
            </div>
        </div>

        <div class="buttons">
            <a href="/docs" class="btn btn-primary">📖 Swagger UI</a>
            <a href="/redoc" class="btn btn-secondary">📘 ReDoc</a>
        </div>

        <div class="footer">
            <p style="margin-top: 15px;">Built with ❤️ using <strong style="color:#60a5fa">FastAPI</strong> + <strong style="color:#a78bfa">Scikit-learn</strong></p>
        </div>
    </div>
</body>
</html>
"""
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/predict", response_model=PredictionResponse)
def predict(data: EyeInput):
    result = predict_dry_eye(data)
    return result
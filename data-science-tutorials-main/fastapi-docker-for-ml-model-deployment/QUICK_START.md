# Quick Start Commands - FastAPI Diabetes Predictor

## 🚀 One-Command Setup & Run

```bash
# Navigate to project
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment

# Install dependencies
pip install -r requirements.txt

# Train the model
cd diabetes-predictor && python train_model.py

# Start the app
fastapi dev app/main.py
```

---

## 📋 Complete Step-by-Step Commands

### 1️⃣ Install Dependencies

```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment
pip install -r requirements.txt
```

### 2️⃣ Train the ML Model

```bash
cd diabetes-predictor
python train_model.py
```

**Output:**

```
Dataset shape: (442, 10)
Mean Squared Error: 2974.20
R² Score: 0.439
Model trained and saved successful
```

### 3️⃣ Start FastAPI Server

```bash
fastapi dev app/main.py
```

**You should see:**

```
🌐 Server started at http://127.0.0.1:8000
   Documentation at http://127.0.0.1:8000/docs
```

---

## 🧪 Test the API

### Health Check

```bash
curl http://127.0.0.1:8000/
```

**Response:** `{"status":"healthy","model":"diabetes_progression_v1"}`

### Make a Prediction (⭐ RECOMMENDED - Use Real-World Medical Values)

```bash
curl -X POST http://127.0.0.1:8000/predict-raw \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

**Response:**

```json
{
  "predicted_progression_score": 249.82,
  "interpretation": "Above average progression",
  "input_summary": {
    "age_years": 50,
    "sex": "Male",
    "bmi": 25.5,
    "blood_pressure_mmhg": 120,
    "glucose_mg_dl": 90
  }
}
```

**Input Field Descriptions:**
- `age`: Patient age in years (20-80)
- `sex`: 0=Female, 1=Male
- `bmi`: Body Mass Index (15-50)
- `bp`: Blood Pressure in mmHg (60-180)
- `s1`: Total Cholesterol in mg/dL (100-300)
- `s2`: LDL Cholesterol in mg/dL (50-200)
- `s3`: HDL Cholesterol in mg/dL (20-80)
- `s4`: Cholesterol Ratio - Total/HDL (1.5-8.0)
- `s5`: Log(Triglycerides) (3.0-5.0)
- `s6`: Glucose in mg/dL (70-200)

---

## 📚 Interactive API Documentation

Open in browser:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **Examples:** See [API_EXAMPLES.md](API_EXAMPLES.md) for more sample inputs

---

## 📁 Directory Structure

```
fastapi-docker-for-ml-model-deployment/
├── diabetes-predictor/
│   ├── app/
│   │   ├── main.py          ← FastAPI app
│   │   └── __init__.py
│   ├── train_model.py       ← Model training
│   └── models/
│       └── diabetes_model.pkl  ← Generated model
├── requirements.txt
└── SETUP_INSTRUCTIONS.md
```

---

## 🔧 Common Commands

| Task                  | Command                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------- |
| Install packages      | `pip install -r requirements.txt`                                                         |
| Train model           | `python diabetes-predictor/train_model.py`                                                |
| Run app               | `fastapi dev diabetes-predictor/app/main.py`                                              |
| Run with uvicorn      | `uvicorn app.main:app --reload` (from diabetes-predictor/)                                |
| Run on different port | `fastapi dev app/main.py --port 8001`                                                     |
| Test health           | `curl http://127.0.0.1:8000/`                                                             |
| Test prediction       | `curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d {...}` |

---

## ⚠️ Troubleshooting

| Issue                                 | Solution                                       |
| ------------------------------------- | ---------------------------------------------- |
| `ModuleNotFoundError`                 | Run `pip install -r requirements.txt`          |
| `models/diabetes_model.pkl not found` | Run `python diabetes-predictor/train_model.py` |
| Port 8000 in use                      | Use `fastapi dev app/main.py --port 8001`      |
| Permission denied                     | Use `chmod +x train_model.py` if needed        |

---

## 📊 Model Information

- **Algorithm:** Random Forest Regressor (100 trees)
- **Training Samples:** 353
- **Test Samples:** 89
- **Accuracy (R² Score):** 0.439
- **Input Features:** 10 normalized physiological measurements
- **Output:** Diabetes progression score (25-346 range)

---

## 💡 Next Steps

1. Visit http://127.0.0.1:8000/docs to explore interactive API docs
2. Try different prediction values in the Swagger UI
3. Modify model hyperparameters in `train_model.py`
4. Create a client app to consume the API
5. Deploy using Docker (Dockerfile available)

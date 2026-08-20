# FastAPI Diabetes Predictor - Setup & Usage Guide

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Step-by-Step Setup Instructions

### 1. Navigate to Project Directory

```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Machine Learning Model

```bash
cd diabetes-predictor
python train_model.py
```

**Expected Output:**

```
Dataset shape: (442, 10)
Features: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
Target range: 25.0 to 346.0
Training samples: 353
Test samples: 89
Mean Squared Error: [value]
R² Score: [value]
Model trained and saved successful
```

This creates a `models/diabetes_model.pkl` file.

### 5. Start the FastAPI Application

```bash
fastapi dev app/main.py
```

Or using uvicorn directly:

```bash
uvicorn app.main:app --reload
```

**Expected Output:**

```
INFO:     Application startup complete
Uvicorn running on http://127.0.0.1:8000
```

### 6. Access the Application

#### API Documentation

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

#### Health Check Endpoint

```bash
curl http://127.0.0.1:8000/
```

#### Make a Prediction

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 0.05,
    "sex": 0.05,
    "bmi": 0.06,
    "bp": 0.02,
    "s1": -0.04,
    "s2": -0.04,
    "s3": -0.02,
    "s4": -0.01,
    "s5": 0.01,
    "s6": 0.02
  }'
```

## Project Structure

```
fastapi-docker-for-ml-model-deployment/
├── diabetes-predictor/
│   ├── app/
│   │   ├── main.py           # FastAPI application
│   │   └── __init__.py
│   ├── train_model.py         # Model training script
│   └── models/                # Generated after training
│       └── diabetes_model.pkl
└── requirements.txt
```

## Model Details

- **Algorithm:** Random Forest Regressor
- **Input:** 10 physiological features
- **Output:** Diabetes progression score (25-346 range)
- **Dataset:** scikit-learn's diabetes dataset (442 samples)
- **Train/Test Split:** 80/20

## Features (Input Data)

1. **age** - Age of patient (normalized)
2. **sex** - Sex of patient (normalized)
3. **bmi** - Body Mass Index (normalized)
4. **bp** - Blood pressure (normalized)
5. **s1-s6** - Six serum measurements (normalized)

## Troubleshooting

**Error: "models/diabetes_model.pkl not found"**

- Run `python train_model.py` first to generate the model

**Error: "ModuleNotFoundError"**

- Install dependencies: `pip install -r requirements.txt`

**Port 8000 already in use**

- Use a different port: `fastapi dev app/main.py --port 8001`

## Next Steps

- Explore the Swagger UI at http://127.0.0.1:8000/docs
- Test different prediction inputs
- Modify model parameters in `train_model.py`
- Deploy using Docker (see Dockerfile if available)

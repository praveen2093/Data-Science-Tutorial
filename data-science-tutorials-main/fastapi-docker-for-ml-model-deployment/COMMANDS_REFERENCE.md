# 🎯 Commands to Build Model & Use the App

## 📋 Complete Step-by-Step Commands

### Step 1: Navigate to Project Directory
```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
**What it installs:**
- fastapi - Web framework
- uvicorn - ASGI server
- scikit-learn - Machine learning
- numpy - Numerical computing
- pydantic - Data validation

### Step 3: Train the Machine Learning Model
```bash
cd diabetes-predictor
python train_model.py
```

**Expected output:**
```
Dataset shape: (442, 10)
Features: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
Target range: 25.0 to 346.0
Training samples: 353
Test samples: 89
Mean Squared Error: 2974.20
R² Score: 0.439
Model trained and saved successful
```

**Creates:** `models/diabetes_model.pkl` (trained model file)

### Step 4: Start the FastAPI Server
```bash
fastapi dev app/main.py
```

**Expected output:**
```
⚡️ Starting FastAPI in development mode
🐍 Using import string: app.main:app
🌐 Server started at http://127.0.0.1:8000
   Documentation at http://127.0.0.1:8000/docs
```

---

## 🧪 Testing Commands

Once the server is running (in a new terminal):

### Test 1: Health Check
```bash
curl http://127.0.0.1:8000/
```
**Expected:** `{"status":"healthy","model":"diabetes_progression_v1"}`

### Test 2: Make a Prediction (With Real-World Values)
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

**Expected Response:**
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

### Test 3: Try Different Patient Profile
```bash
curl -X POST http://127.0.0.1:8000/predict-raw \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "sex": 0,
    "bmi": 22,
    "bp": 110,
    "s1": 180,
    "s2": 110,
    "s3": 50,
    "s4": 3.6,
    "s5": 3.8,
    "s6": 85
  }'
```

### Test 4: Use Interactive Swagger UI
Open in your browser:
```
http://127.0.0.1:8000/docs
```

Then:
1. Click on "POST /predict-raw"
2. Click "Try it out"
3. Edit the example values
4. Click "Execute"
5. See the response below

---

## 🚀 All-In-One Command (One Time Setup)

Run this to do everything at once:

```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment && \
pip install -r requirements.txt -q && \
cd diabetes-predictor && \
python train_model.py && \
echo "" && \
echo "✅ Model trained! Starting server..." && \
echo "📊 Access API at: http://127.0.0.1:8000/docs" && \
echo "" && \
fastapi dev app/main.py
```

---

## 📌 Commands for Next Time

### If model already trained, just run server:
```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment/diabetes-predictor
fastapi dev app/main.py
```

### If dependencies already installed:
```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment/diabetes-predictor
python train_model.py
fastapi dev app/main.py
```

### To retrain model (if you modify train_model.py):
```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment/diabetes-predictor
python train_model.py
```

---

## 🎮 Alternative: Using uvicorn directly

Instead of `fastapi dev`, you can use:
```bash
cd /workspaces/Data-Science-Tutorial/data-science-tutorials-main/fastapi-docker-for-ml-model-deployment/diabetes-predictor
uvicorn app.main:app --reload
```

---

## 📊 Input Values Reference

When making predictions, use these ranges for realistic values:

```json
{
  "age": 50,              // 20-80 years
  "sex": 1,              // 0=Female, 1=Male
  "bmi": 25.5,           // 15-50 (Body Mass Index)
  "bp": 120,             // 60-180 mmHg (Blood Pressure)
  "s1": 195,             // 100-300 mg/dL (Total Cholesterol)
  "s2": 130,             // 50-200 mg/dL (LDL Cholesterol)
  "s3": 40,              // 20-80 mg/dL (HDL Cholesterol)
  "s4": 4.5,             // 1.5-8.0 (Cholesterol Ratio)
  "s5": 4.2,             // 3.0-5.0 (Log Triglycerides)
  "s6": 90               // 70-200 mg/dL (Glucose)
}
```

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `requirements.txt` | List of dependencies |
| `diabetes-predictor/train_model.py` | Script to train the model |
| `diabetes-predictor/app/main.py` | FastAPI application |
| `diabetes-predictor/models/diabetes_model.pkl` | Trained model (created after running train_model.py) |

---

## ✅ Checklist for Running the App

- [ ] Navigate to project directory
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Train model: `python diabetes-predictor/train_model.py`
- [ ] Start server: `fastapi dev diabetes-predictor/app/main.py`
- [ ] Open browser: http://127.0.0.1:8000/docs
- [ ] Test an endpoint
- [ ] Make predictions!

---

## 🆘 If Something Goes Wrong

**Error: "Model not found"**
```bash
cd diabetes-predictor
python train_model.py
```

**Error: "Port already in use"**
```bash
fastapi dev app/main.py --port 8001
```

**Error: "Module not found"**
```bash
pip install -r requirements.txt
```

**Server crashed?**
- Check the error message in terminal
- Make sure you're in the right directory
- Try restarting the server

---

## 🎓 Understanding the Model

The model:
1. Takes 10 physiological features as input
2. Was trained on 353 real patient samples
3. Predicts diabetes progression score (25-346 range)
4. Uses Random Forest algorithm
5. Achieves 43.9% R² score on test data

---

## 📞 Quick Reference Card

| Task | Command |
|------|---------|
| Install deps | `pip install -r requirements.txt` |
| Train model | `python diabetes-predictor/train_model.py` |
| Run app | `fastapi dev diabetes-predictor/app/main.py` |
| Health check | `curl http://127.0.0.1:8000/` |
| Make prediction | `curl -X POST http://127.0.0.1:8000/predict-raw ...` |
| API docs | Open http://127.0.0.1:8000/docs |
| Stop server | Press CTRL+C |

---

## 🎉 You're All Set!

The application is ready to use. Follow the steps above and you'll have:
- ✅ A trained ML model
- ✅ A running FastAPI server
- ✅ Interactive API documentation
- ✅ Full prediction capabilities

Happy predicting! 🚀

# 📊 API Usage Guide - Real-World Values

## The Two Endpoints

### 1️⃣ `/predict-raw` ⭐ **RECOMMENDED** - Uses Real-World Medical Values

**Easy to use!** Just provide actual patient measurements.

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

### 2️⃣ `/predict` - Uses Normalized/Standardized Values

For advanced users who have already normalized their data.

---

## 📋 Field Reference

### Input Parameters for `/predict-raw`:

| Field | Name | Type | Range | Description |
|-------|------|------|-------|-------------|
| `age` | Patient Age | int | 20-80 | Age in years |
| `sex` | Gender | int | 0 or 1 | 0=Female, 1=Male |
| `bmi` | Body Mass Index | float | 15-50 | Weight (kg) / Height² (m²) |
| `bp` | Blood Pressure | int | 60-180 | Systolic blood pressure in mmHg |
| `s1` | Total Cholesterol | float | 100-300 | mg/dL |
| `s2` | LDL Cholesterol | float | 50-200 | mg/dL (bad cholesterol) |
| `s3` | HDL Cholesterol | float | 20-80 | mg/dL (good cholesterol) |
| `s4` | Cholesterol Ratio | float | 1.5-8.0 | Total Cholesterol / HDL |
| `s5` | Log(Triglycerides) | float | 3.0-5.0 | Natural logarithm of triglycerides |
| `s6` | Glucose | int | 70-200 | mg/dL (fasting or random) |

---

## 💡 Example Scenarios

### Example 1: Middle-aged Male (Moderately High Risk)
```json
{
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
```
**Expected:** Above average progression (~250 score)

### Example 2: Young Female (Healthy)
```json
{
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
}
```
**Expected:** Average progression

### Example 3: Older Male (Higher Risk)
```json
{
  "age": 65,
  "sex": 1,
  "bmi": 28.5,
  "bp": 135,
  "s1": 220,
  "s2": 150,
  "s3": 35,
  "s4": 6.2,
  "s5": 4.5,
  "s6": 125
}
```
**Expected:** Above average progression

### Example 4: Young Female (Overweight)
```json
{
  "age": 28,
  "sex": 0,
  "bmi": 28,
  "bp": 115,
  "s1": 200,
  "s2": 135,
  "s3": 42,
  "s4": 4.8,
  "s5": 4.1,
  "s6": 95
}
```
**Expected:** Average to high progression

### Example 5: Older Female (Normal)
```json
{
  "age": 58,
  "sex": 0,
  "bmi": 24,
  "bp": 118,
  "s1": 185,
  "s2": 115,
  "s3": 48,
  "s4": 3.85,
  "s5": 3.9,
  "s6": 88
}
```
**Expected:** Average progression

---

## 🧮 How to Calculate Values

### BMI (Body Mass Index)
```
BMI = Weight (kg) / Height² (m²)

Example:
- 70 kg, 1.75m tall
- BMI = 70 / (1.75 × 1.75) = 22.86
```

### Blood Pressure
```
Take the systolic (upper) reading
Example: 120/80 → use 120
```

### Cholesterol Ratio (s4)
```
s4 = Total Cholesterol (s1) / HDL (s3)

Example:
- Total: 195 mg/dL
- HDL: 40 mg/dL  
- Ratio: 195 / 40 = 4.875
```

### Log(Triglycerides) (s5)
```
s5 = ln(Triglycerides in mg/dL)

Example:
- Triglycerides: 60 mg/dL
- s5 = ln(60) ≈ 4.09

Common triglyceride levels:
- <100 mg/dL: s5 ≈ 3.0-4.6
- 100-150 mg/dL: s5 ≈ 4.6-5.0
- 150-200 mg/dL: s5 ≈ 5.0-5.3
```

---

## 📈 Understanding the Output

### Progression Score
- **Score < 100**: Below average progression (slower progression)
- **Score 100-150**: Average progression
- **Score > 150**: Above average progression (faster progression)

### Example Response
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

---

## 🖥️ Testing in Interactive UI

Visit **http://127.0.0.1:8000/docs** for the Swagger UI where you can:
1. Try different input values
2. See real-time validation
3. Get instant predictions
4. Copy example JSON

---

## ⚠️ Important Notes

- All medical values should be realistic/within normal ranges
- Model predictions are based on patterns in training data
- This is a demonstration model, not for clinical decision-making
- Always consult with healthcare professionals for medical advice

---

## 🔗 Related Commands

```bash
# Test with curl
curl -X POST http://127.0.0.1:8000/predict-raw \
  -H "Content-Type: application/json" \
  -d @patient_data.json

# Health check
curl http://127.0.0.1:8000/

# View API docs
open http://127.0.0.1:8000/docs
```

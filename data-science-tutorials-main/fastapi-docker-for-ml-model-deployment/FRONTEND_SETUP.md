# 🎨 Frontend Setup & Usage Guide

## What's New?

Your FastAPI Diabetes Predictor now includes a **beautiful, modern web interface**!

## Features

- ✨ Modern, responsive UI with gradient design
- 📱 Mobile-friendly (works on all devices)
- ⚡ Real-time predictions with visual feedback
- 📊 Interactive health metrics form
- 🎯 Clear interpretation of results
- 🛡️ CORS-enabled for cross-origin requests

## Quick Start

### 1. Ensure Frontend Files are in Place

The frontend is located at:

```
diabetes-predictor/static/index.html
```

### 2. Run the Server

**Linux/Mac:**

```bash
cd fastapi-docker-for-ml-model-deployment
chmod +x run.sh
./run.sh
```

**Windows:**

```bash
cd fastapi-docker-for-ml-model-deployment
run.bat
```

**Manual:**

```bash
cd diabetes-predictor
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Open in Browser

```
http://localhost:8000/
```

## Using the Frontend

### Input Form Fields

| Field                   | Range  | Unit             | Example |
| ----------------------- | ------ | ---------------- | ------- |
| Age                     | 20-80  | years            | 50      |
| Sex                     | 0-1    | 0=Female, 1=Male | 1       |
| BMI                     | 15-50  | -                | 25.5    |
| Blood Pressure          | 60-180 | mmHg             | 120     |
| Total Cholesterol (s1)  | -      | mg/dL            | 195     |
| LDL Cholesterol (s2)    | -      | mg/dL            | 130     |
| HDL Cholesterol (s3)    | -      | mg/dL            | 40      |
| Total/HDL Ratio (s4)    | -      | ratio            | 4.5     |
| Log(Triglycerides) (s5) | -      | log scale        | 4.2     |
| Glucose (s6)            | -      | mg/dL            | 90      |

### How to Use

1. **Enter Patient Data**: Fill in the health metrics form
2. **Submit**: Click "Predict Progression" button
3. **View Results**: See the prediction score and interpretation
4. **Reset**: Click "Clear Form" to start over

## API Endpoints

### Frontend

- `GET /` → Serves the HTML interface

### Health Check

- `GET /health` → Returns `{"status": "healthy", "model": "diabetes_progression_v1"}`

### Make Predictions

- `POST /api/predict-raw` → Predict using real-world values (recommended)
- `POST /api/predict` → Predict using normalized values

## Example API Call

```bash
curl -X POST http://localhost:8000/api/predict-raw \
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

## Response Format

```json
{
  "predicted_progression_score": 125.5,
  "interpretation": "Average progression",
  "input_summary": {
    "age_years": 50,
    "sex": "Male",
    "bmi": 25.5,
    "blood_pressure_mmhg": 120,
    "glucose_mg_dl": 90
  }
}
```

## Understanding Results

### Prediction Score Scale

- **< 100**: Below average progression
- **100-149**: Average progression
- **≥ 150**: Above average progression

The score predicts the patient's diabetes progression level based on health metrics.

## Useful Links

While Server Running:

- **Frontend**: http://localhost:8000/
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Customizing the Frontend

The frontend is a single HTML file with embedded CSS and JavaScript:

```
diabetes-predictor/static/index.html
```

### Modify Colors

Find this section in index.html:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Change the hex colors to customize the theme.

### Modify Text

All text is in the HTML. Search and replace to update labels, titles, etc.

### Add Features

Add new input fields by following the pattern in the form section.

## Troubleshooting

### "Frontend not found" Message

**Solution**: Ensure the static directory and index.html file exist:

```bash
mkdir -p diabetes-predictor/static
# Ensure index.html is in that directory
```

### Port 8000 Already in Use

**Solution**: Use a different port:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

Then access: http://localhost:8001/

### "Cannot POST /api/predict-raw" Error

**Solution**:

1. Check the server is running
2. Check browser console (F12) for CORS errors
3. Verify the API endpoint URL in the JavaScript

### Slow Predictions

- The ML model is loading the first time - subsequent predictions will be faster
- Check system resources (CPU, RAM)
- Verify the model file is not corrupted

## Browser Compatibility

| Browser              | Status          |
| -------------------- | --------------- |
| Chrome/Edge          | ✅ Full Support |
| Firefox              | ✅ Full Support |
| Safari               | ✅ Full Support |
| Mobile Safari/Chrome | ✅ Responsive   |

## Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t diabetes-predictor .

# Run container
docker run -p 8000:8000 diabetes-predictor
```

Then access: http://localhost:8000/

## Security Notes

⚠️ **Current Setup**:

- CORS is set to allow all origins (`allow_origins=["*"]`)
- This is fine for development/demo

🔒 **For Production**:

- Restrict CORS to specific domains
- Add authentication (JWT, OAuth)
- Use HTTPS
- Add rate limiting
- Validate all inputs strictly

## Performance Tips

1. **Server**: Use `uvicorn app.main:app` (without --reload) for production
2. **Frontend**: All CSS/JS is inline - loads quickly
3. **Model**: First prediction is slower (model initialization), then cached
4. **Browser**: Clear cache if frontend doesn't update

## Advanced Usage

### Use Frontend with External API

Modify the fetch URL in `index.html`:

```javascript
const response = await fetch('https://your-api.com/api/predict-raw', {
```

### Export Frontend as Standalone HTML

The index.html file is completely self-contained:

- No external CSS files
- No external JavaScript files
- No dependencies (pure HTML/CSS/JS)

You can save it anywhere and open it directly in a browser!

### Integrate with Other Applications

Use the API endpoints from any application:

**Python:**

```python
import requests
response = requests.post('http://localhost:8000/api/predict-raw', json={...})
print(response.json())
```

**JavaScript:**

```javascript
fetch('http://localhost:8000/api/predict-raw', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({...})
}).then(r => r.json()).then(console.log)
```

**cURL:**

```bash
curl -X POST http://localhost:8000/api/predict-raw -H "Content-Type: application/json" -d '{...}'
```

---

**Enjoy your diabetes prediction app! 🏥✨**

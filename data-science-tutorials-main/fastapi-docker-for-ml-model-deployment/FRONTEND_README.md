# Diabetes Predictor Frontend Setup

## Overview

This frontend provides a user-friendly interface for the Diabetes Progression Predictor API built with FastAPI.

## Features

- 📊 Clean, modern UI with gradient design
- 📱 Responsive design (works on desktop and mobile)
- ✅ Form validation with helpful hints
- 🔄 Real-time prediction results
- 📈 Visual interpretation of prediction scores
- ⚡ Fast API integration with CORS support

## File Structure

```
diabetes-predictor/
├── app/
│   ├── main.py          # Updated FastAPI app with frontend serving
│   └── __init__.py
├── models/
│   └── diabetes_model.pkl
├── static/
│   └── index.html       # Frontend HTML (this file handles everything)
├── train_model.py
└── requirements.txt
```

## Setup Instructions

### 1. Ensure Frontend Files are in Place

The frontend files should be in the `static/` directory:

```
diabetes-predictor/static/index.html
```

### 2. Install Dependencies

Make sure you have FastAPI and required dependencies installed:

```bash
pip install fastapi uvicorn python-multipart pydantic scikit-learn
```

### 3. Run the Server

Navigate to the diabetes-predictor directory and run:

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Or if you're using the run_model.py script:

```bash
python app/main.py
```

### 4. Access the Application

Open your browser and navigate to:

```
http://localhost:8000/
```

## API Endpoints

### Frontend

- `GET /` - Serves the main HTML interface

### Health Check

- `GET /health` - Returns API health status

### Prediction Endpoints

- `POST /api/predict` - Predict using normalized values
- `POST /api/predict-raw` - Predict using real-world values (recommended)

## Input Parameters (for /api/predict-raw)

| Parameter | Type  | Range  | Description               |
| --------- | ----- | ------ | ------------------------- |
| age       | int   | 20-80  | Patient age in years      |
| sex       | int   | 0-1    | 0=Female, 1=Male          |
| bmi       | float | 15-50  | Body Mass Index           |
| bp        | int   | 60-180 | Blood Pressure in mmHg    |
| s1        | float | -      | Total Cholesterol (mg/dL) |
| s2        | float | -      | LDL Cholesterol (mg/dL)   |
| s3        | float | -      | HDL Cholesterol (mg/dL)   |
| s4        | float | -      | Total/HDL Ratio           |
| s5        | float | -      | Log(Triglycerides)        |
| s6        | int   | -      | Glucose (mg/dL)           |

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

## Interpretation Levels

- **Below average progression**: Score < 100
- **Average progression**: 100 ≤ Score < 150
- **Above average progression**: Score ≥ 150

## Docker Deployment

If you want to containerize this application:

```bash
# Build the Docker image
docker build -t diabetes-predictor .

# Run the container
docker run -p 8000:8000 diabetes-predictor
```

## Troubleshooting

### Frontend not loading

- Check that the `static/index.html` file exists
- Ensure the FastAPI app is running on the correct port
- Check browser console for errors (F12)

### CORS errors

- The application includes CORS middleware, should allow all origins
- Check that the API endpoint URLs match (default: `http://localhost:8000/api/predict-raw`)

### Predictions not working

- Verify the model file exists at `/diabetes-predictor/models/diabetes_model.pkl`
- Check the FastAPI server logs for error messages
- Ensure all input values are within valid ranges

## Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Responsive design

## Future Enhancements

- Add more detailed health metrics visualization
- Implement patient history/comparison
- Add export results as PDF
- Mobile app version
- Advanced analytics dashboard

@echo off
REM Diabetes Predictor - Frontend Setup and Run Script for Windows

echo.
echo 🏥 Diabetes Progression Predictor - Setup Script (Windows)
echo ===========================================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Ensure static directory exists
if not exist "diabetes-predictor\static" (
    echo 📁 Creating static directory...
    mkdir diabetes-predictor\static
)

echo.
echo ✅ Setup complete!
echo.
echo 🚀 Starting FastAPI server...
echo    The application will be available at: http://localhost:8000
echo.
echo 📊 Frontend: http://localhost:8000/
echo 📚 API Docs: http://localhost:8000/docs
echo 📋 ReDoc: http://localhost:8000/redoc
echo.

REM Start the server
cd diabetes-predictor
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

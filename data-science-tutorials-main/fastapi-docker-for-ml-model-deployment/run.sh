#!/bin/bash

# Diabetes Predictor - Frontend Setup and Run Script

echo "🏥 Diabetes Progression Predictor - Setup Script"
echo "=================================================="

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install/upgrade dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Ensure static directory exists
if [ ! -d "diabetes-predictor/static" ]; then
    echo "📁 Creating static directory..."
    mkdir -p diabetes-predictor/static
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Starting FastAPI server..."
echo "   The application will be available at: http://localhost:8000"
echo ""
echo "📊 Frontend: http://localhost:8000/"
echo "📚 API Docs: http://localhost:8000/docs"
echo "📋 ReDoc: http://localhost:8000/redoc"
echo ""

# Start the server
cd diabetes-predictor
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

#!/bin/bash
# QuantForex Pro Startup Script

echo "========================================"
echo "  QuantForex Pro - Starting Server"
echo "========================================"

# Check Python version
python --version

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "ERROR: requirements.txt not found!"
    echo "Current directory: $(pwd)"
    echo "Files here:"
    ls -la
    exit 1
fi

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting server..."
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}

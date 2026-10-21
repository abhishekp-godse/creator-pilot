@echo off
title CreatorPilot - FastAPI Backend
echo ===================================================
echo Starting CreatorPilot FastAPI Backend on port 8000
echo ===================================================

cd /d "%~dp0backend"

REM Check if virtual environment exists, if not create one
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat
echo Installing dependencies...
pip install -r requirements.txt

echo Starting Uvicorn Server...
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
pause

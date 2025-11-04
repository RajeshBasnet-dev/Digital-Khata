@echo off
REM Script to start both Django backend and React frontend for development on Windows

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

REM Start Django backend in background
echo Starting Django backend...
start "Django Backend" /min cmd /c "python manage.py runserver 8000"

REM Wait a moment for Django to start
timeout /t 3 /nobreak >nul

REM Start React frontend
echo Starting React frontend...
cd frontend
npm run dev
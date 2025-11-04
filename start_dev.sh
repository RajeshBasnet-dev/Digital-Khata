#!/bin/bash

# Script to start both Django backend and React frontend for development

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Start Django backend in background
echo "Starting Django backend..."
python manage.py runserver 8000 &
DJANGO_PID=$!

# Wait a moment for Django to start
sleep 3

# Start React frontend
echo "Starting React frontend..."
cd frontend
npm run dev

# Kill Django when frontend is stopped
kill $DJANGO_PID
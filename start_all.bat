@echo off
title CreatorPilot Launcher
echo ==========================================================
echo           Launching CreatorPilot Full-Stack
echo ==========================================================

start "CreatorPilot Backend" cmd /k "run_backend.bat"
timeout /t 3 /nobreak >nul
start "CreatorPilot Frontend" cmd /k "run_frontend.bat"

echo Backend and Frontend have been initiated!
echo Access the web dashboard at: http://localhost:5173
echo Access the API documentation at: http://localhost:8000/docs
echo Or open preview_dashboard.html for instant zero-setup preview!
pause

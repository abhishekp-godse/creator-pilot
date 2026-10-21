@echo off
title CreatorPilot - React Frontend
echo ===================================================
echo Starting CreatorPilot React Client on port 5173
echo ===================================================

cd /d "%~dp0frontend"

if not exist "node_modules" (
    echo Installing npm packages...
    call npm install
)

echo Starting Vite Dev Server...
call npm run dev
pause

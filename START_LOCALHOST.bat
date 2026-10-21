@echo off
title CreatorPilot - Localhost Server (Port 8080)
cd /d "%~dp0"

echo ==========================================================
echo   CreatorPilot - Starting on http://localhost:8080 ...
echo ==========================================================

REM 1. Try Node.js (Confirmed Available)
where node >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] Node.js runtime detected.
    echo [OK] Starting CreatorPilot on http://localhost:8080 ...
    start http://localhost:8080
    node server.js
    goto end
)

REM 2. Try genuine Python (verify execution, not Windows Store stub)
python -c "import sys; sys.exit(0)" >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] Python runtime detected.
    echo [OK] Starting CreatorPilot on http://localhost:8080 ...
    start http://localhost:8080
    python -m http.server 8080
    goto end
)

REM 3. Fallback: Native Windows PowerShell Socket Server (Zero Dependencies)
echo [OK] Using native Windows components...
start http://localhost:8080
powershell -NoProfile -ExecutionPolicy Bypass -File "start_server.ps1"

:end
pause

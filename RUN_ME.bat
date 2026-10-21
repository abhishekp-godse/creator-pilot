@echo off
title CreatorPilot - Server Launcher
cd /d "%~dp0"

echo ==========================================================
echo Starting CreatorPilot on http://localhost:3000 ...
echo This uses native Windows components (No Node/Python needed!)
echo ==========================================================

powershell -NoProfile -ExecutionPolicy Bypass -File "server.ps1"

pause

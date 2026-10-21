@echo off
title CreatorPilot - Local Web Server
echo =============================================================
echo Starting Local Web Server on port 3000...
echo Keep this black window OPEN while viewing the page!
echo =============================================================

cd /d "%~dp0"

REM Try python first
where python >nul 2>nul
if %errorlevel% equ 0 (
    echo Python detected. Starting server...
    start http://localhost:3000/preview_dashboard.html
    python -m http.server 3000
    goto end
)

REM Try py launcher
where py >nul 2>nul
if %errorlevel% equ 0 (
    echo Python launcher (py) detected. Starting server...
    start http://localhost:3000/preview_dashboard.html
    py -m http.server 3000
    goto end
)

REM Try node/npx
where npx >nul 2>nul
if %errorlevel% equ 0 (
    echo Node.js detected. Starting server via npx serve...
    start http://localhost:3000/preview_dashboard.html
    npx serve -p 3000 .
    goto end
)

echo [ERROR] Neither Python nor Node.js were found in your PATH.
echo To open the dashboard without a server, simply double click:
echo preview_dashboard.html directly!
echo.
pause

:end

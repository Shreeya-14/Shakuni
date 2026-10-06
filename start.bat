@echo off
title Shakuni Full-Stack Launcher
echo ===================================================
echo   Launching Shakuni: AI Framework for Strategic Deception
echo ===================================================
echo.

echo [1/2] Launching FastAPI Backend on http://127.0.0.1:8000 ...
start "Shakuni Backend" cmd /k "cd /d C:\Shakuni && python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000"

timeout /t 2 /nobreak >nul

echo [2/2] Launching Vite Frontend on http://localhost:5173 ...
start "Shakuni Frontend" cmd /k "cd /d C:\Shakuni\frontend && npm.cmd run dev"

echo.
echo ===================================================
echo   Shakuni is running!
echo   Open your browser at: http://localhost:5173
echo   Interactive API docs: http://127.0.0.1:8000/docs
echo ===================================================
pause

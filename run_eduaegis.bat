@echo off
echo ========================================================
echo Launching EduAegis - AI Tutor and Governed Grader...
echo Laptop running as Server on http://localhost:3000
echo ========================================================
cd /d "%~dp0"
npm run dev
pause

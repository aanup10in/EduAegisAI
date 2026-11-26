@echo off
echo ========================================================
echo Launching EduAegis on Streamlit (Port 8501)...
echo Multi-Subject AI Tutor & Governed Grader
echo ========================================================
cd /d "%~dp0"
streamlit run streamlit_app.py
pause

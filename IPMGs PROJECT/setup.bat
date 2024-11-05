@echo off

REM Check if virtual environment exists, and create it if it doesn't
IF NOT EXIST "venv\Scripts\activate" (
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Run the Streamlit app
python -m streamlit run app.py

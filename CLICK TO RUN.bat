@echo off
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in the system PATH.
    echo Please open the 'INSTALL PYTHON.exe' file and make sure "Install in PATH" is checked.
    exit /b 1
)
echo Starting setup...
python setup.py
if %errorlevel% neq 0 (
    echo Setup script failed.
    exit /b %errorlevel%
)

python main.py

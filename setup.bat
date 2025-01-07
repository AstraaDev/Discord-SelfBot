python -m pip install -r requirements.txt
cls
echo python main.py >> start.bat
start start.bat
start /b "" cmd /c &exit /b

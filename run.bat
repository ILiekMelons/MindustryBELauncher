@echo off
move main.py %USERPROFILE%\BEWrapper 2> nul
cd %USERPROFILE%\BEWrapper
python3 -m venv mindustry-env
.\mindustry-env\Scripts\activate.bat
pip3 install requests wget pathlib
python3 main.py

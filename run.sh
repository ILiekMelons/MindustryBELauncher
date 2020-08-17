#!/bin/bash
mv main.py ~/BEWrapper 2> /dev/null
cd ~/BEWrapper
python3 -m venv mindustry-env
source mindustry-env/bin/activate
pip3 install requests wget pathlib
python3 main.py

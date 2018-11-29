#!/usr/bin/env bash
if [ ! -d "venv" ]; then
    virtualenv -p python3 venv
fi
. venv/bin/activate

# Install python package requirements for the framework
pip3 install -r requirements.txt
#touch reports/api_tests.log
#pytest tests/ --junitxml=reports/testreport.xml
deactivate

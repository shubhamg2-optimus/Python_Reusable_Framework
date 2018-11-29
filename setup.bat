rem f [ ! -d "venv" ]; then
rem    virtualenv venv
rem fi
rem . venv/bin/activate

rem Install python package requirements for the framework
pip install -r requirements.txt
rem touch reports/api_tests.log
rem pytest tests/ --junitxml=reports/testreport.xml
rem deactivate
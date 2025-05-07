# End-to-end tests for Airalo Partners API
Test scenario for the flow of submitting order and retrieving eSIMS list.

## Install env and packages
```sh
python3 -m venv .env
.env/bin/pip3 install -r requirements.txt`
```

## Run tests
Before running, add client_id and client_secret for authentication to pytest.ini.
```sh
.env/bin/python -m pytest --color=yes --tb=short
```
The environment from pytest.ini is used by default. For running in another environment, use the flag
```sh
pytest -c pytest.stage.ini
```
where pytest.stage.ini - a file with environment configuration.

## Project description
There is a test which automates a real scenario:
1. submitting an order via POST /orders method
2. validating a response
3. retrieving eSIMs list via GET /sims method
4. validating a response

The structure of the testing framework is as follows:
- "tests" contains the test file test_api.py with the test scenario
- "utils" contains a client for calling the API and a validator for validating responses via JSON Schema
- "config.py" obtains the variables from pytest.ini
- "pytest.ini" contains env variables
- "conftest.py" contains fixtures for the test
- "requirements.txt" contains the list of required Python packages

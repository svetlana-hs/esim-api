import os
import pytest
import json

import config
from utils.api_client import ApiClient
from utils.schema_validator import load_schema


@pytest.fixture(scope="session")
def client():
    return ApiClient()


@pytest.fixture(scope="session", autouse=True)
def token(client):
    client.create_token()


@pytest.fixture(scope="session")
def order_response_schema():
    path = os.path.join(config.schemas_path, "order_response.json")
    return load_schema(path)


@pytest.fixture(scope="session")
def sims_response_schema():
    path = os.path.join(config.schemas_path, "sims_response.json")
    return load_schema(path)

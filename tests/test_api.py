import pytest
import json

from utils.schema_validator import validate_schema


@pytest.mark.parametrize(
    "payload",
    [
        {
            "quantity": 6,
            "package_id": "merhaba-7days-1gb",
            "type": "sim",
            "description": "test",
        },
    ],
)
def test_create_order(payload, client, order_response_schema, sims_response_schema):
    # Create a new order
    response = client.create_order(
        payload["quantity"],
        payload["package_id"],
        payload["type"],
        payload["description"],
    )
    assert (
        response.status_code == 200
    ), f"Expected status code is incorrect: {response.text}"

    # Validate response via json schema
    created_order = json.loads(response.content)
    validate_schema(created_order, order_response_schema)

    # Validate sent parameters
    assert (
        created_order["data"]["quantity"] == payload["quantity"]
    ), "Quantity is incorrect"
    assert (
        created_order["data"]["package_id"] == payload["package_id"]
    ), "Package ID is incorrect"
    assert created_order["data"]["type"] == payload["type"], "Type is incorrect"
    assert (
        created_order["data"]["description"] == payload["description"]
    ), "Description is incorrect"

    # Request sims
    response = client.get_sims(limit=6)
    assert (
        response.status_code == 200
    ), f"Expected status code is incorrect: {response.text}"

    # Validate response via json schema
    created_order = json.loads(response.content)
    validate_schema(created_order, sims_response_schema)

    sims = json.loads(response.content)

    # Validate items count and package_id in each item
    assert len(sims["data"]) == 6, "Sims count is incorrect"
    for sim in sims["data"]:
        assert (
            sim["simable"]["package_id"] == payload["package_id"]
        ), "Package ID is incorrect"

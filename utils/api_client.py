import requests
import logging
import http.client as http_client

from config import api_url, client_id, client_secret


# Enable debugging at http.client level (requests uses this under the hood)
http_client.HTTPConnection.debuglevel = 1

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

# Enable logging for requests and urllib3
logging.getLogger("requests.packages.urllib3").propagate = True


# Client for calling GitHub API
class ApiClient:
    def __init__(self):
        self.base_url = api_url
        self.headers = {
            "Accept": "application/json",
        }

    # Method POST /token
    def create_token(self):
        payload = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        response = requests.post(
            self.base_url + "/token", data=payload, headers=self.headers
        )
        response.raise_for_status()
        token = response.json().get("data").get("access_token")
        if not token:
            raise ValueError("Failed to retrieve access token")
        self.headers["Authorization"] = f"Bearer {token}"

    # Method POST /orders
    def create_order(
        self, quantity, package_id, type, description, brand_settings_name=None
    ):
        payload = {
            "quantity": quantity,
            "package_id": package_id,
            "type": type,
            "description": description,
            "brand_settings_name": brand_settings_name,
        }

        response = requests.post(
            self.base_url + "/orders", data=payload, headers=self.headers
        )

        return response

    # Method GET /sims
    def get_sims(self, include=None, limit=None, page=None):
        params = {
            "include": include if include else "order,order.status,order.user",
            "limit": limit if limit else 5,
            "page": page if page else 1,
        }
        response = requests.get(
            self.base_url + "/sims", params=params, headers=self.headers
        )

        return response

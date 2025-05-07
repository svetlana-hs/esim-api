import os


api_url = os.getenv("BASE_URL") + "/v2"
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

schemas_path = os.path.abspath("schemas") + "/"

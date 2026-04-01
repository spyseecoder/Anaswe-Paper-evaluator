import requests


def call_api(endpoint: str, method: str = "GET", data: dict = None, files: dict = None):
    """Helper function to call API"""
    try:
        if method == "GET":
            response = requests.get(endpoint)
        elif method == "POST":
            response = requests.post(endpoint, json=data, files=files)
        return response
    except Exception as e:
        return None

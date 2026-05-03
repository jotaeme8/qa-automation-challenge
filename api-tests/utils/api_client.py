import requests

BASE_URL = "https://petstore.swagger.io/v2"

class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, params=None):
        return self.session.get(f"{BASE_URL}{endpoint}", params=params)

    def post(self, endpoint, body=None):
        return self.session.post(f"{BASE_URL}{endpoint}", json=body)

    def put(self, endpoint, body=None):
        return self.session.put(f"{BASE_URL}{endpoint}", json=body)

    def delete(self, endpoint):
        return self.session.delete(f"{BASE_URL}{endpoint}")

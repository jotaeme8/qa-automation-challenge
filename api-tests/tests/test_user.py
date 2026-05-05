import uuid

BASE_USERNAME = "testuser_qa_auto"
USER_PAYLOAD = {
    "id": 0,
    "username": None,
    "firstName": "QA",
    "lastName": "Auto",
    "email": "qa@auto.com",
    "password": "senha123",
    "phone": "11999999999",
    "userStatus": 1,
}


def make_user_payload(username=None):
    payload = USER_PAYLOAD.copy()
    payload["username"] = username or f"{BASE_USERNAME}_{uuid.uuid4().hex[:8]}"
    return payload


def create_user(api, payload):
    return api.post("/user", payload)


def delete_user(api, username):
    return api.delete(f"/user/{username}")


class TestUser:
    def test_create_user(self, api):
        payload = make_user_payload()
        response = create_user(api, payload)
        assert response.status_code == 200
        delete_user(api, payload["username"])

    def test_get_user_by_username(self, api):
        payload = make_user_payload()
        create_user(api, payload)
        response = api.get(f"/user/{payload['username']}")
        assert response.status_code == 200
        assert response.json()["username"] == payload["username"]
        delete_user(api, payload["username"])

    def test_update_user(self, api):
        payload = make_user_payload()
        create_user(api, payload)
        updated = {**payload, "firstName": "QA Updated"}
        response = api.put(f"/user/{payload['username']}", updated)
        assert response.status_code == 200
        delete_user(api, payload["username"])

    def test_login_user(self, api):
        payload = make_user_payload()
        create_user(api, payload)
        response = api.get("/user/login", params={"username": payload["username"], "password": payload["password"]})
        assert response.status_code == 200
        delete_user(api, payload["username"])

    def test_logout_user(self, api):
        payload = make_user_payload()
        create_user(api, payload)
        api.get("/user/login", params={"username": payload["username"], "password": payload["password"]})
        response = api.get("/user/logout")
        assert response.status_code == 200
        delete_user(api, payload["username"])

    def test_delete_user(self, api):
        payload = make_user_payload()
        create_user(api, payload)
        response = delete_user(api, payload["username"])
        assert response.status_code == 200

    def test_get_deleted_user_returns_404(self, api):
        payload = make_user_payload()
        create_user(api, payload)
        delete_user(api, payload["username"])
        response = api.get(f"/user/{payload['username']}")
        assert response.status_code == 404

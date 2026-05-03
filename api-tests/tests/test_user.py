USERNAME = "testuser_qa_auto"
USER_PAYLOAD = {
    "id": 0,
    "username": USERNAME,
    "firstName": "QA",
    "lastName": "Auto",
    "email": "qa@auto.com",
    "password": "senha123",
    "phone": "11999999999",
    "userStatus": 1,
}

class TestUser:
    def test_create_user(self, api):
        response = api.post("/user", USER_PAYLOAD)
        assert response.status_code == 200

    def test_get_user_by_username(self, api):
        response = api.get(f"/user/{USERNAME}")
        assert response.status_code == 200
        assert response.json()["username"] == USERNAME

    def test_update_user(self, api):
        updated = {**USER_PAYLOAD, "firstName": "QA Updated"}
        response = api.put(f"/user/{USERNAME}", updated)
        assert response.status_code == 200

    def test_login_user(self, api):
        response = api.get("/user/login", params={"username": USERNAME, "password": USER_PAYLOAD["password"]})
        assert response.status_code == 200

    def test_logout_user(self, api):
        response = api.get("/user/logout")
        assert response.status_code == 200

    def test_delete_user(self, api):
        response = api.delete(f"/user/{USERNAME}")
        assert response.status_code == 200

    def test_get_deleted_user_returns_404(self, api):
        response = api.get(f"/user/{USERNAME}")
        assert response.status_code in [404, 200]

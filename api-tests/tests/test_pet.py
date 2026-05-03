PET_ID = 999888777
PET_PAYLOAD = {
    "id": PET_ID,
    "name": "Rex",
    "status": "available",
    "photoUrls": ["http://example.com/rex.jpg"],
}

class TestPet:
    def test_create_pet(self, api):
        response = api.post("/pet", PET_PAYLOAD)
        assert response.status_code == 200
        assert response.json()["name"] == "Rex"

    def test_get_pet_by_id(self, api):
        response = api.get(f"/pet/{PET_ID}")
        assert response.status_code == 200
        assert response.json()["id"] == PET_ID

    def test_update_pet(self, api):
        updated = {**PET_PAYLOAD, "name": "Rex Updated", "status": "sold"}
        response = api.put("/pet", updated)
        assert response.status_code == 200
        assert response.json()["name"] == "Rex Updated"

    def test_find_pets_by_status(self, api):
        response = api.get("/pet/findByStatus", params={"status": "available"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_delete_pet(self, api):
        response = api.delete(f"/pet/{PET_ID}")
        assert response.status_code == 200

    def test_get_deleted_pet_returns_404(self, api):
        response = api.get(f"/pet/{PET_ID}")
        assert response.status_code == 404

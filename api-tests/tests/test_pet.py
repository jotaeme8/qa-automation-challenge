import copy

PET_ID = 999888777
PET_PAYLOAD = {
    "id": PET_ID,
    "name": "Rex",
    "status": "available",
    "photoUrls": ["http://example.com/rex.jpg"],
}


def create_pet(api, payload=None):
    payload = payload or copy.deepcopy(PET_PAYLOAD)
    return api.post("/pet", payload)


def delete_pet(api, pet_id=PET_ID):
    return api.delete(f"/pet/{pet_id}")


class TestPet:
    def test_create_pet(self, api):
        response = create_pet(api)
        assert response.status_code == 200
        assert response.json()["name"] == "Rex"
        delete_pet(api)

    def test_get_pet_by_id(self, api):
        create_pet(api)
        response = api.get(f"/pet/{PET_ID}")
        assert response.status_code == 200
        assert response.json()["id"] == PET_ID
        delete_pet(api)

    def test_update_pet(self, api):
        create_pet(api)
        updated = {**PET_PAYLOAD, "name": "Rex Updated", "status": "sold"}
        response = api.put("/pet", updated)
        assert response.status_code == 200
        assert response.json()["name"] == "Rex Updated"
        delete_pet(api)

    def test_find_pets_by_status(self, api):
        response = api.get("/pet/findByStatus", params={"status": "available"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_delete_pet(self, api):
        create_pet(api)
        response = delete_pet(api)
        assert response.status_code == 200

    def test_get_deleted_pet_returns_404(self, api):
        create_pet(api)
        delete_pet(api)
        response = api.get(f"/pet/{PET_ID}")
        assert response.status_code == 404

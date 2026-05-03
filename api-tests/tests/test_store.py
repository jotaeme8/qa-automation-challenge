ORDER_PAYLOAD = {
    "id": 555444333,
    "petId": 1,
    "quantity": 2,
    "status": "placed",
    "complete": False,
}

class TestStore:
    def test_get_inventory(self, api):
        response = api.get("/store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_create_order(self, api):
        response = api.post("/store/order", ORDER_PAYLOAD)
        assert response.status_code == 200
        assert response.json()["status"] == "placed"

    def test_get_order_by_id(self, api):
        response = api.get(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 200

    def test_delete_order(self, api):
        response = api.delete(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 200

    def test_get_deleted_order_returns_404(self, api):
        response = api.get(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 404

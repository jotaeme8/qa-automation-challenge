ORDER_PAYLOAD = {
    "id": 555444333,
    "petId": 1,
    "quantity": 2,
    "status": "placed",
    "complete": False,
}


def create_order(api, payload=None):
    payload = payload or ORDER_PAYLOAD
    return api.post("/store/order", payload)


def delete_order(api, order_id=ORDER_PAYLOAD["id"]):
    return api.delete(f"/store/order/{order_id}")


class TestStore:
    def test_get_inventory(self, api):
        response = api.get("/store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_create_order(self, api):
        response = create_order(api)
        assert response.status_code == 200
        assert response.json()["status"] == "placed"
        delete_order(api)

    def test_get_order_by_id(self, api):
        create_order(api)
        response = api.get(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 200
        delete_order(api)

    def test_delete_order(self, api):
        create_order(api)
        response = delete_order(api)
        assert response.status_code == 200

    def test_get_deleted_order_returns_404(self, api):
        create_order(api)
        delete_order(api)
        response = api.get(f"/store/order/{ORDER_PAYLOAD['id']}")
        assert response.status_code == 404

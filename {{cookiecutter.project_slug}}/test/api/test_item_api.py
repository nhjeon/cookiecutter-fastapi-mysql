from starlette.testclient import TestClient

from app.main import app

CLIENT = TestClient(app)


def test_create_item_api():
    response = CLIENT.post("/items/",
                           json={
                               "name": "test"
                           },
                           headers={
                               "X-API-KEY": "fake_api_key"
                           }
                           )
    print(response.status_code)
    assert response.status_code == 200
    assert response.json()['name'] == "test"


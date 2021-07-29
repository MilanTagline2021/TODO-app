from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/TODO/",
        json={'id': 21,'title': 'pritesh', 'description': 'tl'}
    )
    assert response.status_code == 201
    assert response.json() == {'id': 21, 'title': 'pritesh','description': 'tl'}

def test_read_item_by_id():
    response = client.get("/TODO/1")
    assert response.status_code == 200
    assert response.json() == {
        "title": "kaushik",
        "description": "developer",
    }

def test_update_item_by_id():
    response = client.put(
        "/TODO/?id=1",
        json={'title': 'milan', 'description': 'python developer'}
    )
    assert response.status_code == 202
    print(response.json())
    assert response.json() == "Updated succeessfully"

def test_delete_item_by_id():
    response = client.delete("/TODO/?id=18")
    assert response.status_code == 204
    assert response.json() == "Deleted succeessfully"

def test_read_item_all():
    response = client.get("/TODO")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == [
        {'title': 'zeel', 'description': 'developer'}, 
        {'title': 'pritesh', 'description': 'developer'}, 
        {'title': 'pritesh', 'description': 'tl'}, 
        {'title': 'milan', 'description': 'python developer'}
    ]




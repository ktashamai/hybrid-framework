import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == 1
    assert "title" in json_data

def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == "foo"
    assert json_data["body"] == "bar"
    assert json_data["userId"] == 1

def test_get_post():
    print("Running GET Post test")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200




import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_single_post_success(base_url):
    response = requests.get(f"{base_url}/posts/1")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

def test_create_post_success(base_url):
    payload = {
        "title": "Learning Pytest",
        "body": "Integrating requests with pytest is powerful.",
        "userId": 1
    }
    
    response = requests.post(f"{base_url}/posts", json=payload)
    
    assert response.status_code == 201 
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data 
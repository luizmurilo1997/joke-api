import re
from unicodedata import category
from fastapi.testclient import TestClient

def test_get_random_joke(client: TestClient):
    response = client.get("/api/jokes/random")
    assert response.status_code == 200
    assert len(response.json()) == 1
    
def test_get_random_joke_by_category(client: TestClient):
    response = client.get("/api/jokes/category", params={"category":"animal"})
    assert response.status_code == 200
    assert len(response.json()) == 1
    
def test_get_random_joke_by_category_not_found(client: TestClient):
    category = 'testerror'
    response = client.get("/api/jokes/category", params={"category":category})
    assert response.status_code == 404
    assert response.json()['detail'] == f'Joke not found with category: {category}'    
    
def test_get_random_joke_by_filter(client: TestClient):
    limit = 5
    query = 'animal'
    response = client.get("/api/jokes/filter", params={"query":query, "limit": limit})
    assert response.status_code == 200
    assert len(response.json()) <= limit
    
def test_get_random_joke_by_filter_not_found(client: TestClient):
    limit = 5
    query = 'testerror'
    response = client.get("/api/jokes/filter", params={"query":query, "limit": limit})
    assert response.status_code == 404
    assert response.json()['detail'] == f'Joke not found with query: {query}' 
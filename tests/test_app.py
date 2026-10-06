import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_message(client):
    response = client.get("/health")
    assert b"Server is up and running" in response.data


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_is_html(client):
    response = client.get("/")
    assert "text/html" in response.content_type


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
import os

os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///./test.db")
os.environ.setdefault("SESSION_SECRET", "test-secret")
os.environ.setdefault("GOOGLE_CLIENT_ID", "dummy-client-id")
os.environ.setdefault("GOOGLE_CLIENT_SECRET", "dummy-client-secret")

from fastapi.testclient import TestClient

from app.main import app


def test_home_page_contains_google_login_button():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    assert "Googleでログイン" in response.text


def test_me_endpoint_returns_guest_when_not_logged_in():
    client = TestClient(app)
    response = client.get("/me")

    assert response.status_code == 200
    assert response.json() == {"authenticated": False}

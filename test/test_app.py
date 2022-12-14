from fastapi.testclient import TestClient

from app.main import create_app


class TestApp:
    client = TestClient(create_app())

    def test_get_root(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response

    def test_doc(self):
        response = self.client.get("/docs")
        assert response.status_code == 200
        assert response.content

    def test_openapi_json(self):
        response = self.client.get("/openapi.json")
        assert response.status_code == 200
        info = response.json()["info"]
        assert info["title"]
        assert info["description"]
        assert info["contact"]
        assert info["version"]

    def test_redoc(self):
        response = self.client.get("/redoc")
        assert response.status_code == 200
        assert response.content

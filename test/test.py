from starlette.testclient import TestClient

from app.main import app


class TestApp:
    client = TestClient(app)

    def test_download_file(self):
        response = self.client.get("/files/1")
        assert response.status_code == 200
        assert response.json() == {"message": "download_file"}

    def test_upload_file(self):
        response = self.client.post("/files")
        assert response.status_code == 200
        assert response.json() == {"message": "upload_file"}

    def test_info_file(self):
        response = self.client.head("/files/1")
        assert response.status_code == 200

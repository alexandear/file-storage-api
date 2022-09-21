import pytest
from starlette.testclient import TestClient

from app.main import app


class TestApp:
    client = TestClient(app)

    def test_download_file(self):
        response = self.client.get("/files/1")
        assert response.status_code == 200
        assert response.json() == {"message": "download_file"}

    @pytest.mark.freeze_uuids
    def test_upload_file(self):
        with open("data/отчет.txt", "rb") as f:
            response = self.client.post("/files", files={"file": f})
            assert response.status_code == 201
            assert response.json() == {"id": "00000000-0000-0000-0000-000000000000", "filename": "отчет.txt"}

    def test_info_file(self):
        response = self.client.head("/files/1")
        assert response.status_code == 200

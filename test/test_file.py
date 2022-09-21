from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import create_app


class TestFile:
    client = TestClient(create_app())

    def test_download_file(self):
        response = self.client.get("/files/1")
        assert response.status_code == 200
        assert response.headers.get("Content-Length") == "123"
        assert response.headers.get("Content-Type") == "application/json"
        assert response.json() == {"message": "downloaded 1"}

    def test_info_file(self):
        response = self.client.head("/files/1")
        assert response.status_code == 200
        assert response.content == b""
        assert response.headers.get("Content-Length") == "123"

    @pytest.mark.freeze_uuids
    def test_upload_file(self):
        this = Path(__file__).parent.resolve()
        with open(this.joinpath("data").joinpath("отчет.txt"), "rb") as f:
            response = self.client.post("/files", files={"file": f})
            assert response.status_code == 201
            assert response.json() == {"file_id": "00000000-0000-0000-0000-000000000000", "filename": "отчет.txt"}

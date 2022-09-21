from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import create_app
from app.router.file import get_db
from app.sql import model


class TestFile:
    engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()

    @pytest.fixture()
    def test_db(self):
        model.Base.metadata.create_all(bind=self.engine)
        yield
        model.Base.metadata.drop_all(bind=self.engine)

    def setup(self):
        app = create_app()
        app.dependency_overrides[get_db] = self.override_get_db
        self.client = TestClient(app)

    def test_download_file(self, test_db):
        this = Path(__file__).parent.resolve()
        with open(this.joinpath("data").joinpath("отчет.txt"), "rb") as f:
            response = self.client.post("/files", files={"file": f})
            assert response.status_code == 201
            file_id = response.json()["id"]
            assert file_id

        response = self.client.get(f"/files/{file_id}")
        assert response.status_code == 200
        assert response.headers.get("Content-Length") == "12"
        assert response.headers.get("Content-Type") == "application/json"
        assert response.json() == {"name": "отчет.txt"}

    def test_info_file(self, test_db):
        this = Path(__file__).parent.resolve()
        with open(this.joinpath("data").joinpath("отчет.txt"), "rb") as f:
            response = self.client.post("/files", files={"file": f})
            assert response.status_code == 201
            file_id = response.json()["id"]
            assert file_id

        response = self.client.head(f"/files/{file_id}")
        assert response.status_code == 200
        assert response.content == b""
        assert response.headers.get("Content-Length") == "12"

    @pytest.mark.freeze_uuids
    def test_upload_file(self, test_db):
        this = Path(__file__).parent.resolve()
        with open(this.joinpath("data").joinpath("отчет.txt"), "rb") as f:
            response = self.client.post("/files", files={"file": f})
            assert response.status_code == 201
            assert response.json() == {
                "size": 12,
                "id": "00000000-0000-0000-0000-000000000000",
                "name": "отчет.txt",
                "content": "Lorem ipsum\n",
            }

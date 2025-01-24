import os

import pytest
from fastapi.testclient import TestClient

from clipthread.server.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def test_db():
    db_path = "test_database.db"
    yield db_path
    if os.path.exists(db_path):
        os.remove(db_path)
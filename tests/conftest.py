import pytest

from fastapi.testclient import TestClient

from pathlib import Path
import sys

root = Path.cwd()
sys.path.append(str(root) + "/src")


from app import app


@pytest.fixture()
def client():
    return TestClient(app)

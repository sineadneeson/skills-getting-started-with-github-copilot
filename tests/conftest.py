import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app

# Snapshot of the original seed data taken once at import time
_ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    """Provide a synchronous TestClient for the FastAPI app."""
    return TestClient(app, follow_redirects=False)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore in-memory activities to the original seed state before each test."""
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))

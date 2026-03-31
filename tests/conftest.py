import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app, get_activities_store


@pytest.fixture
def test_activity_store():
    return copy.deepcopy(activities)


@pytest.fixture
def client(test_activity_store):
    def override_activity_store():
        return test_activity_store

    app.dependency_overrides[get_activities_store] = override_activity_store

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()

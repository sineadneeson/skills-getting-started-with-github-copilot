EXPECTED_ACTIVITIES = [
    "Chess Club",
    "Programming Class",
    "Gym Class",
    "Basketball Team",
    "Tennis Club",
    "Visual Arts",
    "Music Band",
    "Science Club",
    "Debate Team",
]

REQUIRED_FIELDS = {"description", "schedule", "max_participants", "participants"}


def test_get_activities_returns_200(client):
    # Arrange – seed data is set up by the autouse fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_all_seeded_activities(client):
    # Arrange – seed data is set up by the autouse fixture

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for name in EXPECTED_ACTIVITIES:
        assert name in data, f"Expected activity '{name}' not found in response"


def test_get_activities_each_has_required_fields(client):
    # Arrange – seed data is set up by the autouse fixture

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for name, details in data.items():
        missing = REQUIRED_FIELDS - details.keys()
        assert not missing, f"Activity '{name}' is missing fields: {missing}"


def test_get_activities_participants_is_a_list(client):
    # Arrange – seed data is set up by the autouse fixture

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    for name, details in data.items():
        assert isinstance(details["participants"], list), (
            f"Activity '{name}' participants should be a list"
        )

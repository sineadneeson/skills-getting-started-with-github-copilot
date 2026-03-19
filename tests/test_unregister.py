def test_unregister_existing_participant_returns_200(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # seeded participant

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    assert "message" in response.json()


def test_unregister_removes_participant_from_list(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # seeded participant

    # Act
    client.delete(f"/activities/{activity}/participants?email={email}")
    activities_response = client.get("/activities")

    # Assert
    participants = activities_response.json()[activity]["participants"]
    assert email not in participants


def test_unregister_participant_not_in_activity_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "notamember@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "someone@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_is_idempotent_on_second_attempt(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # seeded participant
    client.delete(f"/activities/{activity}/participants?email={email}")  # first removal

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404  # already removed; second attempt must fail

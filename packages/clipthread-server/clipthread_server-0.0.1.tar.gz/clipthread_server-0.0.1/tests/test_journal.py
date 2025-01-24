def test_create_journal(client):
    response = client.post(
        "/journal/",
        json={"query": "test query", "session_id": "test-session"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["query"] == "test query"
    assert data["session_id"] == "test-session"

def test_read_journal(client):
    # First create a journal entry
    create_response = client.post(
        "/journal/",
        json={"query": "test query", "session_id": "test-session"}
    )
    journal_id = create_response.json()["id"]

    # Then read it
    response = client.get(f"/journal/{journal_id}")
    assert response.status_code == 200
    assert response.json()["id"] == journal_id

def test_update_journal(client):
    # First create a journal entry
    create_response = client.post(
        "/journal/",
        json={"query": "test query", "session_id": "test-session"}
    )
    journal_id = create_response.json()["id"]

    # Then update it
    response = client.put(
        f"/journal/{journal_id}",
        json={"query": "updated query"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "updated query"

def test_delete_journal(client):
    # First create a journal entry
    create_response = client.post(
        "/journal/",
        json={"query": "test query", "session_id": "test-session"}
    )
    journal_id = create_response.json()["id"]

    # Then delete it
    response = client.delete(f"/journal/{journal_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Journal entry deleted"}

    # Verify it's deleted
    response = client.get(f"/journal/{journal_id}")
    assert response.status_code == 404

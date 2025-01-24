def test_create_clipboard(client):
    response = client.post(
        "/clipboard/",
        json={"text": "test clip", "pinned": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["text"] == "test clip"
    assert data["pinned"] == False

def test_read_clipboard(client):
    # First create a clipboard entry
    create_response = client.post(
        "/clipboard/",
        json={"text": "test clip", "pinned": False}
    )
    clip_id = create_response.json()["id"]

    # Then read it
    response = client.get(f"/clipboard/{clip_id}")
    assert response.status_code == 200
    assert response.json()["id"] == clip_id

def test_update_clipboard(client):
    # First create a clipboard entry
    create_response = client.post(
        "/clipboard/",
        json={"text": "test clip", "pinned": False}
    )
    clip_id = create_response.json()["id"]

    # Then update it
    response = client.put(
        f"/clipboard/{clip_id}",
        json={"text": "updated clip", "pinned": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "updated clip"
    assert data["pinned"] == True

def test_delete_clipboard(client):
    # First create a clipboard entry
    create_response = client.post(
        "/clipboard/",
        json={"text": "test clip", "pinned": False}
    )
    clip_id = create_response.json()["id"]

    # Then delete it
    response = client.delete(f"/clipboard/{clip_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Clipboard entry deleted"}

    # Verify it's deleted
    response = client.get(f"/clipboard/{clip_id}")
    assert response.status_code == 404
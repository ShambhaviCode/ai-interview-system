import pytest
from fastapi.testclient import TestClient

from surveillance_service import session_manager
from surveillance_service.main import app


@pytest.fixture
def client():
    session_manager.sessions.clear()
    return TestClient(app)


def create_session(client, user_id="candidate-1"):
    response = client.post("/sessions", params={"user_id": user_id})
    assert response.status_code == 200
    return response.json()


def test_create_session(client):
    session = create_session(client)

    assert session["userId"] == "candidate-1"
    assert session["status"] == "CREATED"
    assert session_manager.get_session(session["sessionId"]) is not None


def test_init_attaches_session(client):
    session_id = create_session(client)["sessionId"]

    with client.websocket_connect("/ws") as ws:
        ws.send_json({"type": "INIT", "sessionId": session_id})
        assert ws.receive_json() == {"type": "CONNECTED", "sessionId": session_id}
        assert session_manager.get_session(session_id)["status"] == "ACTIVE"


def test_init_with_unknown_session_does_not_confirm(client):
    with client.websocket_connect("/ws") as ws:
        ws.send_json({"type": "INIT", "sessionId": "does-not-exist"})
        assert ws.receive_json()["error"] == "Invalid session"

        # The connection stays usable, and no CONNECTED message follows.
        ws.send_json({"type": "PING", "sessionId": "does-not-exist"})
        assert ws.receive_json()["error"] == "Unknown message type"


def test_end_session(client):
    session_id = create_session(client)["sessionId"]

    with client.websocket_connect("/ws") as ws:
        ws.send_json({"type": "INIT", "sessionId": session_id})
        ws.receive_json()
        ws.send_json({"type": "END_SESSION", "sessionId": session_id})
        assert ws.receive_json() == {"type": "SESSION_ENDED", "sessionId": session_id}

    assert session_manager.get_session(session_id)["status"] == "ENDED"


def test_cannot_end_another_connections_session(client):
    session_id = create_session(client)["sessionId"]

    with client.websocket_connect("/ws") as owner, client.websocket_connect("/ws") as other:
        owner.send_json({"type": "INIT", "sessionId": session_id})
        owner.receive_json()

        other.send_json({"type": "END_SESSION", "sessionId": session_id})
        assert other.receive_json()["type"] == "ERROR"
        assert session_manager.get_session(session_id)["status"] == "ACTIVE"


def test_ended_session_cannot_be_reattached(client):
    session_id = create_session(client)["sessionId"]
    session_manager.end_session(session_id)

    with client.websocket_connect("/ws") as ws:
        ws.send_json({"type": "INIT", "sessionId": session_id})
        assert ws.receive_json()["error"] == "Invalid session"


def test_disconnect_ends_session(client):
    session_id = create_session(client)["sessionId"]

    with client.websocket_connect("/ws") as ws:
        ws.send_json({"type": "INIT", "sessionId": session_id})
        ws.receive_json()

    assert session_manager.get_session(session_id)["status"] == "ENDED"


@pytest.mark.parametrize("raw", ["not json", "[]", '{"type": "INIT"}', '{"sessionId": 5}'])
def test_malformed_messages_get_an_error_reply(client, raw):
    with client.websocket_connect("/ws") as ws:
        ws.send_text(raw)
        assert ws.receive_json()["type"] == "ERROR"

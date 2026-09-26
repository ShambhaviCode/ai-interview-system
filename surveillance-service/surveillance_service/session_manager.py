import uuid
from datetime import datetime, timezone

# In-memory store: sessionId -> session. Lost on restart.
sessions = {}


def create_session(user_id: str):
    session_id = str(uuid.uuid4())

    session = {
        "sessionId": session_id,
        "userId": user_id,
        "status": "CREATED",
        "createdAt": datetime.now(timezone.utc),
        "wsConnectionId": None,
    }

    sessions[session_id] = session
    return session


def get_session(session_id: str):
    return sessions.get(session_id)


def attach_websocket(session_id: str, ws_connection_id: str):
    session = sessions.get(session_id)
    if not session or session["status"] == "ENDED":
        return None

    session["wsConnectionId"] = ws_connection_id
    session["status"] = "ACTIVE"
    return session


def end_session(session_id: str):
    session = sessions.get(session_id)
    if not session:
        return None

    session["status"] = "ENDED"
    session["wsConnectionId"] = None
    session["endedAt"] = datetime.now(timezone.utc)
    return session

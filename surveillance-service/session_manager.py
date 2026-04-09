import uuid
from datetime import datetime

sessions = {}

def create_session(user_id: str):
    session_id = str(uuid.uuid4())

    session = {
        "sessionId": session_id,
        "userId": user_id,
        "status": "CREATED",
        "createdAt": datetime.utcnow(),
        "wsConnectionId": None
    }

    sessions[session_id] = session
    return session
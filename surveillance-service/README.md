# Surveillance Service

FastAPI service that creates interview sessions and tracks their
WebSocket connection.

## Run

```bash
cd surveillance-service
pip install -r requirements.txt
uvicorn surveillance_service.main:app --reload
```

## Test

```bash
pip install -r requirements-dev.txt
python -m pytest
```

## API

| Route | Description |
| --- | --- |
| `GET /` | Health check |
| `POST /sessions?user_id=<id>` | Create a session (`status: CREATED`) |
| `WS /ws` | Session WebSocket (messages below) |

WebSocket messages (JSON, all require `sessionId`):

| Client sends | Server replies |
| --- | --- |
| `{"type": "INIT", "sessionId": "..."}` | `CONNECTED`, session becomes `ACTIVE` |
| `{"type": "END_SESSION", "sessionId": "..."}` | `SESSION_ENDED` (only from the connection that sent `INIT`) |

Invalid or unknown messages get `{"type": "ERROR", "error": "..."}` and
the connection stays open. Disconnecting ends the attached session.

Sessions are stored in memory and are lost when the service restarts.

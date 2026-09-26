import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from surveillance_service.session_manager import attach_websocket, end_session, get_session

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections = []
        self.session_map = {}  # sessionId → websocket

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

        # find session linked to websocket
        session_id = self.session_for(websocket)

        if session_id:
            end_session(session_id)
            del self.session_map[session_id]

    def session_for(self, websocket: WebSocket):
        for sid, ws in self.session_map.items():
            if ws == websocket:
                return sid
        return None

    async def attach_session(self, session_id: str, websocket: WebSocket):
        session = get_session(session_id)

        if not session or session["status"] == "ENDED":
            await send_error(websocket, "Invalid session")
            return False

        self.session_map[session_id] = websocket

        ws_id = str(id(websocket))
        attach_websocket(session_id, ws_id)
        return True

    async def send_to_session(self, session_id: str, message: dict):
        websocket = self.session_map.get(session_id)
        if websocket:
            await websocket.send_json(message)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()


async def send_error(websocket: WebSocket, message: str):
    await websocket.send_json({"type": "ERROR", "error": message})


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            # Parse manually so one malformed message gets an error reply
            # instead of an exception that drops the connection.
            try:
                data = json.loads(await websocket.receive_text())
            except json.JSONDecodeError:
                await send_error(websocket, "Message must be JSON")
                continue

            if not isinstance(data, dict) or not isinstance(data.get("sessionId"), str):
                await send_error(websocket, "Message must include a sessionId")
                continue

            session_id = data["sessionId"]

            if data.get("type") == "INIT":
                if not await manager.attach_session(session_id, websocket):
                    continue

                await websocket.send_json({
                    "type": "CONNECTED",
                    "sessionId": session_id
                })

            # 🔥 Example: end session manually
            elif data.get("type") == "END_SESSION":
                # Only the socket attached to a session may end it.
                if manager.session_for(websocket) != session_id:
                    await send_error(websocket, "Session is not attached to this connection")
                    continue

                end_session(session_id)
                del manager.session_map[session_id]

                await websocket.send_json({
                    "type": "SESSION_ENDED",
                    "sessionId": session_id
                })

            else:
                await send_error(websocket, "Unknown message type")

    except WebSocketDisconnect:
        pass
    finally:
        manager.disconnect(websocket)

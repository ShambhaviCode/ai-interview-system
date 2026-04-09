import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from session_manager import attach_websocket, end_session, get_session  # Ensure session_manager.py exists in parent directory

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
        session_id = None
        for sid, ws in self.session_map.items():
            if ws == websocket:
                session_id = sid
                break

        if session_id:
            end_session(session_id)
            del self.session_map[session_id]

    async def attach_session(self, session_id: str, websocket: WebSocket):
        session = get_session(session_id)

        if not session:
            await websocket.send_json({"error": "Invalid session"})
            return

        self.session_map[session_id] = websocket

        ws_id = str(id(websocket))
        attach_websocket(session_id, ws_id)

    async def send_to_session(self, session_id: str, message: dict):
        websocket = self.session_map.get(session_id)
        if websocket:
            await websocket.send_json(message)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_json()

            if data["type"] == "INIT":
                session_id = data["sessionId"]

                await manager.attach_session(session_id, websocket)

                await websocket.send_json({
                    "type": "CONNECTED",
                    "sessionId": session_id
                })

            # 🔥 Example: end session manually
            elif data["type"] == "END_SESSION":
                session_id = data["sessionId"]
                end_session(session_id)

                await websocket.send_json({
                    "type": "SESSION_ENDED",
                    "sessionId": session_id
                })

    except WebSocketDisconnect:
        manager.disconnect(websocket)
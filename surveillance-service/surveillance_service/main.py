from fastapi import FastAPI
from surveillance_service.session_manager import create_session
from surveillance_service.websocket import router as websocket_router

# Debug (to confirm correct file is running)
print("🔥 MAIN.PY LOADED")

app = FastAPI()

# Include WebSocket routes
app.include_router(websocket_router)


# Home route
@app.get("/")
def home():
    return {"message": "Surveillance Service Running"}


# Create session API
@app.post("/sessions")
def create(user_id: str):
    return create_session(user_id)
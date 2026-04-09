from fastapi import FastAPI
from session_manager import create_session

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Server is running"}


@app.post("/create-session")
def start_session(user_id: str):
    session = create_session(user_id)
    return session
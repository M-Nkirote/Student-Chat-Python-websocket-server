import socketio
from fastapi import FastAPI
from model_handler import process_prompt

sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)


@sio.on("connect")
async def connect(sid, environ, auth):
    print("Client connected:", sid)
    return True


@sio.on("disconnect")
async def disconnect(sid):
    print("Client disconnected:", sid)


@sio.on("send_prompt")
async def handle_prompt(sid, data):
    print("Received prompt:", data)

    # Extract required fields from client data
    prompt = data["prompt"]
    student_code = data["student_code"]
    first_name = data.get("first_name", "Unknown")  # fallback to Unknown if not provided

    session_code = sid  # Use Socket.IO session ID as the session_code

    response = await process_prompt(prompt, student_code, first_name, session_code)
    await sio.emit("model_response", {"response": response}, to=sid)
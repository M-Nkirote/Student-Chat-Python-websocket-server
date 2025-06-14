import socketio
from fastapi import FastAPI
from model_handler import process_prompt

sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode="asgi")
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)


@sio.on("connect")
async def connect(sid, environ):
    print("Client connected:", sid)


@sio.on("disconnect")
async def disconnect(sid):
    print("Client disconnected:", sid)


@sio.on("send_prompt")
async def handle_prompt(sid, data):
    print("Received prompt:", data)
    response = await process_prompt(data["prompt"], data["student_code"])
    await sio.emit("model_response", {"response": response}, to=sid)

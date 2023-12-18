from fastapi import FastAPI, WebSocket, WebSocketDisconnect, status
from fastapi.responses import HTMLResponse
from typing import Dict

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.id_websocket_dict: Dict[int, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: int):
        await websocket.accept()
        self.id_websocket_dict[client_id] = websocket

    def disconnect(self, websocket: WebSocket):
        client_id_websocket_connection_to_delete = 0
        for client_id, websocket_connection in self.id_websocket_dict.items():
            if websocket_connection == websocket:
                client_id_websocket_connection_to_delete = client_id
        del self.id_websocket_dict[client_id_websocket_connection_to_delete]

    # send a message to yourself
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for client_id, connection in self.id_websocket_dict.items():  # connection here is a websocket object
            await connection.send_text(message)

    async def send_to(self, messsgae: str, receiver_id: int):
        await self.id_websocket_dict[receiver_id].send_text(messsgae)


manager = ConnectionManager()


@app.get("/")
async def get():
    with open("websocket.html", "r") as f:
        html = f.read()
    return HTMLResponse(html, status_code=status.HTTP_200_OK)


@app.websocket("/ws/{sender_id}/{receiver_id}")
async def websocket_endpoint(websocket: WebSocket, sender_id: int, receiver_id: int):
    await manager.connect(websocket, sender_id)
    print(manager.id_websocket_dict)
    try:
        while True:
            data = await websocket.receive_text()
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            # await manager.broadcast(f"Client #{sender_id} says: {data}")
            await manager.send_to(f"#{sender_id} says {data}", receiver_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{sender_id} left the chat")

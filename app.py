from fastapi import FastAPI, File, UploadFile, status, HTTPException, WebSocket, WebSocketDisconnect, status
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated, Dict
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
upload_dir = "uploads"
os.makedirs(upload_dir, exist_ok=True)


@app.get(path="/")
def home():
    with open("templates/home.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(html_content, status_code=status.HTTP_200_OK)


@app.post(path="/upload-files")
async def upload_files(files: Annotated[list[UploadFile], File(description="Upload 0 or more files")]):
    try:
        if not files:
            return {"message": "No file sent"}

        file_contents = [await file.read() for file in files]
        save_paths = [os.path.join(upload_dir, file.filename)
                      for file in files]

        for i, file_path in enumerate(save_paths):
            with open(file_path, "wb") as f:
                f.write(file_contents[i])

        with open("templates/success_page.html", "r") as f:
            html_content = f.read()
        return HTMLResponse(html_content, status_code=status.HTTP_200_OK)

    except Exception as e:
        with open("templates/no_upload.html", "r") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get(path="/downloads")
async def download(filename: str):
    return FileResponse(path=f"uploads/{filename}", filename=filename)


@app.get("/stream")
def main():
    def iterfile():  #
        with open("Counting Stars - OneRepublic (violin_cello_bass cover) Simply Three _ Shaorin Music.mp4", mode="rb") as file_like:  #
            yield from file_like  #

    return StreamingResponse(iterfile(), media_type="video/mp4")


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

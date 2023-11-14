from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
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

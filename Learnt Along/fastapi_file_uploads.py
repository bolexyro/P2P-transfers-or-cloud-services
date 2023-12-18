# if you need explanation Adebola, go to https://chat.openai.com/c/4a67a07c-6b99-4ad9-8e9d-2f16946c1da3
from fastapi import FastAPI, UploadFile, File
from starlette.responses import HTMLResponse
from typing import Annotated

app = FastAPI()


@app.get(path="/")
def home():
    content = """
<body>
<form action="/multiple-files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</body>
    """
    return HTMLResponse(content=content)

# metadata as per no annotations.


@app.post(path="upload-file-without-metadata")
async def upload_file_without_metadata(file: UploadFile | None = None):
    # the None = None is to make the file optional.
    if not file:
        return {"message": "No upload file sent"}
    #     filename: A str with the original file name that was uploaded (e.g. myimage.jpg).
    # content_type: A str with the content type (MIME type / media type) (e.g. image/jpeg).
    # file: A SpooledTemporaryFile (a file-like object). This is the actual Python file that
    # you can pass directly to other functions or libraries that expect a "file-like" object.

    # UploadFile has the following async methods. They all call the corresponding file methods underneath (using the internal SpooledTemporaryFile).

    # write(data): Writes data (str or bytes) to the file.
    # read(size): Reads size (int) bytes/characters of the file.
    # seek(offset): Goes to the byte position offset (int) in the file.
    # E.g., await myfile.seek(0) would go to the start of the file.
    # This is especially useful if you run await myfile.read() once and then need to read the contents again.
    # close(): Closes the file.
    contents = await file.read()
    print(contents)
    print(file.filename)
    print(file.content_type)
    print(file.file)
    await file.close()
    return "DOne"


@app.post(path="/upload-file-with-metadata")
async def upload_file_with_metadata(file: Annotated[UploadFile, File(description="A file to be uploaded")] | None = None):
    return "Done"


@app.post(path="/multiple-files")
async def multiple_files(files: Annotated[list[UploadFile], File(description="Multiple Files to be uploaded")]):
    return {"filename": [file.filename for file in files]}

from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
import tempfile
from text_extraction import extract
from model import generate


class Response(BaseModel):
    result: str | None


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict", response_model=Response)
async def predict(file: UploadFile = Form(...), question: str = Form(...)) -> Any:    # implement this code block
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(await file.read())
        tmp_file_path = tmp_file.name

    file_extension = file.filename.split(".")[-1].lower()
    if file_extension in ["csv", "pdf", "docx", "txt"]:
        extracted_text = extract(tmp_file_path, file_extension)
    else:
        return {"result": "Unsupported file format"}

    return {"result": generate(extracted_text, question)}


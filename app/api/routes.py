from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
import tempfile, os
from app.services.transcriber import transcribe_audio_file
from app.templates.html_forms import get_upload_form_html 
from app.controllers.transcribe_controller import handle_transcription

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=get_upload_form_html())


@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    return await handle_transcription(file)
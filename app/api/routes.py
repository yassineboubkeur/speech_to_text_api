from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, HTMLResponse
import tempfile, os
from app.services.transcriber import transcribe_audio_file
from app.templates.html_forms import get_upload_form_html 
from app.controllers.transcribe_controller import handle_transcription

# Create an API router to define route handlers
router = APIRouter()

# Endpoint to serve the HTML page for uploading audio files
@router.get("/", response_class=HTMLResponse)
async def home():
    # Return the HTML content for the upload form
    return HTMLResponse(content=get_upload_form_html())

# Endpoint to receive uploaded audio file and return its transcription
@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Pass the uploaded file to the transcription handler and return the result
    return await handle_transcription(file)

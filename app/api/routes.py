from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
import tempfile, os
from app.services.transcriber import transcribe_audio_file
from app.templates.html_forms import get_upload_form_html 

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=get_upload_form_html())



@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    try:
        # استخراج الامتداد الأصلي للملف
        ext = os.path.splitext(file.filename)[1].lower()

        # قائمة الامتدادات المدعومة
        supported_formats = [".flac", ".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".oga", ".ogg", ".wav", ".webm"]

        if ext not in supported_formats:
            return JSONResponse(status_code=400, content={"error": "Unsupported audio format."})

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        text = transcribe_audio_file(tmp_path)
        os.remove(tmp_path)

        return {"text": text}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

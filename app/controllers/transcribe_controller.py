import os
import tempfile
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from app.services.transcriber import transcribe_audio_file

# قائمة الامتدادات المدعومة
SUPPORTED_FORMATS = [".flac", ".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".oga", ".ogg", ".wav", ".webm"]

async def handle_transcription(file: UploadFile):
    try:
        ext = os.path.splitext(file.filename)[1].lower()

        if ext not in SUPPORTED_FORMATS:
            return JSONResponse(status_code=400, content={"error": "Unsupported audio format."})

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        text = transcribe_audio_file(tmp_path)
        os.remove(tmp_path)

        return {"text": text}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

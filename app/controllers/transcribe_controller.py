import os
import tempfile
import logging
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from app.services.transcriber import transcribe_audio_file

logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = [".flac", ".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".oga", ".ogg", ".wav", ".webm"]

async def handle_transcription(file: UploadFile):
    try:
        ext = os.path.splitext(file.filename)[1].lower()

        if ext not in SUPPORTED_FORMATS:
            logger.warning(f"Unsupported format: {ext}")
            return JSONResponse(status_code=400, content={"error": "Unsupported audio format."})

        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            file_data = await file.read()
            tmp.write(file_data)
            tmp_path = tmp.name

        logger.info(f"File saved temporarily: {tmp_path}")

        text = transcribe_audio_file(tmp_path)
        os.remove(tmp_path)

        logger.info("File transcribed and temp file deleted")
        return {"text": text}

    except Exception as e:
        logger.exception("Transcription failed due to an unexpected error")
        return JSONResponse(status_code=500, content={"error": str(e)})

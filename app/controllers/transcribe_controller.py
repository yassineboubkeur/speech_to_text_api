import os
import tempfile
import logging
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from app.services.transcriber import transcribe_audio_file

# Initialize logger for this module
logger = logging.getLogger(__name__)

# List of supported audio file extensions
SUPPORTED_FORMATS = [".flac", ".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".oga", ".ogg", ".wav", ".webm"]

async def handle_transcription(file: UploadFile):
    try:
        # Extract file extension and convert to lowercase
        ext = os.path.splitext(file.filename)[1].lower()

        # Check if file extension is supported
        if ext not in SUPPORTED_FORMATS:
            logger.warning(f"Unsupported format: {ext}")
            return JSONResponse(status_code=400, content={"error": "Unsupported audio format."})

        # Create a temporary file with the correct suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
            file_data = await file.read()  # Read the uploaded file contents
            tmp.write(file_data)            # Write data to the temp file
            tmp_path = tmp.name             # Save temp file path for later use

        logger.info(f"File saved temporarily: {tmp_path}")

        # Call transcription logic using the temp file path
        text = transcribe_audio_file(tmp_path)

        # Remove the temporary file after transcription
        os.remove(tmp_path)

        logger.info("File transcribed and temp file deleted")

        # Return the transcription result as a dictionary
        return {"text": text}

    except Exception as e:
        # Log the exception with traceback
        logger.exception("Transcription failed due to an unexpected error")

        # Return HTTP 500 with error message in JSON format
        return JSONResponse(status_code=500, content={"error": str(e)})

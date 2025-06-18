import openai
from app.core.config import settings  # أو من المكان اللي فيه Settings

def transcribe_audio_file(file_path: str) -> str:
    openai.api_key = settings.OPENAI_API_KEY

    with open(file_path, "rb") as audio_file:
        response = openai.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
    return response.text

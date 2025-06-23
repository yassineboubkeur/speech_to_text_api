import openai
import time
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds between retries

def transcribe_audio_file(file_path: str) -> str:
    openai.api_key = settings.OPENAI_API_KEY

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(f"[Attempt {attempt}] Transcribing file: {file_path}")
            
            with open(file_path, "rb") as audio_file:
                response = openai.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-1"
                )

            logger.info("Transcription successful")
            return response.text

        except openai.OpenAIError as e:
            logger.warning(f"OpenAI API error: {e}")
            if attempt == MAX_RETRIES:
                logger.error("Max retries reached. Failing transcription.")
                raise
            time.sleep(RETRY_DELAY)

        except Exception as e:
            logger.exception("Unexpected error during transcription")
            raise

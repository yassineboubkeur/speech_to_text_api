import openai
import time
import logging
from app.core.config import settings

# Initialize logger for this module
logger = logging.getLogger(__name__)

# Maximum number of retries when calling OpenAI API
MAX_RETRIES = 3
# Delay in seconds between retry attempts
RETRY_DELAY = 2

def transcribe_audio_file(file_path: str) -> str:
    """
    Transcribes an audio file using OpenAI Whisper API with retry and error handling.

    Args:
        file_path (str): The path to the audio file to be transcribed.

    Returns:
        str: The transcribed text from the audio.

    Raises:
        openai.OpenAIError: If the OpenAI API call fails after maximum retries.
        Exception: For any other unexpected errors during transcription.
    """
    # Set the OpenAI API key from the settings
    openai.api_key = settings.OPENAI_API_KEY

    # Attempt transcription up to MAX_RETRIES times
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(f"[Attempt {attempt}] Transcribing file: {file_path}")
            
            # Open the audio file in binary mode
            with open(file_path, "rb") as audio_file:
                # Call OpenAI Whisper transcription endpoint
                response = openai.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-1"
                )

            logger.info("Transcription successful")
            # Return the transcribed text from the API response
            return response.text

        except openai.OpenAIError as e:
            # Log the API error and retry if attempts remain
            logger.warning(f"OpenAI API error: {e}")
            if attempt == MAX_RETRIES:
                logger.error("Max retries reached. Failing transcription.")
                # Raise error if max retries exhausted
                raise
            # Wait before retrying
            time.sleep(RETRY_DELAY)

        except Exception as e:
            # Log unexpected exceptions and re-raise
            logger.exception("Unexpected error during transcription")
            raise

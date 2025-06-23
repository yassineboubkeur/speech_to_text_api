Got it! Here’s the complete **README.md** file content based on the documentation above. I’ll save it as a file for you.

````markdown
# Speech to Text API

## Overview
This API allows you to upload audio files and get transcriptions using OpenAI Whisper via a FastAPI backend.

- **Base URL:** `/`
- **Tech Stack:** FastAPI, OpenAI Whisper API
- **Supported Audio Formats:** `.flac`, `.m4a`, `.mp3`, `.mp4`, `.mpeg`, `.mpga`, `.oga`, `.ogg`, `.wav`, `.webm`

## Endpoints

### 1. GET /

- **Description:** Returns an HTML form for uploading audio files.
- **Method:** `GET`
- **Response:** HTML page with file upload form.

### 2. POST /transcribe/

- **Description:** Accepts an audio file and returns the transcribed text.
- **Method:** `POST`
- **Request:**
  - Content-Type: `multipart/form-data`
  - Field: `file` (audio file)
- **Response:** JSON with transcription text, e.g.:
  ```json
  {
    "text": "Transcribed text here"
  }
````

* **Errors:**

  * 400: Unsupported audio format
  * 500: Internal server error or OpenAI API failure

## Usage Example

```bash
curl -X POST "http://localhost:8000/transcribe/" \
  -H "accept: application/json" \
  -F "file=@path/to/audio.mp3"
```

## Setup & Run

1. Create `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

4. Open your browser and navigate to:

```
http://localhost:8000
```

to upload audio files via the form.

## Project Structure

```
app/
├── api/routes.py               # API endpoints
├── controllers/transcribe.py   # Transcription controller
├── services/transcriber.py     # OpenAI Whisper integration
├── templates/html_forms.py     # HTML upload form
├── core/config.py              # Environment config
├── main.py                     # FastAPI app entry
```

## Notes

* Temporary uploaded files are deleted after transcription.
* API uses retry logic (3 attempts) when calling OpenAI Whisper.
* Logging is enabled for troubleshooting.

---

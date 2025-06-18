from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.routes import router

app = FastAPI(title="Speech to Text API")

@app.get("/")
async def main():
    content = """
    <html>
        <body>
            <h2>Upload audio file for transcription</h2>
            <form action="/transcribe/" enctype="multipart/form-data" method="post">
                <input name="file" type="file" accept="audio/*">
                <input type="submit" value="Upload and Transcribe">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)

app.include_router(router)

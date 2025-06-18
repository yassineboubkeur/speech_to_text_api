def get_upload_form_html() -> str:
    return """
    <html>
        <head>
            <title>Speech to Text</title>
        </head>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Upload audio file for transcription</h2>
            <form action="/transcribe/" enctype="multipart/form-data" method="post">
                <input name="file" type="file" accept="audio/*" required>
                <br><br>
                <input type="submit" value="Upload and Transcribe">
            </form>
        </body>
    </html>
    """

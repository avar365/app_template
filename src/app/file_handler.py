import os
from pathlib import Path
from datetime import datetime
from app.db import log_file_action

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def handle_upload(uploaded_file):
    file_path = UPLOAD_DIR / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    
    log_file_action(filename=uploaded_file.name, action="upload")
    return file_path

def list_uploaded_files():
    return os.listdir(UPLOAD_DIR)
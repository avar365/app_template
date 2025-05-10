import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path("data") / "file_log.db"
DB_PATH.parent.mkdir(exist_ok=True)

def _connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS file_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            action TEXT,
            timestamp TEXT
        )
    """)
    return conn

def log_file_action(filename: str, action: str):
    conn = _connect()
    conn.execute(
        "INSERT INTO file_events (filename, action, timestamp) VALUES (?, ?, ?)",
        (filename, action, datetime.now(timezone.utc).isoformat())
    )
    conn.commit()
    conn.close()
import os

from pyrogram import Client

app = Client(
    "session",  # This is the session name
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    session_string=os.environ.get("STRING_SESSION"),
)

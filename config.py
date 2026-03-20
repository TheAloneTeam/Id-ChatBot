import os

# MongoDB connection string (for storing/retrieving chat data)
MONGO_URL = os.environ.get("MONGO_URL", "")

# Together AI API key and endpoint

# Only the OWNER_ID will receive replies (your own Telegram ID)
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))  # Replace with your actual ID in Heroku env

import os
from dotenv import load_dotenv

load_dotenv()

# ================== TELEGRAM ==================

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")

# ================== DATABASE ==================

MONGO_URL = os.getenv("MONGO_URL", "")

# ================== CHATBOT API ==================

API_URL = os.getenv("API_URL", "")

# ================== OWNER ==================

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# ================== VALIDATION ==================

if not API_ID:
    raise ValueError("API_ID is missing")

if not API_HASH:
    raise ValueError("API_HASH is missing")

if not STRING_SESSION:
    raise ValueError("STRING_SESSION is missing")

if not MONGO_URL:
    raise ValueError("MONGO_URL is missing")

if not API_URL:
    raise ValueError("API_URL is missing")

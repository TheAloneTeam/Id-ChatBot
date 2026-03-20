import os
import httpx
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import enums, filters
from pyrogram.types import Message

from MeowChat import app
from MeowChat.utils.admins import admin_check
from config import API_URL, MONGO_URL 

# ================== DATABASE ==================

mongo = AsyncIOMotorClient(MONGO_URL)
db = mongo["chatbot"]
col = db["status"]

# ================== PROMPT ==================


def load_prompt():
    try:
        path = os.path.join(os.path.dirname(__file__), "prompt.txt")
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return ""


PROMPT = load_prompt()

# ================== STATUS ==================


async def is_enabled(chat_id: int) -> bool:
    data = await col.find_one({"chat_id": chat_id})
    return data.get("enabled", False) if data else False


# ================== TOGGLE ==================


@app.on_message(filters.command("chatbot"))
async def toggle_chatbot(client, message: Message):
    chat_id = message.chat.id

    # Only group
    if message.chat.type not in [
        enums.ChatType.GROUP,
        enums.ChatType.SUPERGROUP,
    ]:
        return await message.reply_text("❌ This works only in groups")

    # Admin check
    if not await admin_check(message):
        return await message.reply_text("❌ You are not admin")

    current = await is_enabled(chat_id)
    new = not current

    await col.update_one(
        {"chat_id": chat_id},
        {"$set": {"enabled": new}},
        upsert=True,
    )

    status = "ON ✅" if new else "OFF ❌"
    await message.reply_text(f"🤖 Chatbot is now {status}")


# ================== MAIN ==================


@app.on_message(filters.text & ~filters.command(["chatbot"]))
async def chatbot_reply(client, message: Message):
    chat_id = message.chat.id

    # Only reply if enabled in group
    if message.chat.type in [
        enums.ChatType.GROUP,
        enums.ChatType.SUPERGROUP,
    ]:
        if not await is_enabled(chat_id):
            return

    if not message.text:
        return

    final_text = f"{PROMPT}\nUser: {message.text}"
    payload = {"message": final_text}

    try:
        async with httpx.AsyncClient(timeout=10) as clientx:
            res = await clientx.post(API_URL, json=payload)

            if res.status_code == 200:
                data = res.json()
                reply = (
                    data.get("reply")
                    or data.get("response")
                    or data.get("message")
                    or "🤖 No response"
                )
            else:
                reply = "⚠️ API Error"

        await message.reply_text(reply)

    except Exception as e:
        print("Chatbot Error:", e)
        await message.reply_text("⚠️ Something went wrong")

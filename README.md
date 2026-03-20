🤖 MeowChat Userbot

A powerful Telegram Userbot AI Chatbot built with Pyrogram + MongoDB + API system.

---

🚀 Features

- 🤖 AI Chatbot (API based replies)
- 👤 Runs on your Telegram account (Userbot)
- 🔄 "/chatbot" ON/OFF toggle system
- 👑 Admin / Owner control
- 💾 MongoDB database (chat status saving)
- ⚡ Fast async system (httpx + motor)
- 🧠 Custom prompt support ("prompt.txt")
- 🔐 Secure config system ("config.py")
- 🚀 Heroku deploy ready

---

📦 Requirements

- Python 3.10+
- MongoDB Database (Atlas recommended)
- Telegram API ID & API Hash
- Pyrogram String Session

---

🔐 Environment Variables

API_ID=your_api_id
API_HASH=your_api_hash
STRING_SESSION=your_string_session
MONGO_URL=your_mongo_url
API_URL=your_chatbot_api
OWNER_ID=your_telegram_id

---

🔑 Generate STRING_SESSION

pip install pyrogram tgcrypto
python3

from pyrogram import Client

api_id = int(input("API_ID: "))
api_hash = input("API_HASH: ")

with Client("session", api_id=api_id, api_hash=api_hash) as app:
    print(app.export_session_string())

---

🚀 Deploy to Heroku

🟣 One Click Deploy

""Deploy" (https://www.herokucdn.com/deploy/button.svg)" (https://dashboard.heroku.com/new?template=https://github.com/TheAloneTeam/Id-ChatBot)

---

🛠️ Manual Deploy

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

pip install -r requirements.txt
python main.py

---

📁 Project Structure

MeowChat/
├── plugins/
│   └── chatbot.py
├── utils/
│   └── admins.py
├── __init__.py
├── main.py
├── config.py
├── requirements.txt
├── Procfile
├── runtime.txt

---

💬 Commands

Command| Description
/chatbot| Enable / Disable chatbot

---

⚠️ Notes

- Works in groups
- Default OFF
- Only admin/owner can control
- Requires working API

---

🛡️ Disclaimer

This is a userbot. Use responsibly.

---

❤️ Credits

- Pyrogram
- MongoDB
- httpx

---

👑 Owner

Made with ❤️ by You

---

⭐ Support

Give a ⭐ if you like this project!

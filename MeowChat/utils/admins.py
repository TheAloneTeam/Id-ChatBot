from pyrogram import filters
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.types import Message

# ================== ADMIN CHECK ==================


async def admin_check(message: Message) -> bool:
    if not message.from_user:
        return False

    # Sirf groups me check hoga
    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.GROUP]:
        return False

    # Telegram system users allow
    if message.from_user.id in [
        777000,
        1087968824,
    ]:
        return True

    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [
            ChatMemberStatus.OWNER,
            ChatMemberStatus.ADMINISTRATOR,
        ]
    except Exception:
        return False


# ================== ADMIN FILTER ==================


async def admin_filter_func(filt, client, message):
    return await admin_check(message)


admin_filter = filters.create(func=admin_filter_func, name="AdminFilter")

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Oktavia.helper.basic import eor
from Oktavia.helper.tools import get_arg, eod
from Oktavia.helper import *


@Client.on_message(filters.command("info", ".") & filters.me)
async def infchat_users(c: Client, m: Message):
    kk = await eor(m, "`Processing...`")
    rep = m.reply_to_message
    if rep:
        input = rep.from_user.id
    else:
        input = get_arg(m)
    if not input:
        return await eod(m, "<code>Give id/username or reply to a user to get info.</code>")
    try:
        ok = (await c.get_users(input))
        username = f"@{ok.username}" if ok.username else "-"
        first_name = f"{ok.first_name}" if ok.first_name else "-"
        last_name = f"{ok.last_name}" if ok.last_name else "-"
        fullname = f"{ok.first_name} {ok.last_name}" if ok.last_name else ok.first_name
        kanjut = (await c.get_chat(input)).bio
        bio = f"{kanjut}" if kanjut else "-"
        h = f"{ok.status}"
        pp = await c.get_chat_photos_count(input)
        pp_count = f"{pp}" if pp else "-"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{ok.dc_id}" if ok.dc_id else "-"
        common = await c.get_common_chats(ok.id)
        out_str = f"""<b>USER INFORMATION:</b>
🆔 <b>User ID:</b> <code>{ok.id}</code>
🗣️ <b>First Name:</b> {first_name}
🗣️ <b>Last Name:</b> {last_name}
👤 <b>Username:</b> {username}
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🤖 <b>Is Bot:</b> <code>{ok.is_bot}</code>
🚷 <b>Is Scam:</b> <code>{ok.is_scam}</code>
🚫 <b>Restricted:</b> <code>{ok.is_restricted}</code>
✅ <b>Verified:</b> <code>{ok.is_verified}</code>
⭐ <b>Premium:</b> <code>{ok.is_premium}</code>
🖼️ <b>Profile Photos:</b> <code>{pp_count}</code>
📝 <b>User Bio:</b> <code>{bio}</code>
👀 <b>Same groups seen:</b> {len(common)}
👁️ <b>Last Seen:</b> <code>{status}</code>
🔗 <b>User permanent link:</b> <a href='tg://user?id={ok.id}'>{fullname}</a>
"""
        photo_id = ok.photo.big_file_id if ok.photo else None
        if photo_id:
            photo = await c.download_media(photo_id)
            await c.send_photo(m.chat.id, photo, caption=out_str)
            await kk.delete()
            os.remove(photo)
        else:
            await kk.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await eod(m, "`I can't extract thats id/username.`")


@Client.on_message(filters.command("cinfo", ".") & filters.me)
async def cinfo(c: Client, m: Message):
    kk = await eor(m, "`Processing...`")
    input = get_arg(m)
    if not input:
        return await eod(m, "`Give me a chat_id or chat username.`")
    try:
        ok = (await c.get_chat(input))
        h = f"{ok.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{ok.username}" if ok.username else "-"
        description = f"{ok.description}" if ok.description else "-"
        dc_id = f"{ok.dc_id}" if ok.dc_id else "-"
        out_str = f"""<b>CHAT INFORMATION:</b>
🆔 <b>Chat ID:</b> <code>{ok.id}</code>
👥 <b>Title:</b> {ok.title}
👥 <b>Username:</b> {username}
📩 <b>Type:</b> <code>{type}</code>
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🗣️ <b>Is Scam:</b> <code>{ok.is_scam}</code>
🎭 <b>Is Fake:</b> <code>{ok.is_fake}</code>
✅ <b>Verified:</b> <code>{ok.is_verified}</code>
🚫 <b>Restricted:</b> <code>{ok.is_restricted}</code>
🔰 <b>Protected:</b> <code>{ok.has_protected_content}</code>
🚻 <b>Total members:</b> <code>{ok.members_count}</code>
📝 <b>Description:</b>
<code>{description}</code>
"""
        photo_id = ok.photo.big_file_id if ok.photo else None
        if photo_id:
            photo = await c.download_media(photo_id)
            await c.send_photo(m.chat.id, photo, caption=out_str)
            await kk.delete()
            os.remove(photo)
        else:
            await kk.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await eod(m, "`Can't extract info from thats chat.`")
      

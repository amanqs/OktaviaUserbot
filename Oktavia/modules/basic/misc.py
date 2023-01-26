import asyncio
from datetime import datetime
from platform import python_version

from platform import python_version as yy
from pyrogram import __version__, filters, Client
from pyrogram import Client, filters, raw
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import UsernameInvalid, PeerIdInvalid
from config import ALIVE_TEXT
from Oktavia import START_TIME, StartTime, app
from Oktavia import SUDO_USER
from Oktavia.helper.PyroHelpers import ReplyCheck
from Oktavia.helper.basic import edit_or_reply
from Oktavia.modules.bot.inline import get_readable_time
from Oktavia.helper.tools import HAPP
from Oktavia.helper.pastebin import paste
from Oktavia.helper import s_paste
from Oktavia.helper import *

from Oktavia import *

from Oktavia.modules.help import add_command_help

if ALIVE_TEXT:
   txt = ALIVE_TEXT
else:
    txt = (
      f"** 𝗢𝗸𝘁𝗮𝘃𝗶𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁 **\n",
      f"**status**: [Admin]\n\n"
          f" **oktavia_version**: `0.1`\n"
          f" ping=results["ping"]"
          f" **peer_users: `13 users`"
          f" **oktavia_uptime**: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
          f" **Order**: [ᴀᴍᴀɴɢ](t.me/amwang)\n"  
    )

@Client.on_message(
    filters.command(["alive", "oktavia"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def alive(client: Client, message: Message):
    xx = await message.reply_text("🤖")
    try:
       await message.delete()
    except:
       pass
    send = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    xd = (f"{txt}")
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=xd,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(xd, disable_web_page_preview=True)


@Client.on_message(filters.command("open", ".") & filters.me)
async def open_file(client: Client, m: Message):
    xd = await edit_or_reply(m, "`Reading File!`")
    f = await client.download_media(m.reply_to_message)
    if f:
        _error = open(f, "r")
        _error_ = _error.read()
        _error.close()
        if len(_error_) >= 4096:
            await xd.edit("`Pasting to Spacebin!`")
            ext = "py"
            x = await s_paste(_error_, ext)
            s_link = x["url"]
            s_raw = x["raw"]
            pasted = f"**Pasted to Spacebin**\n**Link:** [Spacebin]({s_link})\n**Raw Link:** [Raw]({s_raw})"
            return await xd.edit(pasted, disable_web_page_preview=True)
        else:
            await xd.edit(f"**Output:**\n```{_error_}```")
    else:
        await edit_or_reply(m, "Balas ke File untuk membukanya!")
        os.remove(f)

@Client.on_message(filters.command("id", ".") & filters.me)
async def get_id(client: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID:** `{rep.audio.file_id}`\n"
            file_id += "**File Type:** `audio`"

        elif rep.document:
            file_id = f"**File ID:** `{rep.document.file_id}`\n"
            file_id += f"**File Type:** `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`\n"
            file_id += "**File Type**: `Photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID:** `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set:** `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji:** `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker:** `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker:** `False`\n"
            else:
                file_id += "**Sticker Set:** __None__\n"
                file_id += "**Sticker Emoji:** __None__"

        elif rep.video:
            file_id = f"**File ID:** `{rep.video.file_id}`\n"
            file_id += "**File Type:** `Video`"

        elif rep.animation:
            file_id = f"**File ID:** `{rep.animation.file_id}`\n"
            file_id += "**File Type:** `GIF`"

        elif rep.voice:
            file_id = f"**File ID:** `{rep.voice.file_id}`\n"
            file_id += "**File Type:** `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID:** `{rep.animation.file_id}`\n"
            file_id += "**File Type:** `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"  •  **Longitude:** `{rep.location.longitude}`\n"
            file_id += f"  •  **Latitude:** `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location:**\n"
            file_id += f"  •  **Longitude:** `{rep.venue.location.longitude}`\n"
            file_id += f"  •  **Latitude:** `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address:**\n"
            file_id += f"  •  **Title:** `{rep.venue.title}`\n"
            file_id += f"  •  **Detailed:** `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = f"👀 **Forwarded User ID:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **From User ID:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Message ID:** `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = f"👀 **Forwarded User ID:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **From User ID:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Message ID:** `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await edit_or_reply(message, user_detail)

    else:
        await edit_or_reply(message, f"👥 **Chat ID:** `{message.chat.id}`")

@Client.on_message(filters.command("sosmed", ".") & filters.me)
async def sosmed(client: Client, message: Message):
    Man = await message.edit("`Processing . . .`")
    link = get_arg(message)
    bot = "thisvidbot"
    if link:
        try:
            xnxx = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            xnxx = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
    async for sosmed in client.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await asyncio.gather(
            Man.delete(),
            client.send_video(
                message.chat.id,
                sosmed.video.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)


add_command_help(
    "misc",
    [
        [".alive", "Check if the bot is alive or not."],
        [".sosmed", "Download media tt,ig,fb,yt."],
        [".id", "Send id of what you replied to."],
        [".info", "Full info about a user."],
        [".cinfo", "Get info about group & channel"],
    ],
)



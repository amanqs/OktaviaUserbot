from Oktavia import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from pyrogram import __version__
from pyrogram import tgbot
from Oktavia.modules.bot import callback

@app.on_message(filters.command("start") & filters.private)
async def start(client, message, bot, msg):
   user = await bot.get_me()
    mention = user.mention
    buttons = [
        [
            InlineKeyboardButton(
                "☞︎︎︎ Cʀᴇᴀᴛᴇ Uʙᴏᴛ ☜︎︎︎", callback_data="multi_client")
        ],
        [
            InlineKeyboardButton(
                "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ", callback_data="help_or_command"), InlineKeyboardButton(
                "ᴀʙᴏᴜᴛ", callback_data="about")
        ],
    ]
    await bot.send_message(
        msg.chat.id,
        START.format(msg.from_user.mention, mention, __version__),
        reply_markup=InlineKeyboardMarkup(buttons)
    )
   
@callback("help_or_command")
async def added_to_group_msg(_, cq):
    await cq.answer(
        "Sedang Tahap Percobaan...",
        show_alert=True,
    )
      
      @callback("about")
async def added_to_group_msg(_, cq):
    await cq.answer(
        "Sedang Tahap Percobaan...",
        show_alert=True,
    )
      
      @callback("multi_client")
async def added_to_group_msg(_, cq):
    button = [
        [
            InlineKeyboardButton(
                text="SESSION 1",
                callback_data=f"session_1",
            ),
            InlineKeyboardButton(
                text="SESSION 2",
                callback_data=f"session_2",
            )
        ],
        [
            InlineKeyboardButton(
                text="SESSION 3",
                callback_data=f"session_3",
            ),
            InlineKeyboardButton(
                text="SESSION 4",
                callback_data=f"session_4",
            )
        ],
        [
            InlineKeyboardButton(
                text="SESSION 5",
                callback_data=f"session_5",
            ),
        ],
    ]
    await cq.message.reply(
        text="String Session Mana Yang Ingin Anda Buat ???",
        reply_markup=InlineKeyboardMarkup(button),
    )

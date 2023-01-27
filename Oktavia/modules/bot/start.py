from Oktavia import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("Hey Oktavia Userbot Assistant here")

@app.on_message(filters.command("buat") & filters.private)
async def start(client, message):
   await message.reply_text("Silahkan PM @amwang Untuk Panduan Membuat Userbot")

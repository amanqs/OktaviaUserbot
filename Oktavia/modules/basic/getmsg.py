

# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
# kenkan
# abdul
#
# All rights reserved.


import os

from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *

from Oktavia.helper.tools import get_arg
from Oktavia.modules.help import add_command_help


@Client.on_message(filters.command("copy", ".") & filters.me)
async def copy(client, message):
    await message.edit("Processing...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("There is an error")
    else:
        try:
            chat = str(link.split("/")[-2])
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("There is an error")
    anjing = dia.caption or None
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("There is an error")


@Client.on_message(filters.command("getmsg", ".") & filters.me)
async def getmsg(client, message):
    dia = message.reply_to_message
    if not dia:
        await message.edit("Please reply to the media...")
    anjing = dia.caption or None
    await message.edit("Take content....")
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("There is an error")


@Client.on_message(filters.command("take", ".") & filters.me)
async def take(client: Client, message: Message):
    dia = message.reply_to_message
    if not dia:
        await message.edit("There is an error")
    dia.caption or None
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.from_user.id, anu)
        await message.delete()
        os.remove(anu)


add_command_help(
    "copymsg",
    [
        [
            "copy [text/reply]",
            "Copy anything from the protected channel or picture timer.",
        ],
        [
            "getmsg [text/reply]",
            "Copy anything from protected bots",
        ],
    ],
)

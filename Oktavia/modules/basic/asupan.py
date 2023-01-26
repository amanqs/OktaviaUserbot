from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import *

from Oktavia.modules.help import add_command_help


@Client.on_message(filters.command("asupan", ".") & filters.me)
async def asupan(client: Client, message: Message):
    await gather(
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "tedeasupancache", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=message.id,
        ),
    )


add_command_help(
    "asupan",
    [
        [".asupan", "get asupan video."],
        [".bokep"], "kaming sun..."
    ],
)

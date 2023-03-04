import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from Oktavia.helper.utility import get_arg

from Oktavia.modules.help import add_command_help


@Client.on_message(filters.me & filters.command(["q", "quotly"], "."))
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**Please Reply to Message**")
    if message.reply_to_message:
        await message.edit("`Making a Quote . . .`")
        bot = "QuotLyBot"
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if not quotly:
                return await message.edit("**Failed to Create Quotly Sticker**")
            await message.delete()
            await message.reply_sticker(
                sticker=quotly.sticker.file_id,
                reply_to_message_id=message.reply_to_message.id
                if message.reply_to_message
                else None,
            )


add_command_help(
    "quotly",
    [
        ["q or .quotly", "To make an quote."],
        [
            "q <color> or .quotly <color>",
            "Make a message into a sticker with the custom background color given.",
        ],
    ],
)

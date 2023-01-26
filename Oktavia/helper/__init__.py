import os
import sys
from pyrogram import Client
from .pastebin import *


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Bot"])

async def join(client):
    try:
        await client.join_chat("About_db")
    except BaseException:
        pass

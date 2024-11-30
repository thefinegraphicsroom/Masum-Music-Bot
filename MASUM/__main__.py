import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from MASUM import LOGGER, app, userbot
from MASUM.core.call import Baby
from MASUM.misc import sudo
from MASUM.plugins import ALL_MODULES
from MASUM.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("MASUM.plugins" + all_module)
    LOGGER("MASUM.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Baby.start()
    try:
        await Baby.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("MASUM").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Baby.decorators()
    LOGGER("MASUM").info(
        "DROP YOUR GIRLFRIEND'S NUMBER AND SEXY PIC TO @ll_ALPHA_BABY_lll , @PURVI_SUPPORT FOR ANY ISSUES MADE BY MASUM"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("MASUM").info("Stopping DEEP Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

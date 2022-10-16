# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Cilik-PyroBot

from pyrogram import idle
from uvloop import install

from config import BOT_VER
from Cilik import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from Cilik.helpers.misc import create_botlog, git, heroku

MSG_ON = """
✅ **Bagaskara-Userbot Activated.**
**🏷️ Userbot Version -** `{}`
**Ketik** `.bagas` **untuk Mengecheck Bot**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("allfucek")
            await bot.join_chat("suka2bagas")
            await bot.join_chat("loveisfuckedup")
            await bot.join_chat("ybgskr_ex")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER)
                )
            except BaseException:
                pass
            LOGGER("Bagaskara").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Bagaskara").info(f"Bagaskara-Userbot v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Bagaskara").info("Starting Bagaskara-Userbot)
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())

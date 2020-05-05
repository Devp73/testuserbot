"""Log PMs
Check https://t.me/tgbeta/3505"""
import asyncio
from telethon import events
from telethon.tl import functions, types
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register


bot.storage.NO_PM_LOG_USERS = []


#@borg.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if BOTLOG and not sender.bot:
        chat = await event.get_chat()
        if chat.id not in bot.storage.NO_PM_LOG_USERS and chat.id != bot.uid:
            try:
                e = await bot.get_entity(int(BOTLOG_CHATID))
                fwd_message = await bot.forward_messages(
                    e,
                    event.message,
                    silent=True
                )
            except Exception as e:
                logger.warn(str(e))


#@borg.on(admin_cmd("nolog ?(.*)"))
@register(outgoing=True, pattern="^.nolog$")
async def approve_p_m(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if BOTLOG:
        if event.is_private:
            if chat.id not in bot.storage.NO_PM_LOG_USERS:
                bot.storage.NO_PM_LOG_USERS.append(chat.id)
                await event.edit("Won't Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()
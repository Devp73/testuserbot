#fix by @heyworld for OUB


from telethon.tl.types import InputMediaDice
import emoji
#from uniborg.util import admin_cmd
from emoji import emoticon
from userbot.events import register 
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, ALIVE_NAME



@register(outgoing=True, pattern="^.dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice(emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(emoticon))
        except:
            pass

        
CMD_HELP.update({
    "dice":
    ".dice\
\nUsage: hahaha just a magic."
})    

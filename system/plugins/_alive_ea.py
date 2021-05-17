# Copyright (C) 2021 KeinShin@Github.



#  Hello sur 
import time as t


from system.decorators import light
from system.Config import Variable
from system.Config.utils import  get_readable_time
ping = get_readable_time((t.time() - t.time()))
from system import (ALIVE_IMG, app, ALIVE_MESSAGE, OWNER, time, ttl, updates, self_hosted, MODE,      
ALIVE_IMG
)        # Easter OwO



@light.on(["alive", "black", "alv", f"{OWNER}"], sudo_ids=Variable.SUDO_IDS)
async def alive(client: Client, m: Message):
    if ALIVE_MESSAGE is not None:
      text = f"""ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ is ᴀᴡᴀᴋᴇɴᴇᴅ
      🇴‌🇼‌🇳‌🇪‌🇷‌-: {OWNER}
      ᴛɪᴍᴇ: {time}
      ᴄᴏᴍᴍᴀɴᴅs: {ttl}
      ᴘɪɴɢ: {ping}
      ᴜᴘᴅᴀᴛᴇꜱ: {updates}
      ꜱᴇʟꜰ ʜᴏꜱᴛᴇᴅ: {self_hosted}
      ᴍᴏᴅᴇ: {mode_type}
      """
    else:
      text = ALIVE_MESSAGE
    await app.send_document(m.chat.id, ALIVE_IMG, caption=text)

 

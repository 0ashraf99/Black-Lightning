 # Copyright (C) 2021 KeinShin@Github. All rights reserved


import asyncio
from pyrogram.raw.types.message import Message
from pyrogram.types import update
from system.datas_sqlite.afk_sqlite import get_afk, get_reason, update_afk, del_afk
from system.datas_sqlite import c, conn

from system import COMMAND_HELP, OWNER, light, HNDLR
from system.Config import Variable
from system import (
  app,
)

from pyrogram import filters



@light.on(["afk"])

async def _(client, message ):

    try:

     if get_afk():
         return
    except IndexError:
        pass

    try:
        txt = message.text
        reason = txt.split()[1:]
        reason=" ".join(reason)
    except IndexError:
        reason = "**Contact me when i'm back alive, till [AFK]**\n __This is an automated message__"
        
    update_afk("True", reason)
    
    await message.edit(f"**Afk update from now onwards i'll handle any kind of updates**\n\n**Reason** - {reason}")

@app.on_message(~filters.bot & (filters.mentioned | filters.private) & ~filters.user('keinshin'))
async def n(client, message):
  user = await app.get_me()
  usr = await app.get_users(user.id)
  if not get_afk():
    
    return


  ar = "**Contact me when i'm back alive, till [AFK]**\n __This is an automated message__"
  if get_reason() != ar:
        msg=f"""
**Hello User @{message.from_user.username}!
This is an automated message from my assistant because I'm [AFK]**

__I was Last online __ - {user.status}
**Reason for afk**:
 
    {get_reason()}
""" 
  else:
       msg = get_reason()
     
  await app.send_message(message.chat.id, text=msg, reply_to_message_id=message.message_id)


@app.on_message(filters.user(OWNER))
async def sed(client, message:Message):
     
    try:

     del_afk()
    
     msg=await app.send_message(message.chat.id, "**AFK BACK NORMAL [ONLINE]**" )
     await asyncio.sleep(1)
     await app.delete_messages(msg.chat.id, msg.message_id, revoke=True)
    except Exception:
        pass

COMMAND_HELP.update({
    "afk": f"`{HNDLR} afk` `(reason) or default`",
    "afk's help": "**USE**: __Creates an automated message by your bot when you are afk__"
})

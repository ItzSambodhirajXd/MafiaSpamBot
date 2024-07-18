from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from telethon import events, Button


data  = [
    Button.url("Channel", url="t.me/ABOUT_SAMBODHIRAJ"),
    Button.url("Repo", url="https://t.me/Team_Heartless_Fed"),
    Button.url("Group", url="https://t.me/+T7UFIlflxTE5ZWE1")
]


@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[•|| संबोधिराज ||•](tg://user?id={6721553082})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hey {mention},

𝐓𝐇𝐈𝐒 𝐈𝐒 𝐒𝐀𝐌𝐁𝐎𝐃𝐇𝐈𝐑𝐀𝐉 𝐎𝐏 𝐒𝐏𝐀𝐌𝐁𝐎𝐓 

𝐎𝐖𝐍𝐄𝐑:- {myOwner}

𝐒𝐔𝐃𝐎:- {sudo_user}

𝐂𝐑𝐄𝐀𝐓𝐎𝐑:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)


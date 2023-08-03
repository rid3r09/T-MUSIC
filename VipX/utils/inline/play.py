import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, GROUP_USERNAME, CHANNEL_USERNAME
from VipX import app

import config
from VipX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    vip = math.floor(percentage)
    if 0 < ᴛsᴇʀɪᴇs <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < ᴛsᴇʀɪᴇs < 3:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= ᴛsᴇʀɪᴇs < 4:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= ᴛsᴇʀɪᴇs < 5:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= ᴛsᴇʀɪᴇs < 7:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= ᴛsᴇʀɪᴇs < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= ᴛsᴇʀɪᴇs < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= ᴛsᴇʀɪᴇs < 12:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= ᴛsᴇʀɪᴇs < 13:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < ᴛsᴇʀɪᴇs < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= ᴛsᴇʀɪᴇs < 15:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= ᴛsᴇʀɪᴇs < 16:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= ᴛsᴇʀɪᴇs < 17:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= ᴛsᴇʀɪᴇs < 18:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= ᴛsᴇʀɪᴇs < 19:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= ᴛsᴇʀɪᴇs < 20:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= ᴛsᴇʀɪᴇs < 21:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= ᴛsᴇʀɪᴇs < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= ᴛsᴇʀɪᴇs < 23:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= ᴛsᴇʀɪᴇs < 24:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= ᴛsᴇʀɪᴇs < 25:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= ᴛsᴇʀɪᴇs < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= ᴛsᴇʀɪᴇs < 27:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= ᴛsᴇʀɪᴇs < 28:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= ᴛsᴇʀɪᴇs < 29:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= ᴛsᴇʀɪᴇs < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= ᴛsᴇʀɪᴇs < 31:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= ᴛsᴇʀɪᴇs < 32:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= ᴛsᴇʀɪᴇs < 33:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= ᴛsᴇʀɪᴇs < 34:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= ᴛsᴇʀɪᴇs < 35:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= ᴛsᴇʀɪᴇs < 36:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= ᴛsᴇʀɪᴇs < 37:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= ᴛsᴇʀɪᴇs < 38:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= ᴛsᴇʀɪᴇs < 39:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= ᴛsᴇʀɪᴇs < 40:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= ᴛsᴇʀɪᴇs < 41:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= ᴛsᴇʀɪᴇs < 42:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= ᴛsᴇʀɪᴇs < 43:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= ᴛsᴇʀɪᴇs < 44:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < vip < 45:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= ᴛsᴇʀɪᴇs < 46:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= ᴛsᴇʀɪᴇs < 47:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= ᴛsᴇʀɪᴇs < 48:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= ᴛsᴇʀɪᴇs < 49:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= ᴛsᴇʀɪᴇs < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= ᴛsᴇʀɪᴇs < 51:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= ᴛsᴇʀɪᴇs < 52:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= ᴛsᴇʀɪᴇs < 53:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= ᴛsᴇʀɪᴇs < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= ᴛsᴇʀɪᴇs < 55:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= ᴛsᴇʀɪᴇs < 56:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= ᴛsᴇʀɪᴇs < 57:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= ᴛsᴇʀɪᴇs < 58:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= ᴛsᴇʀɪᴇs < 59:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= ᴛsᴇʀɪᴇs < 60:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= ᴛsᴇʀɪᴇs < 61:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= ᴛsᴇʀɪᴇs < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= ᴛsᴇʀɪᴇs < 63:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= ᴛsᴇʀɪᴇs < 64:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= ᴛsᴇʀɪᴇs < 65:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= ᴛsᴇʀɪᴇs < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= ᴛsᴇʀɪᴇs < 67:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= ᴛsᴇʀɪᴇs < 68:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= ᴛsᴇʀɪᴇs < 69:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= ᴛsᴇʀɪᴇs < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= ᴛsᴇʀɪᴇs < 71:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= ᴛsᴇʀɪᴇs < 72:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= ᴛsᴇʀɪᴇs < 73:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= ᴛsᴇʀɪᴇs < 74:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= ᴛsᴇʀɪᴇs < 75:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= ᴛsᴇʀɪᴇs < 76:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 < vip < 77:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= ᴛsᴇʀɪᴇs < 78:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= ᴛsᴇʀɪᴇs < 79:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= ᴛsᴇʀɪᴇs < 80:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= ᴛsᴇʀɪᴇs < 81:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= ᴛsᴇʀɪᴇs < 82:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= ᴛsᴇʀɪᴇs < 83:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= ᴛsᴇʀɪᴇs < 84:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= ᴛsᴇʀɪᴇs < 85:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= ᴛsᴇʀɪᴇs < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= ᴛsᴇʀɪᴇs < 87:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= ᴛsᴇʀɪᴇs < 88:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= ᴛsᴇʀɪᴇs < 89:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= ᴛsᴇʀɪᴇs < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= ᴛsᴇʀɪᴇs < 91:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= ᴛsᴇʀɪᴇs < 92:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= ᴛsᴇʀɪᴇs < 93:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= ᴛsᴇʀɪᴇs < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= ᴛsᴇʀɪᴇs < 95:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= ᴛsᴇʀɪᴇs < 96:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= ᴛsᴇʀɪᴇs < 97:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= ᴛsᴇʀɪᴇs < 98:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= ᴛsᴇʀɪᴇs < 99:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"

        buttons  = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
          ],
          [
            InlineKeyboardButton(

                text="➤",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="➤➤┃", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="□", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="cℓσsε", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
                


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    vip = math.floor(percentage)
    if 0 < vip <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < vip < 3:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= ᴛsᴇʀɪᴇs < 4:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= ᴛsᴇʀɪᴇs < 5:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= ᴛsᴇʀɪᴇs < 7:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= ᴛsᴇʀɪᴇs < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= ᴛsᴇʀɪᴇs < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= ᴛsᴇʀɪᴇs < 12:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= ᴛsᴇʀɪᴇs < 13:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < vip < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= ᴛsᴇʀɪᴇs < 15:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= ᴛsᴇʀɪᴇs < 16:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= ᴛsᴇʀɪᴇs < 17:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= ᴛsᴇʀɪᴇs < 18:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= ᴛsᴇʀɪᴇs < 19:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= ᴛsᴇʀɪᴇs < 20:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= ᴛsᴇʀɪᴇs < 21:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= ᴛsᴇʀɪᴇs < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= ᴛsᴇʀɪᴇs < 23:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= ᴛsᴇʀɪᴇs < 24:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= ᴛsᴇʀɪᴇs < 25:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= ᴛsᴇʀɪᴇs < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= ᴛsᴇʀɪᴇs < 27:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= ᴛsᴇʀɪᴇs < 28:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= ᴛsᴇʀɪᴇs < 29:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= ᴛsᴇʀɪᴇs < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= ᴛsᴇʀɪᴇs < 31:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= ᴛsᴇʀɪᴇs < 32:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= ᴛsᴇʀɪᴇs < 33:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= ᴛsᴇʀɪᴇs < 34:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= ᴛsᴇʀɪᴇs < 35:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= ᴛsᴇʀɪᴇs < 36:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= ᴛsᴇʀɪᴇs < 37:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= ᴛsᴇʀɪᴇs < 38:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= ᴛsᴇʀɪᴇs < 39:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= ᴛsᴇʀɪᴇs < 40:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= ᴛsᴇʀɪᴇs < 41:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= ᴛsᴇʀɪᴇs < 42:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= ᴛsᴇʀɪᴇs < 43:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= ᴛsᴇʀɪᴇs < 44:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < vip < 45:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= ᴛsᴇʀɪᴇs < 46:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= ᴛsᴇʀɪᴇs < 47:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= ᴛsᴇʀɪᴇs < 48:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= ᴛsᴇʀɪᴇs < 49:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= ᴛsᴇʀɪᴇs < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= ᴛsᴇʀɪᴇs < 51:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= ᴛsᴇʀɪᴇs < 52:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= ᴛsᴇʀɪᴇs < 53:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= ᴛsᴇʀɪᴇs < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= ᴛsᴇʀɪᴇs < 55:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= ᴛsᴇʀɪᴇs < 56:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= ᴛsᴇʀɪᴇs < 57:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= ᴛsᴇʀɪᴇs < 58:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= ᴛsᴇʀɪᴇs < 59:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= ᴛsᴇʀɪᴇs < 60:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= ᴛsᴇʀɪᴇs < 61:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= ᴛsᴇʀɪᴇs < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= ᴛsᴇʀɪᴇs < 63:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= ᴛsᴇʀɪᴇs < 64:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= ᴛsᴇʀɪᴇs < 65:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= ᴛsᴇʀɪᴇs < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= ᴛsᴇʀɪᴇs < 67:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= ᴛsᴇʀɪᴇs < 68:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= ᴛsᴇʀɪᴇs < 69:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= ᴛsᴇʀɪᴇs < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= ᴛsᴇʀɪᴇs < 71:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= ᴛsᴇʀɪᴇs < 72:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= ᴛsᴇʀɪᴇs < 73:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= ᴛsᴇʀɪᴇs < 74:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= ᴛsᴇʀɪᴇs < 75:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= ᴛsᴇʀɪᴇs < 76:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 <= ᴛsᴇʀɪᴇs < 77:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= ᴛsᴇʀɪᴇs < 78:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= ᴛsᴇʀɪᴇs < 79:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= ᴛsᴇʀɪᴇs < 80:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= ᴛsᴇʀɪᴇs < 81:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= ᴛsᴇʀɪᴇs < 82:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= ᴛsᴇʀɪᴇs < 83:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= ᴛsᴇʀɪᴇs < 84:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= ᴛsᴇʀɪᴇs < 85:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= ᴛsᴇʀɪᴇs < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= ᴛsᴇʀɪᴇs < 87:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= ᴛsᴇʀɪᴇs < 88:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= ᴛsᴇʀɪᴇs < 89:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= ᴛsᴇʀɪᴇs < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= ᴛsᴇʀɪᴇs < 91:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= ᴛsᴇʀɪᴇs < 92:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= ᴛsᴇʀɪᴇs < 93:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= ᴛsᴇʀɪᴇs < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= ᴛsᴇʀɪᴇs < 95:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= ᴛsᴇʀɪᴇs < 96:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= ᴛsᴇʀɪᴇs < 97:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= ᴛsᴇʀɪᴇs < 98:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= ᴛsᴇʀɪᴇs < 99:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
        
        buttons  = [

        [

            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▶",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▶▶┃", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="□", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="cℓσsε", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
    
def stream_markup(_, videoid, chat_id):

    buttons  = [   

            [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▶",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▶▶┃", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="□", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],
        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="cℓσsε", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons

def telegram_markup(_, chat_id):
    buttons  = [   
        
            [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(
                text="▶",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▶▶┃", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="□", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),
            
            InlineKeyboardButton(

                text="cℓσsε", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],
    ]

    return buttons
## Search Query Inline

def track_markup(_, videoid, user_id, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="cℓσsε", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons
## Live Stream Markup

def livestream_markup(_, videoid, user_id, mode, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_3"],

                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text=_["CLOSEMENU_BUTTON"],

                callback_data=f"forceclose {videoid}|{user_id}",

            ),

        ]

    ]

    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text=_["CLOSE_BUTTON"],

                callback_data=f"forceclose {videoid}|{user_id}",

            ),

        ],

    ]

    return buttons
## Slider Query Markup

def slider_markup(

    _, videoid, user_id, query, query_type, channel, fplay

):

    query = f"{query[:20]}"

    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

          ],
          [
          
            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],

        [

            InlineKeyboardButton(

                text="◀",

                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["CLOSE_BUTTON"],

                callback_data=f"forceclose {query}|{user_id}",

            ),

            InlineKeyboardButton(

                text="▶",

                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",

            ),

        ],

    ]

    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 

            [

                [

                    InlineKeyboardButton(

                        text="✯ cℓσsε ✯", callback_data="close"

                    )

                ]    

            ]

        )

## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [

        [
            InlineKeyboardButton(

                text=_["S_B_5"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),
            ],
            [
            InlineKeyboardButton(

                text="▶",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▶▶┃", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="□", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [  

            InlineKeyboardButton(

                text="《10",

                callback_data=f"ADMIN 1|{chat_id}",

            ),

            

            InlineKeyboardButton(

                text="cℓσsε", callback_data=f"close",

            ),

            InlineKeyboardButton(

                text="10》",

                callback_data=f"ADMIN 2|{chat_id}",

            ),

        ],

    ]

    return buttons

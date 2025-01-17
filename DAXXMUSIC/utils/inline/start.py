from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, CallbackQuery
from pyrogram import filters

import config
from DAXXMUSIC import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="SUMMON ME",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="My Master", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="Commands", callback_data="settings_back_helper"),
        ],
    ]
    return buttons


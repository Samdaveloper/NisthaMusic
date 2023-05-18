import asyncio
import random
from Nistha.config import BOT_USERNAME, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


NISTHA_IMG = (
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",
"https://graph.org/file/e24ef6985e84cdc3857ec.jpg",

)





START_TEXT = """
ʜɪ ɢᴜʏꜱ, ɪ ᴀᴍ ᴠᴇʀʏ ʜɪɢʜʟʏ ᴀ.ɪ ᴀᴅᴠᴀɴᴄᴇᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ʙᴏᴛ.
ɪ' ᴍ ᴠᴇʀʏ ғᴀꜱᴛ ᴀɴᴅ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ !
"""

    
   

@Client.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(NISTHA_IMG),
        caption=(START_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("❤️‍🔥sᴜᴘᴘᴏʀᴛ ⨻ ᴥᴅ❤️‍🔥", url="https://t.me/{SUPPORT_GROUP}"),
            InlineKeyboardButton("🍃ᴜᴘᴅᴀᴛᴇs ⨻ ᴥᴅ🍃", url="https://t.me/{UPDATE_CHANNEL}")
        ],
        [
            InlineKeyboardButton("❣️ᴄᴏᴍᴍᴀɴᴅs ⨻ ᴥᴅ❣️", callback_data="help_cmd"),
            InlineKeyboardButton("💖ᴍᴀɪɴᴛᴀɪɴᴇʀ ⨻ ᴥᴅ💖", url="https://t.me/{OWNER_USERNAME}"),
        ]
   
     ]
  ),
)
    
    

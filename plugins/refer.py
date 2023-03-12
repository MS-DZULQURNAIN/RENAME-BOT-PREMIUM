from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["referral"]))
async def referral(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("Bagikan link mu" ,url=f"https://t.me/share/url?url=https://t.me/MsRenameBot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Bagikan referral lu ketemen lu ntar lu dapet 3GB Limit Upload\nPer Referral 3GB\n Link lu : https://t.me/MsRenameBot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    

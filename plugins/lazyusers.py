import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
token = os.environ.get('TOKEN','5945280153:AAFk_spFvichod71v4qFDZXgZAtAcNVt28g')
botid = token.split(':')[0]
ADMIN = int(os.environ.get("ADMIN", "5104293442"))

from helper.database import botdata, find_one, total_user,getid

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["pengguna"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	id = str(getid())
	ids = id.split(',')

	await message.reply_text(f"🄼🅂 𝗗🆉𝗨𝗟𝚀𝐔𝐑𝐍Λ𝐈𝐍\n\n**🌐SEMUA ID : {ids}\n🚹Total Pengguna : {total_user()}\n📝Total ubah nama : {total_rename}\n🆙Total Ukuran :- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("TUTUP", callback_data="cancel")]]) 
                             )

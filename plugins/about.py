import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**MS RENAME BOT📝**\n\nPemilik : <a href='https://t.me/MSDZULQURNAIN'>🄼🅂 𝗗🆉𝗨𝗟𝚀𝐔𝐑𝐍Λ𝐈𝐍</a>\nLanguage : Python3\nLibrary : Pyrogram 2.0\nTotal ubah nama : {total_rename}\nTotal ukuran : {humanbytes(int(total_size))}\n\n🄼🅂 𝗗🆉𝗨𝗟𝚀𝐔𝐑𝐍Λ𝐈𝐍",quote=True)

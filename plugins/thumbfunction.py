from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['lihatthumbnail']))
async def lihatthumbnail(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**Lu kaga punya thumbnail kocak😒**\n\nklik /pasangthumbnail buat pasang thumbnail😑")
	
	 
@Client.on_message(filters.private & filters.command(['hapusthumbnail']))
async def hapusthumbnail(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Thumbnail berhasil dihapus🗑**")
	
@Client.on_message(filters.private & filters.command(['pasangthumbnail']))
async def pasangthumbnail(client,message):
        await message.reply_text("**KIRIM FOTO LU BUAT THUMBNAIL**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Thumbnail berhasil disimpan**✅\n\nSilahkan kirim video dan pilih ubah nama/rename buat menerapkan thumbnail ini😘\n\nUntuk mengganti thumbnail hapus dulu thumbnail nya klik /hapusthumbnail trs pasang lagi klik /pasangthumbnail gituuuuu🔥")
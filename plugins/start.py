from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes

from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
import os

CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", ""))
bot_username = os.environ.get("BOT_USERNAME","")
log_channel = int(os.environ.get("LOG_CHANNEL", ""))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/MS-RENAME-BOT-03-10")



# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""**Halo {message.from_user.first_name} {message.from_user.last_name}❤** \n\nGW ADALAH **MS RENAME BOT📝**\n\n**Gw bisa rename/ubah nama extensi dari file/video lu, Gw juga support pasang thumbnail permanen🖼**\n\n**klik tombol tutorial kalo lu kaga paham⚠**"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("DEVELOPER 👤", url="https://t.me/MSDZULQURNAIN")],
                                      [InlineKeyboardButton("🄼🅂 ק𝙍♢JΞC†", url="https://t.me/MSPR0JECT"),
                                      InlineKeyboardButton("🄼🅂 Ꮥᴜקק♢ꭈׁׅ†", url='https://t.me/MsSUPP0RT')],
                                      [InlineKeyboardButton("TUTORIAL 💡", url="https://telegra.ph/MS-RENAME-BOT-03-10")]
                                      ]))
        return
    if id:
        if old == True:
            try:
                await client.send_message(id, "TEMEN LU DAH MAKE BOT GW👍")
                await message.reply_photo(photo=LAZY_PIC,
                                         caption=txt,
                                         reply_markup=InlineKeyboardMarkup(
                                             [[InlineKeyboardButton("DEVELOPER 👤", url="https://t.me/MSDZULQURNAIN")],
                                      [InlineKeyboardButton("🄼🅂 ק𝙍♢JΞC†", url="https://t.me/MSPR0JECT"),
                                      InlineKeyboardButton("🄼🅂 Ꮥᴜקק♢ꭈׁׅ†", url='https://t.me/MsSUPP0RT')],
                                      [InlineKeyboardButton("TUTORIAL 💡", url="https://telegra.ph/MS-RENAME-BOT-03-10")]
                                          ]))
            except:
                return
        else:
            await client.send_message(id, "Selamat tod lu menang 3GB Upload limit")
            _user_ = find_one(int(id))
            limit = _user_["uploadlimit"]
            new_limit = limit + 3145728000
            uploadlimit(int(id), new_limit)
            await message.reply_text(text=f"{txt}", reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("DEVELOPER 👤", url="https://t.me/MSDZULQURNAIN")],
                                      [InlineKeyboardButton("🄼🅂 ק𝙍♢JΞC†", url="https://t.me/MSPR0JECT"),
                                      InlineKeyboardButton("🄼🅂 Ꮥᴜקק♢ꭈׁׅ†", url='https://t.me/MsSUPP0RT')],
                                      [InlineKeyboardButton("TUTORIAL 💡", url="https://telegra.ph/MS-RENAME-BOT-03-10")]
                                          ]))
                                          
     
@Client.on_callback_query(filters.regex('tutup'))
async def tutup(bot,update):
        await update.message.delete()

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    fsub = CHANNEL
    user_id = message.from_user.id
    if fsub:
        try:
            await client.get_chat_member(fsub, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("Lu kaga subscribe channel gw njir‼ join semua channel dibawah ini baru bisa ya tod😏 ",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url="https://t.me/MSPR0JECT"),
					                      InlineKeyboardButton("🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url="https://t.me/MsSUPP0RT")],
					                     [InlineKeyboardButton("🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url="https://t.me/DZST0RE"),
					                      InlineKeyboardButton("🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url="https://t.me/TESTI_DZSTORE")],
					                     [InlineKeyboardButton("🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=f"https://t.me/{fsub}")]]))
            await client.send_message(log_channel,f"MS VIDEO EDITOR 💻,\n\n**ID** : `{user_id}`\n**Nama**: {message.from_user.first_name} {message.from_user.last_name}\n**Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("BATASI ANAK ANJ INI🚨", callback_data="ceasepower")]]))
            return

    try:
        bot_data = find_one(int(botid))
        prrename = bot_data['total_rename']
        prsize = bot_data['total_size']
        user_deta = find_one(user_id)
    except:
        await message.reply_text("ketik /about ya tod🤗")
    try:
        used_date = user_deta["date"]
        buy_date = user_deta["prexdate"]
        daily = user_deta["daily"]
        user_type = user_deta["usertype"]
    except:
        await message.reply_text(text=f"woy {message.from_user.first_name}🙂 **gw lagi beresin ini tod**\n\nJan pake akun nokos makanya njing☺\nBot kaga bisa kalo lu ngirim file spam dr akun nokos lu😒\n\nKalo lu bukan admin gw ada solusi nih {message.from_user.first_name }😗\n\nLu upgrade premium bae dah mending, dijamin langsung bisa ketik /premium buat upgrade premium❤\n\nAtau klik bae tombol dibawah ini👇",
                                  reply_markup=InlineKeyboardMarkup(
                                                                     [[InlineKeyboardButton("UPGRADE PREMIUM💎", callback_data='premium')]]))
        await message.reply_text(text=f"💻")
        return 

    c_time = time.time()

    if user_type == "GRATISAN":
        LIMIT = 600
    else:
        LIMIT = 50
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"___Bot ini bukan lu doang yg make ya tod`\n Tunggu {ltime} atau upgrade premium tanpa limit ketik___ /premium ___buat upgrade ke premium😗___", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        value = 3145728000
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - \
            int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% hari ini {humanbytes(limit)} Terdeteksi🔍\n\n  Ukuran file {humanbytes(file.file_size)}\n  Limit harian {humanbytes(used)}\n\nSisa **{humanbytes(remain)}** diakun lu\nmakanya lu upgrade premium tanpa limit", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("UPGRADE PREMIUM💎", callback_data="premium")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" Limit lu {humanbytes(limit)} Limit harian {humanbytes(used)} ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("UPGRADE PREMIUM💎", callback_data="premium")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""**Mau lu apain nih file?**\n\n**Nama file** :- {filename}\n**Ukuran file** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("UBAH NAMA📝", callback_data="rename")],
                    [InlineKeyboardButton("THUMBNAIL🖼", callback_data='thumbnail')],
                    [InlineKeyboardButton("BATAL🚪", callback_data='cancel')]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 3145728000)
                    usertype(message.from_user.id, "GRATISAN")

                    await message.reply_text(f'premium berakhir pada {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Kaga bisa upload file diatas 2GB, Upgrade premium tanpa limit upload ❗")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 3145728000)
                    usertype(message.from_user.id, "GRATISAN")

            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""**MAU LU APAIN NIH FILE?**\n\n**Nama file** :- {filename}\n**Ukuran file** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}\n**""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("UBAH NAMA📝", callback_data="rename")],
                    [InlineKeyboardButton("THUMBNAIL🖼", callback_data='thumbnail')],
                    [InlineKeyboardButton("BATAL🚪", callback_data='cancel')]]))
                    
                    
 
@Client.on_callback_query(filters.regex('xkembali'))
async def xkembali(bot,update):
        await update.message.edit(f"**MAU LU APAIN NIH FILE?**", reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("UBAH NAMA📝", callback_data="rename")],
                    [InlineKeyboardButton("THUMBNAIL🖼", callback_data='thumbnail')],
                    [InlineKeyboardButton("BATAL🚪", callback_data='cancel')]]))
                    
@Client.on_callback_query(filters.regex('thumbnail'))
async def encode(bot,update):
        taddthumb = "**PILIH MENU THUMBNAIL DIBAWAH INI🖼"
        addthumbbutton = InlineKeyboardMarkup([
                                              [InlineKeyboardButton("PASANG THUMBNAIL🖼", callback_data="pasangthumbnail")],
                                              [InlineKeyboardButton("HAPUS THUMBNAIL🗑", callback_data="hapusthumbnail")],
                                              [InlineKeyboardButton("LIHAT THUMBNAIL 👀", callback_data=" lihatthumbnail")],
                                              [InlineKeyboardButton("TUTUP", callback_data="tutup")]])
        await update.message.edit(text = taddthumb, reply_markup = addthumbbutton)
 
@Client.on_callback_query(filters.regex('pasangthumbnail'))
async def encode(bot,update):
        taddthumb = "___KIRIM FOTO LU BUAT THUMBNAIL DIBAWAH___\n\n[**CONTOH**](https://telegra.ph/file/00720c7690d7f5dbaa322.jpg)\n\nKALO GAPAHAM CHAT ADMIN DIBAWAH INI⬇"
        addthumbbutton = InlineKeyboardMarkup([
                                              [InlineKeyboardButton("ADMIN👤", url="https://t.me/MSDZULQURNAIN")],
                                              [InlineKeyboardButton("TUTUP", callback_data="tutup")]])
        await update.message.edit(text = taddthumb, reply_markup = addthumbbutton)
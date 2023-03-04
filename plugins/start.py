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

CHANNEL = os.environ.get('CHANNEL', "-100152957746")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 5104293442))
bot_username = os.environ.get("BOT_USERNAME","tlgrenamerbot")
log_channel = int(os.environ.get("LOG_CHANNEL", "-100152957746"))
token = os.environ.get('TOKEN', '5945280153:AAFk_spFvichod71v4qFDZXgZAtAcNVt28g')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/d052c0671e48ca6ca15be.jpg")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "selamat pagi 🌞️"
elif 12 <= currentTime.hour < 12:
    wish = 'selamat siang 🌝'
else:
    wish = 'selamat malam 🌚'

# -------------------------------


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    old = insert(int(message.chat.id))
    try:
        id = message.text.split(' ')[1]
    except:
        txt=f"""Halo {wish} {message.from_user.first_name }❤ \n\n
	GW ADALAH **MS VIDEO EDITOR💻**\n\nGw bisa ngedit video lu kaya **UBAH NAMA,ENCODE RESOLUSI,POTONG DURASI VIDEO,EXTRAC VIDEO KE AUDIO MP3,SPESIAL CUSTOM THUMBNAIL**"""
        await message.reply_photo(photo=LAZY_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup(
                                      [[InlineKeyboardButton("DEVELOPER 👤", url="https://t.me/MSDZULQURNAIN")],
                                      [InlineKeyboardButton("🄼🅂 ק𝙍♢JΞC†", url="https://t.me/MSPR0JECT"),
                                      InlineKeyboardButton("🄼🅂 Ꮥᴜקק♢ꭈׁׅ†", url='https://t.me/MsSUPP0RT')],
                                      [InlineKeyboardButton("TUTORIAL 💡", callback_data='tutor')]
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
                                      [InlineKeyboardButton("TUTORIAL 💡", callback_data='tutor')]
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
                                      [InlineKeyboardButton("TUTORIAL 💡", callback_data='tutor')]
                                          ]))
    
@Client.on_callback_query(filters.regex('tutor'))
async def tutor(bot,update):
        await event.answer(f'BLM ADA TUTOR TOD,LAGI MALES GW☺', alert=True)

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = CHANNEL
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
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
					                     [InlineKeyboardButton("🄹♢ɨ𝐍  🄲ΉΛ𝐍𝐍ΞꝈ", url=f"https://t.me/{fsub_channel}")]]))
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
        LIMIT = 300
    else:
        LIMIT = 50
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"```Bot ini bukan lu doang yg make ya tod`\n Tunggu {ltime} atau upgrade premium tanpa limit ketik /premium buat upgrade ke premium😗```", reply_to_message_id=message.id)
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
                    [InlineKeyboardButton("UBAH NAMA📝", callback_data="rename"),
                     InlineKeyboardButton("ENCODE RESOLISI♻", callback_data='encode')],
                    [InlineKeyboardButton("POTONG DURASI VIDEO✂", callback_data='trim'),
                     InlineKeyboardButton("EXTRAC AUDIO🎼", callback_data='extmp3')],
                    [InlineKeyboardButton("PASANG THUMBNAIL🖼", callback_data='addthumb')],
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
            await message.reply_text(f"""Mau lu apain nih file?**\n\n**Nama file** :- {filename}\n**Ukuran file** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}\n**Reply pesan ini trs kasi nama baru buat file nya👌**""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("UBAH NAMA📝", callback_data="rename"),
                     InlineKeyboardButton("ENCODE RESOLISI♻", callback_data='encode')],
                    [InlineKeyboardButton("POTONG DURASI VIDEO✂", callback_data='trim'),
                     InlineKeyboardButton("EXTRAC AUDIO🎼", callback_data='extmp3')],
                    [InlineKeyboardButton("PASANG THUMBNAIL🖼", callback_data='addthumb')],
                    [InlineKeyboardButton("BATAL🚪", callback_data='cancel')]]))
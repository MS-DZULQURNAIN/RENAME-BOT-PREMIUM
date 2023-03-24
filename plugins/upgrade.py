"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
QRIS = os.environ.get("QRIS", "https://telegra.ph/file/00720c7690d7f5dbaa322.jpg")

@Client.on_message(filters.private & filters.command(["premium"]))
async def premiumcm(bot,message):
        tcprem = "**GRATISAN**\nLIMIT HARIAN : 2GB\nHarga          : Rp.0\n\n**PREMIUM💎**\nLIMIT HARIAN : **UNLIMITED**\nHarga          : **Rp10.000** PerBulan\n                 🌏 **1$** / Month"""
        kcprem = InlineKeyboardMarkup([
        			[InlineKeyboardButton("Payment/Pembayaran💳", callback_data="pay")], 
        			[InlineKeyboardButton("ADMIN👤", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("BATAL",callback_data = "cancel")]])
        await message.reply_text(text = tcprem,reply_markup = kcprem)


@Client.on_callback_query(filters.regex('premium'))
async def premium(bot,update):
        tprem = "**GRATISAN**\nLIMIT HARIAN : 2GB\nHarga          : Rp.0\n\n**PREMIUM💎**\nLIMIT HARIAN : **UNLIMITED**\nHarga          : **Rp10.000** PerBulan\n                 🌏 **1$** / Month"""
        kprem = InlineKeyboardMarkup([
        			[InlineKeyboardButton("Payment/Pembayaran💳", callback_data="pay")], 
        			[InlineKeyboardButton("ADMIN👤", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("BATAL",callback_data = "cancel")]])
        await update.message.edit(text = tprem,reply_markup = kprem)

	
@Client.on_callback_query(filters.regex('pay'))
async def pay(bot,update):
        tpay = "**PILIH MENU PEMBAYARAN DIBAWAH**"
        kpay = InlineKeyboardMarkup([
        			[InlineKeyboardButton("INDONESIA🇮🇩", callback_data="payidn")], 
        			[InlineKeyboardButton("INTERNATIONAL🌏", callback_data="payint")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "premium")]])
        await update.message.edit(text = tpay,reply_markup = kpay)
	
@Client.on_callback_query(filters.regex('payid'))
async def payid(bot,update):
        tpayid = "**SCAN QRIS DIATAS⬆**\n\n**DANA** : `082137969411`\n\n**OVO** : `082137969411`\n\n**GO-PAY** : `082137969411`\n\n**LINK AJA** : `082137969411`\n\n**SHOPEE PAY** : `082137969411`\n\n**KIRIMKAN BUKTI TRANSFER KE ADMIN DIBAWAH INI**"
        kpayid = InlineKeyboardMarkup([
        			[InlineKeyboardButton("ADMIN💎", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "pay")]])
        await update.message.reply_photo(photo=QRIS, text = tpayid, reply_markup = kpayid)
	
@Client.on_callback_query(filters.regex('payint'))
async def payint(bot,update):
        tpayint = "**PAY PAL**\n__Please send to paypal__\n\nUsername : @gegepaypal10\n\n__With a nominal value of 1$__\n\n **SEND PROOF OF TRANSFER TO ADMIN⬇**"
        kpayint = InlineKeyboardMarkup([
        			[InlineKeyboardButton("ADMIN👤", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tpayint,reply_markup = kpayint)

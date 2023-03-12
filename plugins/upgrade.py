"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('premium'))
async def premium(bot,update):
        tprem = """**GRATISAN**
	    LIMIT HARIAN : 2GB
	    Harga          : Rp.0
	
	    **PREMIUM💎** 
	    LIMIT HARIAN : **UNLIMITED**
	    Harga          : **Rp10.000** /Bulan
	                🌏 **1$** / Month"""
	    kprem = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**Payment/Pembayaran💳**", callback_data="pay")], 
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("BATAL",callback_data = "cancel")]])
        await update.message.edit(text = tprem,reply_markup = kprem)
	

@Client.on_message(filters.private & filters.command(["premium"]))
async def premium(bot,message):
    	tprem = """**GRATISAN**
	    LIMIT HARIAN : 2GB
	    Harga          : Rp.0
	
    	**PREMIUM💎** 
	    LIMIT HARIAN : **UNLIMITED**
	    Harga          : **Rp10.000** /Bulan
	                🌏 **1$** / Month"""
	    kprem = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**Payment/Pembayaran💳**", callback_data="pay")], 
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("BATAL",callback_data = "cancel")]])
        await message.reply_text(text = tprem,reply_markup = kprem)
	
	
@Client.on_callback_query(filters.regex('pay'))
async def pay(bot,update):
        tpay = "**PILIH MENU PEMBAYARAN DIBAWAH**"
        kpay = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**INDONESIA🇮🇩**", callback_data="payidn")], 
        			[InlineKeyboardButton("**INTERNATIONAL🌏*", callback_data="payint")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "premium")]])
        await update.message.edit(text = tpay,reply_markup = kpay)
    
    
@Client.on_callback_query(filters.regex('payidn'))
async def payidn(bot,update):
        tpayidn = "**SILAHKAN PILIH METODE PEMBAYARAN**"
        kpayidn = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**DANA**", callback_data="dana"), 
        			 InlineKeyboardButton("**OVO**", callback_data="ovo"),
        			 InlineKeyboardButton("**GO-PAY**", callback_data="gopay")],
        			[InlineKeyboardButton("**LINK AJA**", callback_data="linkaja"),
        			 InlineKeyboardButton("**SHOPEE PAY**", callback_data="shopeepay")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "pay")]])
        await update.message.edit(text = tpayidn,reply_markup = kpayidn)
    
    
@Client.on_callback_query(filters.regex('dana'))
async def dana(bot,update):
        tdana = """**DANA**
        __Silakan kirim ke nomor :__
    
        082137969411 A/N SITXX HERXXXTI
    
        __Dengan nominal yg tertera Rp10.000__
    
        **KIRIMKAN BUKTI TF KE ADMIN⬇**"""
        kdana = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tdana,reply_markup = kdana)
	
	
@Client.on_callback_query(filters.regex('ovo'))
async def ovo(bot,update):
        tovo = """**OVO**
        __Silakan kirim ke nomor :__
    
        082137969411 A/N MUXXXAD SXX DZXXIN
    
        __Dengan nominal yg tertera Rp10.000__
    
        **KIRIMKAN BUKTI TF KE ADMIN⬇**"""
        kovo = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tovo,reply_markup = kovo)
	
	
@Client.on_callback_query(filters.regex('gopay'))
async def gopay(bot,update):
        tgopay = """**OVO**
        __Silakan kirim ke nomor :__
    
        082137969411 A/N MUXXXAD SXX DZXXIN
    
        __Dengan nominal yg tertera Rp10.000__
    
        **KIRIMKAN BUKTI TF KE ADMIN⬇**"""
        kgopay = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tgopay,reply_markup = kgopay)
	
	
@Client.on_callback_query(filters.regex('linkaja'))
async def linkaja(bot,update):
        tlinkaja = """**OVO**
        __Silakan kirim ke nomor :__
    
        082137969411 A/N MUXXXAD SXX DZXXIN
    
        __Dengan nominal yg tertera Rp10.000__
    
        **KIRIMKAN BUKTI TF KE ADMIN⬇**"""
        klinkaja = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tlinkaja,reply_markup = klinkaja)
	
	
@Client.on_callback_query(filters.regex('shopeepay'))
async def shopeepay(bot,update):
        tspay = """**OVO**
        __Silakan kirim ke nomor :__
    
        082137969411 A/N MUXXXAD SXX DZXXIN
    
        __Dengan nominal yg tertera Rp10.000__
    
        **KIRIMKAN BUKTI TF KE ADMIN⬇**"""
        kspay = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tspay,reply_markup = kspay)
	
	
@Client.on_callback_query(filters.regex('payint'))
async def payint(bot,update):
        tpayint = """**PAY PAL**
        __Please send to paypal__
    
        Username : @gegepaypal10
    
        __With a nominal value of 1$__
    
        **SEND PROOF OF TRANSFER TO ADMIN⬇**"""
        kpayint = InlineKeyboardMarkup([
        			[InlineKeyboardButton("**ADMIN👤**", url="https://t.me/MSDZULQURNAIN")],
        			[InlineKeyboardButton("KEMBALI",callback_data = "payidn")]])
        await update.message.edit(text = tpayint,reply_markup = kpayint)
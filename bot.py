import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5945280153:AAFk_spFvichod71v4qFDZXgZAtAcNVt28g")

API_ID = int(os.environ.get("API_ID", "15823382"))

API_HASH = os.environ.get("API_HASH", "016d5e115a06ddfb6121823d72ae4d8c")

STRING = os.environ.get("STRING", "BQCNhTeU9cEvr_0k8yl1x6nnokNXJrRp5rCkzsBxV6czeTlYFIf4YIOd2fq6A8Yyaz5UJp1gKcwGRS_XI77T5EujaQtKB9AUZVrEchOvaV6bg81MZdJu_7NVGkMyQpzhTHwecSO_5t-3uGpkUXbrcQqXDFFaS3uxJgXTRUoAZXBkbb3Y155n1FCJKl4mfO2nPvZHiz4NRoZHjgh6XNWOU3wsULwskh5HtsSKb2-nO4nMJmrVRLC_XDuNHrFLxnSlLMavbRsXOuYj7YQw2dNPmpgT949o1QnEwnVmYSnAl7clBsB4UQpMJFsFMNt8vle7pErVOAeE7ynJudNT3suKTouRAAAAATA9VkIA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    print("BOT TELAH AKTIF🔥🔥🔥")
    print("MS DZULQURNAIN") 
    bot.run()

import random
import discord
from get_code import collection_to_page
from dotenv import load_dotenv
import os
from flask import Flask,request
import threading

app = Flask(__name__)
bot = discord.Client(intents=discord.Intents.default())
load_dotenv()

file_temp={}
domain=os.getenv('DOMAIN')

@app.route('/')
def home():
    try:
        return file_temp[request.args.get('nonce')]
    except:
        return ''

@bot.event
async def on_message(message:discord.Message):
    if message.author==bot.user:
        return
    data=message.content
    if not data:
        return
    print(f'[{message.author}] {data}')
    data=data.split(' ')
    cmd=data[0]
    if cmd!='collection_download' and cmd!='cdl' :
        print("[Debug] Pass.")
        return
    if len(data)!=2:
        print("[Debug] Argument Error")
        return

    url=data[1]

    try:
        cname=url.split('/')[5]
        await message.channel.send(f'Preparing the collection \"{cname}\" ...')
        print("[Debug] Crawl Start")
        data=collection_to_page(url)
    except:
        await message.channel.send('This link is not minecraft planet collection :((')
        print("[Debug] Crawl Error")
        return

    nonce=random.randrange(100000000)
    if len(file_temp)==1000:
        file_temp={}
    file_temp[nonce]=data
    content=f'Hello, the collection \"{cname}\" is prepared!\nhttps://{domain}/?nonce={nonce}'
    print("[Debug] Crawl Successfully")
    await message.channel.send(content)

@bot.event
async def on_ready():
    id=os.getenv('ID')
    print(f'https://discord.com/oauth2/authorize?client_id={id}&permissions=0&scope=bot%20applications.commands')

if __name__=='__main__':
    t=threading.Thread(target=app.run)
    t.start()
    bot.run(os.getenv('TOKEN'))
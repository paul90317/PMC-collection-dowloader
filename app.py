import discord
import io
from get_code import collection_to_page
from dotenv import load_dotenv
import os

bot = discord.Client(intents=discord.Intents(messages=True,guilds=True))

def io_get(data:str):
    return io.BytesIO(data.encode('utf-8'))

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

    files=[]
    files.append(discord.File(io_get(data),filename='download.htm'))
    content=f'Hello, the collection \"{cname}\" is prepared!\nRun download.htm below with chrome!'
    print("[Debug] Crawl Successfully")
    await message.channel.send(content, files=files)
    

load_dotenv()

@bot.event
async def on_ready():
    id=os.getenv('ID')
    print(f'https://discord.com/oauth2/authorize?client_id={id}&permissions=0&scope=bot%20applications.commands')

bot.run(os.getenv('TOKEN'))
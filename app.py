import re
import discord
import io
from code_getter import get_collection
from dotenv import load_dotenv
import os

client = discord.Client()
re_url=re.compile('https?:\/\/[a-zA-Z0-9\-]+(\.[a-zA-Z0-9]+)*(\/\S*)?')
html_data=open('download.htm','r',encoding='utf-8').read()

def io_get(urls:list):
    return io.BytesIO(html_data.replace('{urls}',str(urls)).encode('utf-8'))

@client.event
async def on_ready():
    print('Login:', client.user)

@client.event
async def on_message(message:discord.Message):
    if message.author == client.user:
        return
    url=message.content
    if not url:
        return
    if not re_url.fullmatch(url):
        return

    try:
        cname=url.split('/')[5]
        await message.channel.send(f'Preparing the collection \"{cname}\" ...')
        dp,rp=get_collection(url)
    except:
        await message.channel.send('This link is unvalid :((')
        return

    files=[]
    files.append(discord.File(io_get(dp),filename='datapacks-download.htm'))
    files.append(discord.File(io_get(rp),filename='resourcepacks-download.htm'))
    content=f'Hello, the collection \"{cname}\" is prepared\n'
    await message.channel.send(content, files=files)

load_dotenv()

client.run(os.getenv('TOKEN'))
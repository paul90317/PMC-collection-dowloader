import re
import discord
import io
from code_getter import get_collection
from dotenv import load_dotenv
import os

client = discord.Client()
re_url=re.compile('https?:\/\/[a-zA-Z0-9\-]+(\.[a-zA-Z0-9]+)*(\/\S*)?')

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
        code_dp, code_rp,link_dp,link_rp=get_collection(url)
    except:
        await message.channel.send('This link is unvalid :((')
        return

    files=[]
    files.append(discord.File(io.BytesIO(code_dp.encode('utf-8')),filename='datapacks-download.bat'))
    files.append(discord.File(io.BytesIO(code_rp.encode('utf-8')),filename='resourcepacks-download.bat'))
    content=f'Hello, the collection \"{cname}\" is prepared\n'
    if link_dp!=''or link_dp!='':
        content+='I\'m sorry about that I can\'t download following content in this collection, you need to download it by your hand :((\n'
    if link_dp!='':
        content+=' - Datapacks\n'
        content+=link_dp
    if link_rp!='':
        content+=' - Resourcepacks\n'
        content+=link_rp
    content+='Download following files (.bat) and run them, it will downlaod files in the collection automatically'
    await message.channel.send(content, files=files)

load_dotenv()

client.run(os.getenv('TOKEN'))
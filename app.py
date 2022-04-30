import re
import discord
import io
from code_getter import get_collection
from dotenv import load_dotenv
import os

bot = discord.Client()
re_url=re.compile('https?:\/\/[a-zA-Z0-9\-]+(\.[a-zA-Z0-9]+)*(\/\S*)?')
html_data=open('download.htm','r',encoding='utf-8').read()

def io_get(urls:list):
    return io.BytesIO(html_data.replace('{urls}',str(urls)).encode('utf-8'))

@bot.event
async def on_message(message:discord.Message):
    if message.author==bot.user:
        return
    data=message.content
    if not data:
        return
    print(message.author,data)
    data=data.split(' ')
    cmd=data[0]
    if cmd!='collection_download' and cmd!='cdl' :
        print(True,"=> command pass")
        return
    if len(data)!=2:
        print(False,"=> argument error")
        return

    url=data[1]

    if not re_url.fullmatch(url):
        await message.channel.send(f'Please give me a link of minecraft planet collection.')
        print(False,"=> not url")
        return

    try:
        cname=url.split('/')[5]
        await message.channel.send(f'Preparing the collection \"{cname}\" ...')
        print(True,"=> crawl start ")
        dp,rp=get_collection(url)
        
    except:
        await message.channel.send('This link is not minecraft planet collection :((')
        print(False,"=> link is not minecraft planet collection ")
        return

    files=[]
    files.append(discord.File(io_get(dp),filename='datapacks-download.htm'))
    files.append(discord.File(io_get(rp),filename='resourcepacks-download.htm'))
    content=f'Hello, the collection \"{cname}\" is prepared\n'
    await message.channel.send(content, files=files)
    print(True,"=> crawl successfully")

load_dotenv()

@bot.event
async def on_ready():
    id=os.getenv('ID')
    print(f'https://discord.com/oauth2/authorize?client_id={id}&permissions=0&scope=bot%20applications.commands')

bot.run(os.getenv('TOKEN'))
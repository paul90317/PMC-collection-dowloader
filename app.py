import discord
from discord.ext import commands
import io
from get_code import collection_to_page
from dotenv import load_dotenv
import os
import nest_asyncio
import crawl
from parser import parser
nest_asyncio.apply()

bot = commands.Bot(command_prefix='/',intents=discord.Intents.default())

def io_get(data:str):
    return io.BytesIO(data.encode('utf-8'))

@bot.command()
async def cdl(ctx:commands.context.Context, url='https://www.planetminecraft.com/collection/147813/hello-world/'):
    print(f'[{ctx.author.name}] {url}')

    if not parser.collection(url):
        await ctx.send('This is not a minecraft planet collection link :((')
        print("[Debug] Crawl Error")
        return

    cname=url.split('/')[5]
    await ctx.send(f'Preparing the collection \"{cname}\" ...')
    print("[Debug] Crawl Start")
    data=collection_to_page(url)

    files=[]
    files.append(discord.File(io_get(data),filename='download.htm'))
    content=f'Hello, the collection \"{cname}\" is prepared!\nRun download.htm below with chrome!'
    print("[Debug] Crawl Successfully")
    await ctx.send(content, files=files)

@bot.event
async def on_ready():
    pass

if __name__=='__main__':
    load_dotenv()
    bot.run(os.getenv('TOKEN'))
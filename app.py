import discord
from discord.ext import commands
import io
from get_code import collection_to_page
from dotenv import load_dotenv
import os
import nest_asyncio
from parser import parser
nest_asyncio.apply()

bot = commands.Bot(command_prefix='/',intents=discord.Intents.all())

def io_get(data:str):
    return io.BytesIO(data.encode('utf-8'))

@bot.command()
async def cdl(ctx:commands.context.Context, url='https://www.planetminecraft.com/collection/147813/hello-world/'):
    print(f'[{ctx.author}] {url}')
    if not parser.collection(url):
        await ctx.channel.send('This is not a minecraft planet collection link :((')
        print("[Debug] Crawl Error")
        return

    print("[Debug] Crawl Start")
    data=collection_to_page(url)

    files=[discord.File(io_get(data),filename='download.htm')]
    content=f'{ctx.author.mention}, the collection {url} is prepared!\nDownload and run `download.htm` below with **chrome**!'
    print("[Debug] Crawl Successfully")
    await ctx.channel.send(content, files=files)

@bot.event
async def on_ready():
    pass

if __name__=='__main__':
    load_dotenv()
    bot.run(os.getenv('TOKEN'))
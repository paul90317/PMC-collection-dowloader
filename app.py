import discord
from discord.ext import commands
import io
from get_code import collection_to_page
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix='/',intents=discord.Intents.default())

def io_get(data:str):
    return io.BytesIO(data.encode('utf-8'))

@bot.command()
async def cdl(ctx:commands.context.Context, url:str):
    print(f'[{ctx.author.name}] {url}')
    try:
        cname=url.split('/')[5]
        await ctx.send(f'Preparing the collection \"{cname}\" ...')
        print("[Debug] Crawl Start")
        data=collection_to_page(url)
    except:
        await ctx.send('This link is not minecraft planet collection :((')
        print("[Debug] Crawl Error")
        return

    files=[]
    files.append(discord.File(io_get(data),filename='download.htm'))
    content=f'Hello, the collection \"{cname}\" is prepared!\nRun download.htm below with chrome!'
    print("[Debug] Crawl Successfully")
    await ctx.send(content, files=files)

@bot.event
async def on_ready():
    id=os.getenv('ID')
    print(f'https://discord.com/oauth2/authorize?client_id={id}&permissions=0&scope=bot%20applications.commands')

if __name__=='__main__':
    load_dotenv()
    bot.run(os.getenv('TOKEN'))
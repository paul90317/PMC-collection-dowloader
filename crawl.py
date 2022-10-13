from base64 import encode
import json
import urllib.request as client
from wsgiref import headers
from bs4 import BeautifulSoup as bfs
import aiohttp
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

async def get(url):
    stimeout =  aiohttp.ClientTimeout(total=None,sock_connect=0.2,sock_read=0.2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url,headers={
                'user-agent':user_agent,
                'accept':accept
            }) as res:
                data= await res.read()
                return data.decode(encoding='utf-8')
    except:
        return None

def is_collection(url:str):
    sp=url.split('/')
    if len(sp)>=4 and sp[2]=='www.planetminecraft.com'and sp[3]=='collection':
        return True
    return False

async def expand_collection(url:str):
    try:
        root_url='https://www.planetminecraft.com'
        data=await get(url)
        root = bfs(data, 'html.parser')
        root=root.find('ul',class_='resource_list grid')
        root=root.find_all('a',class_='r-title')
        data=[]
        for atag in root:
            data.append(root_url+atag['href'])
        return data
    except:
        return url

def is_datapack(url:str):
    temp=[d for d in url.split('/') if d!='']
    if len(temp)==4 and temp[1]=='www.planetminecraft.com'and temp[2]=='data-pack':
        return True
    return False

async def expand_datapack(url:str):
    try:
        root_url='https://www.planetminecraft.com'
        data=await get(url)
        if data==None:
            return None
        root = bfs(data, 'html.parser')
        temp=root.find('ul',class_='content-actions').find_all('a')
        data_packs=[root_url+d['href'] for d in temp]
        temp=root.find('div',class_='content-actions')
        if temp!=None:
            temp=temp.find_all('a')
            texture_packs=[root_url+d['href'] for d in temp]
        else:
            texture_packs=[]
        return data_packs,texture_packs
    except:
        return url

def is_texturepack(url:str):
    temp=[d for d in url.split('/') if d!='']
    if len(temp)==4 and temp[1]=='www.planetminecraft.com'and temp[2]=='texture-pack':
        return True
    return False

async def expand_texture(url:str):
    try:
        root_url='https://www.planetminecraft.com'
        data=await get(url)
        root = bfs(data, 'html.parser')
        temp=root.find('ul',class_='content-actions').find_all('a')
        return [root_url+d['href'] for d in temp]
    except:
        return url
    
def is_mirror(url:str):
    sp=url.split('/')
    if len(sp)>=7 and(sp[6]=='mirror'or sp[6]=='website')and sp[2]=='www.planetminecraft.com':
        return True
    return False

async def expand_mirror(url:str):
    try:
        data=await get(url)
        return [json.loads(data)['forward_url']]
    except:
        return url

def is_mediafire(url:str):
    sp=url.split('/')
    if len(sp)>=3 and sp[2]=='www.mediafire.com':
        return True
    return False

async def expand_mediafire(url:str):
    try:
        data=await get(url)
        root = bfs(data, 'html.parser')
        return [root.find('a',class_='input popsok')['href']]
    except:
        return url

def is_adfoc(url:str):
    sp=url.split('/')
    if len(sp)>=3 and sp[2]=='adfoc.us':
        return True
    return False

async def expand_adfoc(url:str):
    try:
        data=await get(url)
        root = bfs(data, 'html.parser')
        return [root.find('a',class_='skip')['href']]
    except:
        return url

def is_curseforge(url:str):
    temp=[d for d in url.split('/') if d!='']
    if len(temp)>=2 and temp[1]=='www.curseforge.com':
        try:
            int(temp[len(temp)-1])
            return True
        except:
            pass
    return False

async def expand_curseforge(url:str):
    url+='file'if url[len(url)-1]=='/' else '/file'
    return [url]

def is_ignore(url:str):
    temp=[u for u in url.split('/')if u!='']
    if len(temp)<2:
        return True
    domain=temp[1]
    if domain=='discord.com' or domain=='discord.gg' or (domain=='github.com'and len(temp)<=4)or domain=='youtu.be'or domain=='youtube.com'or domain=='www.youtube.com':
        return True
    return False


from ast import parse
import json
from types import NoneType
from bs4 import BeautifulSoup as bfs
import aiohttp
import typing
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

async def get(url:str)->str|None:
    stimeout = aiohttp.ClientTimeout(total=None,sock_connect=0.2,sock_read=0.2)
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

async def expand_collection(url:str)->str|list[str]:
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
        print(f'[Degug] Fail to crawl {url}')
        return url

async def expand_datapack(url:str)->str|tuple[list[str]]:
    try:
        root_url='https://www.planetminecraft.com'
        data=await get(url)
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
        print(f'[Degug] Fail to crawl {url}')
        return url

async def expand_texturepack(url:str)->str|list[str]:
    try:
        root_url='https://www.planetminecraft.com'
        data=await get(url)
        root = bfs(data, 'html.parser')
        temp=root.find('ul',class_='content-actions').find_all('a')
        return [root_url+d['href'] for d in temp]
    except:
        print(f'[Degug] Fail to crawl {url}')
        return url

async def expand_mirror(url:str)->str|list[str]:
    try:
        data=await get(url)
        return [json.loads(data)['forward_url']]
    except:
        print(f'[Degug] Fail to crawl {url}')
        return url

async def expand_mediafire(url:str)->str|list[str]:
    try:
        data=await get(url)
        root = bfs(data, 'html.parser')
        return [root.find('a',class_='input popsok')['href']]
    except:
        print(f'[Degug] Fail to crawl {url}')
        return url

async def expand_adfoc(url:str)->str|list[str]:
    try:
        data=await get(url)
        root = bfs(data, 'html.parser')
        return [root.find('a',class_='skip')['href']]
    except:
        print(f'[Degug] Fail to crawl {url}')
        return url

async def expand_curseforge(url:str)->str|list[str]:
    url+='file'if url[len(url)-1]=='/' else '/file'
    return [url]



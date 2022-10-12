import json
import urllib.request as client
from bs4 import BeautifulSoup as bfs

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

def expand_collection(url):
    root_url='https://www.planetminecraft.com'
    req=client.Request(url,headers={
        "user-agent":user_agent
    })

    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')

    root = bfs(data, 'html.parser')
    root=root.find('ul',class_='resource_list grid')
    root=root.find_all('a',class_='r-title')
    data=[]
    for atag in root:
        data.append(root_url+atag['href'])
    return data

def expand_datapack(url):
    root_url='https://www.planetminecraft.com'
    req=client.Request(url,headers={
        "user-agent":user_agent
    })

    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')

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

def expand_other(url):
    root_url='https://www.planetminecraft.com'
    req=client.Request(url,headers={
        "user-agent":user_agent
    })

    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')

    root = bfs(data, 'html.parser')
    temp=root.find('ul',class_='content-actions').find_all('a')
    return [root_url+d['href'] for d in temp]


def expand_mirror(url):
    req=client.Request(url,headers={
        "user-agent":user_agent
    })
    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')
    return [json.loads(data)['forward_url']]

def expand_mediafire(url):
    req=client.Request(url,headers={
        "user-agent":user_agent
    })
    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')
    root = bfs(data, 'html.parser')
    return [root.find('a',class_='input popsok')['href']]

def expand_adfoc(url):
    req=client.Request(url,headers={
        "user-agent":user_agent,
        'accept':accept
    })
    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')
    root = bfs(data, 'html.parser')
    return [root.find('a',class_='skip')['href']]


import json
import urllib.request as client
from bs4 import BeautifulSoup as bfs
def collection(url):
    root_url='https://www.planetminecraft.com'
    req=client.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    })

    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')

    root = bfs(data, 'html.parser')
    root=root.find('ul',class_='resource_list grid')
    root=root.find_all('a',class_='r-title')
    data=[]
    for atag in root:
        data+=[root_url+atag['href']]
    return data

def download(url):
    root_url='https://www.planetminecraft.com'
    req=client.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    })

    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')

    root = bfs(data, 'html.parser')

    dp=root_url+root.find('ul',class_='content-actions').find('a')['href']
    rp=root.find('div',class_='content-actions')
    if rp!=None:
        rp=root_url+rp.find('a')['href']

    return dp,rp

def mirror(url):
    req=client.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    })
    with client.urlopen(req) as res:
        data=res.read().decode('utf-8')
    return json.loads(data)['forward_url']

import crawl
import asyncio
import warnings
warnings.filterwarnings('ignore',category=DeprecationWarning)
html_data=open('download.htm','r',encoding='utf-8').read()

def collection_classify(url:str):
    dps=[]
    tps=[]
    ots=[]
    tasks=[]
    tasks.append(asyncio.ensure_future(crawl.expand_collection(url)))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    packs=tasks[0].result()
    if type(packs)==str:
        return dps,tps,ots
    for url in packs:
        if crawl.is_datapack(url):
            dps.append(url)
        elif crawl.is_texturepack(url):
            tps.append(url)
        else:
            ots.append(url)
    for _ in range(5):
        dps2=[]
        tasks=[]
        for url in dps:
            if crawl.is_datapack(url):
                tasks.append(asyncio.ensure_future(crawl.expand_datapack(url)))
            elif crawl.is_curseforge(url):
                tasks.append(asyncio.ensure_future(crawl.expand_curseforge(url)))
            elif crawl.is_adfoc(url):
                tasks.append(asyncio.ensure_future(crawl.expand_adfoc(url)))
            elif crawl.is_mediafire(url):
                tasks.append(asyncio.ensure_future(crawl.expand_mediafire(url)))
            elif crawl.is_mirror(url):
                tasks.append(asyncio.ensure_future(crawl.expand_mirror(url)))
            elif crawl.is_ignore(url):
                ots.append(url)
            else:
                dps2.append(url)
        if len(tasks)==0:
            break
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        for t in tasks:
            data=t.result()
            if type(data)==str:
                dps2.append(data)
            elif type(data)==tuple:
                dp,tp=data
                dps2+=dp
                tps+=tp
            else:
                dps2+=data
        dps=dps2
        
    for _ in range(5):
        tps2=[]
        tasks=[]
        for url in tps:
            if crawl.is_texturepack(url):
                tasks.append(asyncio.ensure_future(crawl.expand_texture(url))) 
            elif crawl.is_curseforge(url):
                tasks.append(asyncio.ensure_future(crawl.expand_curseforge(url))) 
            elif crawl.is_adfoc(url):
                tasks.append(asyncio.ensure_future(crawl.expand_adfoc(url))) 
            elif crawl.is_mediafire(url):
                tasks.append(asyncio.ensure_future(crawl.expand_mediafire(url))) 
            elif crawl.is_mirror(url):
                tasks.append(asyncio.ensure_future(crawl.expand_mirror(url))) 
            elif crawl.is_ignore(url):
                ots.append(url)
            else:
                tps2.append(url)
        if len(tasks)==0:
            break
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        for t in tasks:
            data=t.result()
            if type(data)==str:
                tps2.append(data)
            else:
                tps2+=data
        tps=tps2
       
    return dps,tps,ots
    

def collection_to_page(url):
    dps,tps,ots=collection_classify(url)
    data=html_data
    data=data.replace('collection_name',url,-1)
    data=data.replace('[\'data_packs\']',str(dps))
    data=data.replace('[\'texture_packs\']',str(tps))
    data=data.replace('[\'others\']',str(ots))
    return data

if __name__=='__main__':
    with open('out.htm','w') as f:
        data=collection_to_page('https://www.planetminecraft.com/collection/147813/hello-world/')
        f.write(data)



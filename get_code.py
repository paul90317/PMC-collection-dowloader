import crawl

html_data=open('download.htm','r',encoding='utf-8').read()

def collection_classify(url:str):
    packs=crawl.expand_collection(url)
    dps=[]
    tps=[]
    ots=[]
    for url in packs:
        if crawl.is_datapack(url):
            dps.append(url)
        elif crawl.is_texturepack(url):
            tps.append(url)
        else:
            ots.append(url)
    for iii in range(5):
        nochange=True
        dps2=[]
        for url in dps:
            if crawl.is_datapack(url):
                dp,tp=crawl.expand_datapack(url)
                dps2+=dp
                tps+=tp
                if dp[0]!=url:
                    nochange=False
            elif crawl.is_curseforge(url):
                dp=crawl.expand_curseforge(url)
                dps2+=dp
                nochange=False
            elif crawl.is_adfoc(url):
                dp=crawl.expand_adfoc(url)
                dps2+=dp
                if dp[0]!=url:
                    nochange=False
            elif crawl.is_mediafire(url):
                dp=crawl.expand_mediafire(url)
                dps2+=dp
                if dp[0]!=url:
                    nochange=False
            elif crawl.is_mirror(url):
                dp=crawl.expand_mirror(url)
                dps2+=dp
                if dp[0]!=url:
                    nochange=False
            elif crawl.is_ignore(url):
                ots.append(url)
            else:
                dps2.append(url)
        dps=dps2
        if nochange:
            break
        
    for iii in range(5):
        nochange=True
        tps2=[]
        for url in tps:
            if crawl.is_texturepack(url):
                tp=crawl.expand_texture(url)
                tps2+=tp
                if tp[0]!=url:
                    nochange=False
            elif crawl.is_curseforge(url):
                tp=crawl.expand_curseforge(url)
                tps2+=tp
                nochange=False
            elif crawl.is_adfoc(url):
                tp=crawl.expand_adfoc(url)
                tps2+=tp
                if tp[0]!=url:
                    nochange=False
            elif crawl.is_mediafire(url):
                tp=crawl.expand_mediafire(url)
                tps2+=tp
                if tp[0]!=url:
                    nochange=False
            elif crawl.is_mirror(url):
                tp=crawl.expand_mirror(url)
                tps2+=tp
                if tp[0]!=url:
                    nochange=False
            elif crawl.is_ignore(url):
                ots.append(url)
            else:
                tps2.append(url)
        tps=tps2
        if nochange:
            break
       
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



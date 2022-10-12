from tempfile import TemporaryFile
import crawl

html_data=open('download.htm','r',encoding='utf-8').read()

def collection_to_page(collection_link):
    def classify_projects(links):
        ret={}
        for link in links:
            key=link.split('/')[3]
            if key not in ret:
                ret[key]=[link]
            else:
                ret[key].append(link)
        return ret

    data=crawl.expand_collection(collection_link)
    data=classify_projects(data)
    data_packs=[]
    texture_packs=[]

    if 'data-pack' in data:
        for link in data['data-pack']:
            data_pack,texture_pack=crawl.expand_datapack(link)
            data_packs+=data_pack
            texture_packs+=texture_pack
    if 'texture-pack' in data:
        for link in data['texture-pack']:
            texture_packs+=crawl.expand_other(link)

    others=[]
    for key in data:
        if key=='data-pack'or key=='texture-pack':
            continue
        others+=data[key]

    temp=data_packs
    data_packs=[]
    for link in temp:
        key=link.split('/')[6]
        if key=='file':
            data_packs+=[link]
        else:
            data_pack=crawl.expand_mirror(link)
            domain=data_pack[0].split('/')[2]
            if domain=='www.mediafire.com':
                data_packs+=crawl.expand_mediafire(data_pack[0])
            elif domain=='adfoc.us':
                data_packs+=crawl.expand_adfoc(data_pack[0])
            else:
                data_packs+=data_pack
            

    temp=texture_packs
    texture_packs=[]
    for link in temp:
        key=link.split('/')[6]
        if key=='file':
            texture_packs+=[link]
        else:
            texture_pack=crawl.expand_mirror(link)
            domain=texture_pack[0].split('/')[2]
            if domain=='www.mediafire.com':
                texture_packs+=crawl.expand_mediafire(texture_pack[0])
            elif domain=='adfoc.us':
                texture_packs+=crawl.expand_adfoc(texture_pack[0])
            else:
                texture_packs+=texture_pack

    data=html_data
    data=data.replace('collection_name',collection_link,-1)
    data=data.replace('[\'data_packs\']',str(data_packs))
    data=data.replace('[\'texture_packs\']',str(texture_packs))
    data=data.replace('[\'others\']',str(others))
    return data

if __name__=='__main__':
    with open('out.htm','w') as f:
        data=collection_to_page('https://www.planetminecraft.com/collection/147813/hello-world/')
        f.write(data)



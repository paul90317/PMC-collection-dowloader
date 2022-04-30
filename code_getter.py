import crawl


def get_collection(url):
    def url_get(url):
        mir=False
        if not url:
            return mir,None
        data=url.split('/')
        url_type=data[6]
        if url_type=='mirror':
            mir=True
            url=crawl.mirror(url)
        
        return mir,url

    dl_dp=[]
    mir_dp=[]
    dl_rp=[]
    mir_rp=[]
    urls=crawl.collection(url)
    for url in urls:
        dp,rp=crawl.download(url)
        mir,url=url_get(dp)
        if url:
            if(mir):
                mir_dp.append(url)
            else:
                dl_dp.append(url)
        mir,url=url_get(rp)
        if url:
            if(mir):
                mir_rp.append(url)
            else:
                dl_rp.append(url)

    return dl_dp+mir_dp,dl_rp+mir_rp
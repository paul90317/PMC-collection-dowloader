import crawl


def get_collection(url):
    def code_gen(url):
        if not url:
            return None
        data=url.split('/')
        data=[data[6],data[4]]
        if data[0]=='mirror':
            data[0]='link'
            data[1]=crawl.mirror(url)
        else:
            data[0]='code'
            data[1]=f'curl {url} -o {data[1]}.zip'
        return data

    code_dp=''
    link_dp=''
    code_rp=''
    link_rp=''
    urls=crawl.collection(url)
    for url in urls:
        dp,rp=crawl.download(url)
        temp=code_gen(dp)
        if temp:
            if(temp[0]=='code'):
                code_dp+=temp[1]+'\n'
            else:
                link_dp+=temp[1]+'\n'
        temp=code_gen(rp)
        if temp:
            if(temp[0]=='code'):
                code_rp+=temp[1]+'\n'
            else:
                link_rp+=temp[1]+'\n'

    return code_dp, code_rp,link_dp,link_rp
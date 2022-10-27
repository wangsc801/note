from bs4 import BeautifulSoup
from datetime import datetime
import requests

def practice(url,file=False):
    headers={
        'User-Agent':'Mozzila 5.0 (Windows NT 6.1; rv:86.0) Gecko 20100101 Firefox 86.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
    }
    session=requests.Session()
    req=session.get(url,headers=headers)
    bs=BeautifulSoup(req.text,'html.parser')
    content=bs.find('div',{'class':'con4'})

    if file==True:
        filename=f"scrape_{datetime.strftime(datetime.now(),'%Y-%m-%d_%H%M%S')}.txt"
        for a in content.findAll('a',href=True):
            with open(filename,'wt',encoding='utf-8') as txt:
                txt.write(a['href']+'\n')
    else:
        for a in content.findAll('a',href=True):
            print(a['href'])

practice('http://quanji456.com/Zuixinmeiju/LCZXDYJ69334/',False)

# I got banned
#
# requests.exceptions.ConnectionError: 
# ('Connection aborted.', ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None))

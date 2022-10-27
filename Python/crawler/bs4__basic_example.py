import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}
url='https://www.runoob.com/w3cnote/python-spider-intro.html'
request = session.get(url,headers=headers)
bs = BeautifulSoup(request.text, 'html.parser')
found = bs.findAll('h3')


with open('basic_bs_result.txt', 'wt', encoding='utf-8') as f:
    for i in found:
        f.write(str(i))

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.gov.cn/')
bs = BeautifulSoup(html.read(), 'html.parser')
info = bs.findAll('div', {'class': 'column1'})

for i in info:
    info_text = i.get_text()
    print(info_text)

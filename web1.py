

import requests
from bs4 import BeautifulSoup

res = requests.get('http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs2&word=%E5%A3%81%E7%BA%B8&oriquery=%E5%9B%BE%E7%89%87&ofr=%E5%9B%BE%E7%89%87&sensitive=0')
res.encoding = 'utf-8'
print(res.text)

# soup=BeautifulSoup(res.text,'html.parser')

# print(soup.text)

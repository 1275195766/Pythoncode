import requests
from bs4 import BeautifulSoup
import re
url = 'http://news.qq.com/original/oneday/cod3070.html'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
r = requests.get(url,headers=headers)
# print(r.status_code)
soup = BeautifulSoup(r.content,"html.parser")
# print(soup)
img=soup.select('div.tmpcontent script')
print(img[0].string)
img=img[0].string
rec=re.compile(r'//img1.gtimg.com/ninja.*?\.jpg')
img_url=rec.findall(img)
# for i in img_url:
#     print(i)
print(img_url)
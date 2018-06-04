import urllib.request #网页请求模块
from bs4 import BeautifulSoup #是用Python写的一个HTML/XML的解析器

url="http://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD&from=home#%E5%85%A8%E9%83%A8%2613"
data=urllib.request.urlopen(url).read()

soup=BeautifulSoup(data,'html.parser')
print(soup.prettify())
imgurl=soup.find_all('img')
print(imgurl)
import urllib
from urllib import request
from bs4 import BeautifulSoup
import re
url="https://list.jd.com/list.html?cat=670,671,672"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"}
req=request.Request(url,headers=headers)

page_info=request.urlopen(req).read()
soup=BeautifulSoup(page_info,'html.parser')
# print(soup.prettify())
srcs=soup.find_all('img',attrs={"data-img":"1"} )
print(srcs)
x=1
for src in srcs:
    imagename=r"H:\Pythoncode\新建文件夹"+str(x)+".jpg"
    imageurl="http//"+str(src.get('data-lazy-img'))
    try:
        request.urlretrieve(imageurl,filename=imagename)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
                x+=1
        if hasattr(e,"reason"):
                x+=1
    x+=1
    print(src.get("src"))


from urllib import request
import urllib.parse
from bs4 import BeautifulSoup
import re
url="http://tieba.baidu.com/f?kw=nani%E5%B0%8F%E8%A7%86%E9%A2%91&red_tag=b1595315325"
# postdata=urllib .parse.urlencode({"name":"15523270926","password":"hj19971109"}).encode('utf-8')
req=request.Request(url)
req.add_headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400")

page_info=request.urlopen(req).read()

soup=BeautifulSoup(page_info,'html.parser')
# print(soup.prettify())

titles=soup.find_all('a',class_=re.compile("j_th_tit "))
print(titles)
# for title in titles:
#     print(title.get_text())
#     print("https://tieba.baidu.com/"+title.get("href"))
    # re_ht=re.compile(pat)
    # print(re_ht.search(str(title)))


#
# with open(r'H:\Pythoncode\新建文件夹\tieba.txt','w') as file:
#     for title in titles:
#         file.write(title.string+'\n')
#         file.write("https://tieba.baidu.com/"+title.get('href')+'\n\n')
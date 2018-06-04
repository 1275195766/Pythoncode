from urllib import request
from bs4 import BeautifulSoup
import re
url="http://tieba.baidu.com/f?kw=nani%E5%B0%8F%E8%A7%86%E9%A2%91&red_tag=b1595315325"
req=request.Request(url)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400")
data=request.urlopen(req).read()
soup=BeautifulSoup(data, 'html.parser')
print(soup.prettify())


titles=soup.find_all('a',class_=re.compile("j_th_tit "))
print(titles)




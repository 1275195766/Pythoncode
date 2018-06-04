
from urllib import request
from bs4 import BeautifulSoup
url="https://www.jianshu.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400"}
req=request.Request(url,headers=headers)
# req.add_headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400")

page_info=request.urlopen(req).read().decode('utf-8')
soup=BeautifulSoup(page_info,'html.parser')
print(soup.prettify())
titles=soup.find_all('a','title')
print(titles)
# for title in titles:
#     print(title.sting)
#     print("https://www.jianshu.com"+title.get('href'))
#
# with open(r'H:\Pythoncode\新建文件夹\articles1.txt','w') as file:
#     for title in titles:
#         file.write(title.string+'\n')
#         file.write("https://www.jianshu.com"+title.get('href')+'\n\n')
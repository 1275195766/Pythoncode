import  urllib.request
from bs4 import BeautifulSoup

url='https://www.qiushibaike.com/'
headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400")
opener=urllib.request.build_opener()
opener.addheaders=[headers]

urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()

soup=BeautifulSoup(data,'html.parser')

userlist=soup.find_all('h2')
for div in soup.find_all('div','content'):
    for span in div.find_all('span'):
        if span.string:
            print(span.string)
        else:
            continue

# print(userlist)
# for title in userlist:
#     print(title.string)
# for content in contentlist:
#     print(content.string)
import urllib.request
res=urllib.request.urlopen('http://news.sina.com.cn/china/')
print(res.read())

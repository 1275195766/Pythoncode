import urllib.request

url="http://www.baidu.com/s?wd="
key="名侦探柯南"
key_code=urllib.request.quote(key)
url_all=url+key_code
req=urllib.request.Request(url_all)
data=urllib.request.urlopen(req).read()
fd=open("H:/Pythoncode/webspider/5.html","wb")
fd.write(data)
fd.close()












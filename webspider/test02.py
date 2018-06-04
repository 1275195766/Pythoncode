import urllib.request
import urllib.parse
url="http://www.iqianyue.com/mypost/"
postdata=urllib.parse.urlencode({
    "name":"wuayaoxue2@qq.com",
    "pass":"124566"
}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
data=urllib.request.urlopen(url,postdata).read()
fh=open("H:/Pythoncode/webspider/6.html","wb")
fh.write(data)
fh.close()

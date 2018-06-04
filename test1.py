import urllib.request
import urllib.parse
import http.cookiejar
url="http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lh9Va"
postdate=urllib.parse.urlencode({"username":"Larry1275","password":"hj19971109"}).encode('utf-8')#使用urlencode处理后，在设置编码为utf-8
req=urllib.request.Request(url,postdate)#构建post对象
req.add_header('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
#使用HTTP.cookiejar.CookieJar（）创建CookieJar对象
cjar=http.cookiejar.CookieJar()
openr=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将openr安装为全局
urllib.request.install_opener(openr)
file=openr.open(req)
data=file.read()#登陆并爬取网页
file=open("H:\\Pythoncode\\新建文件夹\\3.html","wb")
file.write(data)#将内容写入对应文件
file.close()

url2="http://bbs.chinaunix.net/"
#req2=urllib.request.Request(url2,postdate)
#req2.add_header('User-Agent',' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
data2=urllib.request.urlopen(url2).read()
fhandle=open('H:\\Pythoncode\\新建文件夹\\4.html','wb')
fhandle.write(data)
fhandle.close()
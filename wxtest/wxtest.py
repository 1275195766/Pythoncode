import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" style'
    imgre = re.compile(reg)
    html=html.decode('utf-8')#python3
    imglist = re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    #return imglist

html = getHtml("https://tieba.baidu.com/p/2424801358#!/l/p1")
print (getImg(html))

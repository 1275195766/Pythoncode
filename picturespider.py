import urllib.request
import re
url="https://list.jd.com/list.html?cat=9987,653,655"
def craw(url,page):
    html1=urllib.request.urlopen(url).read()#用urllib.request.urlopen()打开网页，并保存到html1变量中
    html1=str(html1)#将网页转换成字符串

    pat1=r'<div id="plist".+?<div class="page clearfix">'#第一次过滤的正则表达式
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]#第一次过滤后的图片网址
    #print(result1)
    pat2=r'<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'#图片网址过滤的正则表达式
    imagelist=re.compile(pat2).findall(result1)#过滤后的图片网址
    x=1
    for imageurl in imagelist:
        imagename="H:\\Pythoncode\\picture\\"+str(page)+str(x)+".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(1,79):
    url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)

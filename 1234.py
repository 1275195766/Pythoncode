import requests
import re
def getNovelContent():
    response=requests.get("http://www.quanshuwang.com/book/0/742")
    response.encoding("gbk")
    html=response.text
    reg=r'<li><a href"(.*?)"title=".*?">(.*?)</a></li>'
    reg=re.compile(reg)
    urls=re.findall(reg,html)
    for url in urls:
        novel_url=url[0]
        novel_title=url[1]
        chapt=requests.get(novel_url)
        chapt.encoding="gbk"
        chapt_html=chapt.text
        reg=r'</script>&nbsp,&nbsp,&nbsp,&nbsp,(.*?)<scripttype="text/javascript">'
        reg=re.compile(reg,re.S)
        chapt_content=re.findall(reg,chapt_html)
        chapt_content=chapt_content[0].replace("&nbsp,&nbsp,&nbsp,&nbsp,","")
        chapt_content=chapt_content.replace("<br/>","")
        with open('H:\\Pythoncode\\{}.doc'.format(novel_title),'w')as f:
            f.write(chapt_content)
            




import urllib #网页请求模块
import requests #用于下载网页
import json #用于将网页转换成json对象
def get_url(tag,cate,len,path):
    url='http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag='+tag+'&start=1&len='+str(len)
    link=requests.get(url)
    jd=json.loads(link.text)
    url_list=jd['all_items']
    print(url_list)
    x=1
    for i in url_list:
        img_rul=i['pic_url']
        print(img_rul)
        try:
            urllib.request.urlretrieve(img_rul,path+str(x)+'.jpg')
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
get_url('动漫','壁纸',40,r'H:\picture\picture\ ')



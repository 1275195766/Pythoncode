import requests
import sys
import random
import urllib.request
url='https://image.baidu.com/search/acjson?'
#tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%8A%A8%E6%BC%AB%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E5%8A%A8%E6%BC%AB%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=30&rn=30&gsm=1e&1526398275525=
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'}
def get_page(data):
    try:
        page=requests.get(url,params=data,headers=header)
        page.encoding='utf-8'
        return page.json()
    except:
        return ''

def get_src(data,n):
    page_info=get_page(data)
    print(page_info)
    piclist=page_info['data']

    # print(piclist)
    for i in piclist[:-1]:
            # print(i)
            val=i['replaceUrl']
            print(val)
            for v in val:
                # print(v['ObjURL'])

                try:
                    fromsrc =v['FromURL']
                    objurl=v['ObjURL']
                    title = i['fromPageTitleEnc']
                    # print("fromsrc:"+fromsrc)
                    # print("objurl:"+objurl)
                    newsrc="http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&hs=0&pn="+str(n)+"&spn=0&di=97948933610&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3588772980%2C2454248748&os=1031665791%2C326346256&simid=0%2C0&adpicid=0&lpn=0&ln=1981&fr=&fmq=1526575070122_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl="+objurl+"&fromurl="+fromsrc

                    get_pic(title, newsrc)
                except:
                    # for k in v:

                    print('保存失败')
#
#
#
def get_pic(title,newsrc):
    print(newsrc,end='        ')#"http://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url="+newsrc+"&thumburl="+
    req=requests.get(newsrc,headers=header)
    print(req.status_code)

    with open(r'H:\Pythoncode\picture\\'+title+str(random.randint(0,20))+'.jpg',"wb") as file:
        file.write(req.content)
    # urllib.request.urlretrieve(newsrc,r'H:\Pythoncode\picture\\'+title+str(random.randint(0,9)))

if __name__=="__main__":
    word='图片'
    data={'tn':'resultjson_com',
          'ipn':'rj',
          'ct':'201326592',
          'fp':'result',
          'word':word,
          'pn':0,
          'rn':30
         #  'width':1920,
         # 'height':1080

          }

for i in range(0,210,30):
    data['pn']=i
    get_src(data,i)

# href="/search/down?tn=download&amp;ipn=dwnl&amp;word=download&amp;ie=utf8&amp;fr=result&amp;url=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01b26f599106e10000002129eb2896.JPG&amp;thumburl=http%3A%2F%2Fimg0.imgtn.bdimg.com%2Fit%2Fu%3D1097067045%2C1404153333%26fm%3D27%26gp%3D0.jpg"></a>
# objurl=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0142135541fe180000019ae9b8cf86.jpg%401280w_1l_2o_100sh.png&rpstart=0&rpnum=0&adpicid=0
# http://img.zcool.cn/community/0142135541fe180000019ae9b8cf86.jpg@1280w_1l_2o_100sh.webp
# 'http://img0.imgtn.bdimg.com/it/u=1097067045,1404153333&fm=27&gp=0.jpg'
# 'http://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=http%3A%2F%2Fimg.taopic.com%2Fuploads%2Fallimg%2F120727%2F201995-120HG1030762.jpg&thumburl=http%3A%2F%2Fimg1.imgtn.bdimg.com%2Fit%2Fu%3D594559231%2C2167829292%26fm%3D27%26gp%3D0.jpg'
# 'http://img.taopic.com/uploads/allimg/120727/201995-120HG1030762.jpg'
# 'http://img1.imgtn.bdimg.com/it/u=594559231,2167829292&fm=27&gp=0.jpg'
# http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0
# http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&step_word=&hs=0&pn=1&spn=0&di=113204231140&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=594559231%2C2167829292&os=2394225117%2C7942915&simid=3436308227%2C304878115&adpicid=0&lpn=0&ln=1981&fr=&fmq=1526575070122_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.taopic.com%2Fuploads%2Fallimg%2F120727%2F201995-120HG1030762.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bpw5rtv_z%26e3Bv54AzdH3Fejvp56AzdH3Fda8da0AzdH3Fdanll9_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=
import requests


url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%B0%8F%E7%8C%AA%E4%BD%A9%E5%A5%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E5%B0%8F%E7%8C%AA%E4%BD%A9%E5%A5%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=60&rn=30&gsm=3c&1526565872969='
def getimgs(page):
    try:
        # htmls=[]
        res = requests.get(url)
        htmls=res.json().get('data')
    except Exception as e:
        print(e)
    count = (page-1)*10
    for html in htmls:
        # for i in html:
            if html.get('hoverURL') != None:
                try:
                    ir = requests.get(html['hoverURL'])     #ir = requests.get(html.get('hoverURL'))
                    if ir.status_code == 200:
                        open(r'C:\Users\Larry\Desktop\picture\\' + '%d.jpg'%count, 'wb').write(ir.content)
                        print(str(count) + "----" + html['hoverURL'])   #html.get('hoverURL')
                        count = count + 1
                except Exception as e:
                    print('保存失败')
getimgs(2)
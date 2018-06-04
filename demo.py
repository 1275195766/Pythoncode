import requests
import os


url = 'https://image.baidu.com/search/acjson'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}

def Get_json(data):
    try:
        text = requests.get(url, params=data, headers=headers)
        text.encoding = 'utf-8'
        return text.json()      #得到网页的 json 格式
    except:
        return ''

def Get_pic(data):
    html = Get_json(data)
    pictures = html['data']     #获得字典 data 的值
    for i in pictures[:-1]:
        new_url = i['hoverURL']
        title = i['fromPageTitleEnc']
        Save_pic(new_url, title)

def Save_pic(url_pic, i):
    print(url_pic, end='       ')
    r = requests.get(url_pic, headers=headers)
    print(r.status_code)
    if not os.path.exists('picture'):       #判断目录是否存在 不存在就创建
        os.mkdir('picture')
    i = i.replace('"', '_')                 #因标题格式错误 替换
    with open('picture\%s.jpg'%i[:7], 'wb') as f:   #以二进制写入文件
        f.write(r.content)

if __name__ == '__main__':

    aa = input('请输入你要查找的目标： ')
    data = {
        'tn': 'resultjson_com',
        'ipn':'rj',
        'ct': '201326592',
        'fp': 'result',
        'word': aa,
        'pn': 30,
        'rn': 30,
    }
    for i in range(30,210,30):      #遍历
        data['pn'] = i
        Get_pic(data)
        break


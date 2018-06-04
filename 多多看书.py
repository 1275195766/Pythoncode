import urllib.request

import requests

import os

import bs4



url='https://xiaoshuo.sogou.com/'

header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}

opener=urllib.request.build_opener()    #创建opener对象

opener.addheaders=[header]      #对opener对象添加浏览器标头

urllib.request.install_opener(opener)     #将opener对象安装为全局

# sx=input('请输入要看的分类:')

page_home=requests.get(url)     #获取首页

# print(page_home.text)

soup=bs4.BeautifulSoup(page_home.text,'html.parser')    #将首页转换为bs对象

# print(soup)

fl=soup.find_all('a',pbtag='男生')    #提去男生分类标签

for j in range(0,18):

    for i in fl:

        new_ns=url+i.get('href')    #构造男生分类标签的网址

        page_ns=requests.get(new_ns)    #获取分类网页

        soup_ns=bs4.BeautifulSoup(page_ns.text,'html.parser')

        nrs=soup_ns.find_all('a',class_='btn btn-toc')  #提取单本小说的标签

        titles=soup_ns.select('h3 a[pbflag=内容区_'+str(j)+']')    #提取标题
        for title in titles:
            with open(r'H:\小说\\' + str(title.string)+ '.txt', 'a') as f:
                print(str(title.string))
                f.write('\n')
        # for t in titles:
        #     print(t.string)


        for nr in nrs:

            nr_url=url+nr.get('href')   #全部目录网址

            # print(nr_url)

            qbml=requests.get(nr_url)   #获取全部目录的网页源码

            soup_ml=bs4.BeautifulSoup(qbml.text,'html.parser')

            zw_urls=soup_ml.find_all('a','text-ellips')

            # print(zw_url)

            for zw_url in zw_urls:

                # print(zw_url.get('href'))
                zw=url+zw_url.get('href')
                zw_nr=requests.get(zw)
                soup_zw=bs4.BeautifulSoup(zw_nr.text)
                zwnrs=soup_zw.select('div#contentWp p')
                for zj in soup_zw.find('h1'):
                    with open(r'H:\小说\\' +str( title.string) + '.txt', 'a') as f:
                        f.write('\n'+str(zj) + '\n\n')
                    print(zj)
                    break

                for zwnr in zwnrs:
                    with open(r'H:\小说\\' +str( title.string)+ '.txt', 'a') as f:
                        f.write(str(zwnr.string)+'\n')
                # print(title.string)
                    print(zwnr.string)

            # break

        # print(i.get('href'))

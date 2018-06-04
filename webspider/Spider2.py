import urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://iqianyue.com",timeout=10)
        #file=urllib.request.urlopen("http://blog.csdn.net/weiwei_pig/article/details/51178226",timeout=1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))
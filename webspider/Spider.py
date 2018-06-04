import urllib.request

url="http://blog.csdn.net/weiwei_pig/article/details/51178226"

file=urllib.request.urlopen(url)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
opener=urllib.request.build_opener()
opener.addheaders=[headers]


data=opener.open(url).read()
#print(data)

fhandle=open("H:\Pythoncode/3.html","wb")

fhandle.write(data)
fhandle.close()


#print(file.geturl())
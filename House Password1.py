import re

# -*- coding=utf-8 -*-
r=r"src=.+?.jpg"
string='< src="https://imgsa.baidu.com/forum/w%3D580/sign=ee98fb91d8b44aed594ebeec831d876a/4a16d7cec3fdfc03fac51b63d63f8794a6c22692.jpg" >'
result=re.search(r,string)
print(result)

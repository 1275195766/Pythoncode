import re

from notebook.notebookapp import raw_input

temp = []
temp2 = []
temp3 = []


def checkio(data):
    for itme in data:
        if itme>='a' and itme<='z':
            temp.append(itme)
        elif itme>='A' and itme<='Z':
            temp2.append(itme)
        elif itme>='0' and itme<='9':
            temp3.append(itme)
    if len(temp)!=0 and len(temp2)!=0 and len(temp3)!=0 and len(data)>=10 :
        a=True
    else:
        a=False
    # r=re.compile(r'^([0-9]+?)([A-Z]+?)([a-z]+?)$')
    #
    # r.match(data).groups()
    # if len() == 3 and len(data) >= 10:
    #     a = True
    # else:
    #     a = False
    #
    #     # replace this for solution
    # return a


data = raw_input()
print(checkio(data))

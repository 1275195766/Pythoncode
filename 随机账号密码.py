import random
zhmm={}
for i in range(30):

    zh=''
    mm=''
    for j in range(3):
        zh=zh+chr(random.randint(97,122))
    for k in range(5):
        zh=zh+chr(random.randint(48,57))
    for j in range(3):
        mm =mm + chr(random.randint(97, 122))
    for k in range(6):
        mm = mm + chr(random.randint(48, 57))
    if not zhmm.get(zh):
        zhmm[zh]=mm
print(zhmm)
with  open(r'H:\zhmm.txt','w') as file:
    for k,v in zhmm.items():
        file.write('账号:'+k+'\n'+'密码:'+v+'\n\n')
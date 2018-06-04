a=1
while a==1 :
    temp=input("猜一下我心里在想什么数字：")
    #print('temp=',temp)
    if temp>='0' and temp<='9':
        guess=int(temp)
    elif temp=='q' or 'Q':
        break
    
    if guess>8:
        print("哎呀！太大了")
    elif guess<8:
        print("哎呀！太小了")
    else:
        print('猜对了,退出游戏请按q')
    
        

print("游戏结束")
    

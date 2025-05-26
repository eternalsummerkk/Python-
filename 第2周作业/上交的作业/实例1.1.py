tempstr=input("请输入一个温度数值（若以华氏温度为单位请以F结尾，若以摄氏度为单位请以C结尾)：")
print(tempstr[0:-1])
print(tempstr[-1])
if tempstr[-1] in ['C','c']:
    F =(eval(tempstr[0:-1])*1.8)+32
    print("转换后的温度是:{:.2f}F".format(F))
elif tempstr[-1] in ['F','f']:
    C =(eval(tempstr[0:-1])-32)/1.8
    print("转换后的温度是:{:.2f}C".format(C))
else:
    print("输入的温度数值格式错误，既非华氏温度也非摄氏度")

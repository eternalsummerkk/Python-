money=input("请输入一个数值(美元以USD结尾，人民币以CNY结尾):")
print(money[0:-3])
print(money[-1])
if money[-1] in ["y","Y"]:
    USD=eval(money[0:-3])/6
    print("转换后的数值为:{:.2f}".format(USD))
elif money[-1] in ["d","D"]:
    CNY=eval(money[0:-3])*6
    print("转换后的数值为:{:.2f}".format(CNY))
else:
    print("您输入的格式有误")


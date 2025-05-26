money=input("请输入一个数值（以USD结尾表示美元，以CNY结尾表示人民币）：")
if money[-1] in ["D","d"]:
    CNY=float(money[0:-3])*6
    print("由{:.2f}美元转换得的人民币为{:.2f}元".format(money,CNY))
elif money[-1] in ["Y","y"]:
    USD=float(money[0:-3])/6
    print("{:.2f}人民币转换得的美元为{:.2f}$".format(money,USD))
else:
    print("您输入的格式有误")

#print("由{:.2f}人民币转换得的美元为{:.2f}$".format(money,USD))
#print("转换得的美元为{:.2f}$".format(USD))
#第一行代码是错误的，第二行代码是正确的。
#第一行错误在money=1234USD/CNY 是一个字符串类型变量，而{:2F}命令约束的是数值类型变量
#把line7 第一个{:2f}修改为{}即可

#猜数游戏
number_int1=5#内置一个数字作为基准
for i in range(1000000000000000):#设置循环用于计数
      number_int2=eval(input("请输入一个处于0~9的整数："))#将input置于循环结构内，使得猜错之后重新输入数字
      if number_int1==number_int2:#第一个条件：两数字相等
            print("预测{}次，你猜中了！".format(i+1))
            break#结束整个循环
      if number_int2<number_int1:#第二个条件
            print("遗憾，太小了")
      if number_int2>number_int1:#第三个条件
            print("遗憾，太大了")
#注意选择结构：
if-if-if
if-else
if-elif-else

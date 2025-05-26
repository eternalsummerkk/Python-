number=5#预设的整数
for i in range(100000000):#设置一个循环，通过循环进行计数。
      number_u=int(input("请您输入一个0~9的整数："))
      if number_u>number:
            print("遗憾，太大了")
      elif number_u<number:
            print("遗憾，太小了")
      else:
            print("预测{}次，你猜中了！".format(i+1))
      if number==number_u:#猜对以后终止循环
            break

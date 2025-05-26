number_integer=5
number_int=0#事先为number_int赋值，不然line4中的number_int是未命名变量。
count=0
while number_integer!=number_int:#while循环的条件是两个数不等（TRUE），一旦两个数相等，循环终止。
      number_int=int(input("请输入1个0~9的整数："))
      if number_integer==number_int:#此时两个数相等，循环终止，不需要加break。
            count=count+1#一旦进行一次循环，就+1，为循环次数计数。
            print("预测{}次，你猜中了！".format(count))
      if number_integer>number_int:
            count=count+1
            print("遗憾，太小了")
      if number_integer<number_int:
            count=count+1
            print("遗憾，太大了")


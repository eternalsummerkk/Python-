#求最大公约数
number_int1=int(input("请输入1个整数："))
number_int2=int(input("请输入1个整数："))#用户输入数字
if number_int1>number_int2:
      number_smaller=number_int2
else:
      number_smaller=number_int1#最大公约数不超过用户输入的最小的数字，找到最小的数字
for i in range(number_smaller+1,1,-1):#最大公约数的范围不超过用户输入的最小的数字，故最大值应该为number_smaller
      if number_int1%i==0 and number_int2%i==0:
            f=i
            break#通过多次循环找公约数，循环到最后一遍最终找到最大的公约数，并将其提取出来。
print("{}和{}的最大公约数为{}".format(number_int1,number_int2,f))#打印出最大公约数

#求最小公倍数
number_int1=int(input("请输入1个整数："))
number_int2=int(input("请输入1个整数："))#用户输入数字
if number_int1>number_int2:
      number_smaller=number_int2
else:
      number_smaller=number_int1#最大公约数不超过用户输入的最小的数字，找到最小的数字
for i in range(1,number_smaller+1):#最大公约数的范围不超过用户输入的最小的数字，故最大值应该为number_smaller
      if number_int1%i==0 and number_int2%i==0:
            f=i#通过多次循环找公约数，循环到最后一遍最终找到最大的公约数，并将其提取出来。
number_zuixiaogongbeishu=(number_int1*number_int2)/f
print("{}和{}的最小公倍数为{}".format(number_int1,number_int2,number_zuixiaogongbeishu))#打印出最大公约数





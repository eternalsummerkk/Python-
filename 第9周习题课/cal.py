from random import random
from random import randint
number_1=randint(0,9)
number_2=randint(0,9)
roll=randint(1,10)
key_1=number_1+number_2
key_2=number_1-number_2
idx=0
if 1<=roll<=5:
      print("{}+{}=?".format(number_1,number_2))
      key_visitor=eval(input("请你输入该算式的答案："))
      while key_1!=key_visitor:
            print("{}+{}={} 错误".format(number_1,number_2,key_visitor))
            key_visitor=eval(input("请你输入该算式的答案："))
            idx=idx+1
      else:
            idx=idx+1
            print("{}+{}={} 正确,进行了{}次运算，正确率为{}".format(number_1,number_2,key_1,idx,1/idx)) 
if 6<=roll<=10:
      print("{}-{}=?".format(number_1,number_2))
      key_visitor=eval(input("请你输入该算式的答案："))
      while key_2!=key_visitor:
            print("{}-{}={} 错误".format(number_1,number_2,key_visitor))
            key_visitor=eval(input("请你输入该算式的答案："))
            idx=idx+1
      else:
            idx=idx+1
            print("{}-{}={} 正确,进行了{}次运算，正确率为{}".format(number_1,number_2,key_2,idx,1/idx)) 

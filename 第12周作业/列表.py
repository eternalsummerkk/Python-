#序列数据的输入
def getNum():
      num=[]
      Numstr=input("请输入数字（输入回车键停止）")
      while Numstr!="":
            num.append(eval(Numstr))#eval()函数处理不了""字符串，将line6与line7调换位置会报错#ls.append(x)表示把x加入列表的最后一个 书本P161
            Numstr=input("请输入数字（输入回车键停止）")
      return num#返回函数值num给getNum()并显示  
#求平均值
def mean(numbers):
      s=0
      for i in numbers:
            s=s+i
      return s/len(numbers)
#求中位数
def median(numbers):
      m=0
      new=sorted(numbers)#这一行必须是这样写而不能只写sorted(numbers)。#sorted()函数，对列表进行排序，课本P149页。
      if len(numbers)%2==0:
            m=(new[len(numbers)//2]+new[len(numbers)//2-1])/2#项数为偶数时#分片的指针[]不能是浮点类型因此必须整除//
      else:#项数为奇数时
            m=new[len(numbers)//2]
      return m
#求标准差
def standard(numbers):#标准差就是方差的算术平方根
      st=0
      average_numbers=mean(numbers)
      length_numbers=len(numbers)
      for i in numbers:
            st=st+pow(average_numbers-i,2)
      st=st/length_numbers#求方差
      st=st**0.5#求算数平方根
      return st

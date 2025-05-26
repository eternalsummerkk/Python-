#习题3
from random import random
from random import randint
n=randint(5,10)
sum_奇数=0
sum_偶数=0
str_奇数=""
str_偶数=""
for i in range(1,n+1,2):#确定是奇数中的哪一个数即{？}！
      key_奇数=1#一次外层循环结束重新赋值
      for j in range(1,i+1):#求确定的奇数{？}！的阶乘
            key_奇数= key_奇数*j#求确定的奇数{？}！的阶乘的具体算法
      sum_奇数=sum_奇数+key_奇数#求和
      str_奇数=str_奇数+"{}!+".format(i)#变字符串
for i in range(2,n+1,2):#同上
      key_偶数=1
      for j in range(1,i+1):
            key_偶数= key_偶数*j
      sum_偶数=sum_偶数+key_偶数
      str_偶数=str_偶数+"-{}!".format(i)#line19
sum_阶乘=sum_奇数-sum_偶数#求最终答案
str_阶乘="{}{}={}".format( str_奇数,str_偶数,sum_阶乘)####
print(str_阶乘)

            
     

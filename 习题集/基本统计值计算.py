#获取数字
from math import *
def getnums():
      nums=[]
      inputnum=input("请输入数字，以回车结束")
      while inputnum!="":
            nums.append(eval(inputnum))#input输入的“数字”是str
            inputnum=input("请输入数字，以回车结束")
      return nums
#平均值
def mean(nums):
      tn=0
      for i in nums:
            tn=tn+i
      return tn/len(nums)
#标准差
def dev(nums,mean):
      a=0
      for i in nums:
            a=a+(i-mean)**2
      return sqrt(a/(len(nums)-1))
#中位数
def median(nums):
      sorted(nums)
      if len(nums)%2==0:
            midnum=(nums[len(nums)/2]+nums[(len(nums)/2)-1])/2
      else:
            midnum=nums[len(nums)//2]
      return midnum
#主体函数
n=getnums()
m=mean(n)
print("平均值{}，标准差{}，中位数{}".format(m,dev(n,m),median(n)))

      
      

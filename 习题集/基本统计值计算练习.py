#基本统计值计算
from math import *
#获取用户输入
def getnums():
      nums=[]
      numsinput=input("请输入数字，以回车结束：")
      while numsinput!="":
            nums.append(eval(numsinput))
            numsinput=input("请输入数字，以回车结束：")
      return nums
#计算平均值
def mean(nums):
      a=0
      for i in nums:
            a += i
      return a/len(nums)
#计算方差
def fc(nums,avg):
      b=0
      for i in nums:
            b+=(i-avg)**2
      return sqrt(b/(len(nums)-1))
#计算中位数
def median(nums):
      nums.sort()
      if len(nums)%2==0:
            midnum=(nums[len(nums)/2]+nums[len(nums)/2]-1)/2
      else:
            midnum=nums[len(nums)//2]
      return midnum
#计算
n=getnums()
m=mean(n)
print("fc{}，zws{},pjs{}".format(fc(n,m),median(n),m))
            

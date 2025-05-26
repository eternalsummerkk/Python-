#5.5无异常处理版
def isPrime(number_1):
      for i in range(2,number_1):#for-else扩展语句
            if number_1%i==0:#为什么“2”可以
                  return False
                  break
      else:
            return True
number_2=eval(input("请输入整数："))
if isPrime(number_2):
      print("是质数")
else:
      print("不是质数")

      

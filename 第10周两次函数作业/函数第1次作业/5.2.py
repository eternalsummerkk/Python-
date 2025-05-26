def isOdd(number_1):
      if number_1%2==0:
            return False
      else:
            return True
number_2=eval(input("请输入一个整数："))
if isOdd(number_2):
      print("奇数")
else:
      print("偶数")
            

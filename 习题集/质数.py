def isprime():
      nums=eval(input("请输入一个整数："))
      while type(nums)!=type(1):
            nums=eval(input("请重新输入一个整数："))
      for i in range(2,nums):
            if nums%i==0:
                  return False
      else:
            return True
isprime()

      

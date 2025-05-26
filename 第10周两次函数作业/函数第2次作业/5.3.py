#5.3
def isNum(str_1):
      if type(eval(str_1))==type(5) or type(eval(str_1))==type(5.5) or type(eval(str_1))==type(1+1j):#要加eval(),变成可计算的量
            return True
      else:
            return False
str_2=input("输入一个字符串：")#input()函数输入的变量是字符类型
if isNum(str_2):
      print("True")
else:
      print("False")

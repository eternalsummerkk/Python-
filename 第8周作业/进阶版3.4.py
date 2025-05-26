#回文数的判定进阶版
number_huiwen=input("请你输入一个数字：")
lenghth_huiwen=len(number_huiwen)
for i in range(1,lenghth_huiwen//2+1):#只需要判断回文数的位数的一半次数即可，无论奇数偶数
      if number_huiwen[i-1]!=number_huiwen[-i]:
            print("你输入的不是一个回文数字")
            break#该if的意义就是只要有一对不是回文即可终止
else:#利用for-else扩展语句，只要for循环正常执行完毕，意味着满足回文数字的要求。
      print("你输入的是一个回文数字")
      

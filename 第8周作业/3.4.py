#不限制位数的回文数判定
number_huiwen=input("请输入一个数字，计算机会判定它是否为回文数：")
length_huiwen=len(number_huiwen)#索引
for i in range(length_huiwen//2):#整除2，无论是奇数位数还是偶数位数，都只需要length_huiwen//2次循环即可判定。
      if number_huiwen[i]!=number_huiwen[-i-1]:#一旦进入该if，意味着不是回文数
            print("您输入的数字不是回文数")
            break#有一对不是回文，终止循环。
else:#for-else扩展语句,书本P108,for循环遍历完后进入该else。这意味着首尾每一对数字都相同，满足回文数要求。
      print("您输入的是一个回文数字")
            
      

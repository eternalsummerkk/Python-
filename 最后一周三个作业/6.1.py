from random import *
list_1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9"]
count=0#计数
for i in range(10):#创建10个空的密码
      key=""
      count=count+1
      for j in range(8):#给每个空的密码随机填入字符
            key=key+list_1[randint(0,len(list_1)-1)]
      if count%2==0:#如果达到偶数行，换行
            print(key)  
      else:#如果是奇数行，空一格
            print(key,end=" ")


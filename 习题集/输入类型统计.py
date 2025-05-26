str1=input("输入字符串")
count_num=0
count_zimu=0
count_blank=0
count_else=0
for i in str1:
      if "0"<=i<="9":
            count_num+=1
      elif "A"<=i<="z":
            count_zimu+=1
      elif i==" ":
            count_blank+=1
      else:
            count_else+=1
print("{},{},{},{}".format(count_num,count_zimu,count_blank,count_else))
      
            

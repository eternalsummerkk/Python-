#第一步取出数字，第二步验证是否为质数，如果是打印且计数，如果不是跳过
counts=0
for i in range(2,101):
      for j in range(2,i):
            if i%j==0:
                  break
      else:
            counts=counts+1
            print(i,end=" ")
      if counts/5==1:#恰好为5个数时换行
            counts=0
            print()

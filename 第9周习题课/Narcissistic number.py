#习题2
for a in range(100,1000):
      if pow(eval(str(a)[0]),3)+pow(eval(str(a)[1]),3)+pow(eval(str(a)[2]),3)==a:
            number_1=a
            break
for b in range(number_1+1,1000):
      if pow(eval(str(b)[0]),3)+pow(eval(str(b)[1]),3)+pow(eval(str(b)[2]),3)==b:
            number_2=b
            break
for c in range(number_2+1,1000):
      if pow(eval(str(c)[0]),3)+pow(eval(str(c)[1]),3)+pow(eval(str(c)[2]),3)==c:
            number_3=c
            break
for d in range(number_3+1,1000):
      if pow(eval(str(d)[0]),3)+pow(eval(str(d)[1]),3)+pow(eval(str(d)[2]),3)==d:
            number_4=d
            break
print("4个水仙花数为{}，{}，{}，{}".format(number_1,number_2,number_3,number_4))
#另一种
print("#另一种")
idx=0
for i in range(100,1000):
      if pow(eval(str(i)[0]),3)+pow(eval(str(i)[1]),3)+pow(eval(str(i)[2]),3)==i:
            print("{}是水仙花数。".format(i))
            idx=idx+1
print("{}个".format(idx))
            

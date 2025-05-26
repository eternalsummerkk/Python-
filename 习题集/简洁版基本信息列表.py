from random import *
timeL=[]
n=[]
e=[]
for i in range(24):
      timeL.append(str(i)+":00")
      n.append(uniform(30.40,31.53))
      e.append(uniform(120.52,122.12))
      print("{}   沪NX2119   {}   {}".format(timeL[i],n[i],e[i]))
time=[]
counts=0
for i in range(0,len(e)):
      if n[i]>31.3:
            counts+=1
            time.append(timeL[i])
print("{}{}".format(time,counts))

from random import *
file_0=open("cardata.txt","w")
list_0=[]
for i in range(0,24):
      list_1=[]
      time_0=str(i)+":00"
      list_1.append(time_0)
      plate="沪NX2119"
      list_1.append(plate)
      north=uniform(30.40,31.53)
      list_1.append(north)
      east=uniform(120.52,122.12)
      list_1.append(east)
      list_0.append(list_1)
      print(list_1)
print(list_0)
count_0=0
time_1=[]
for j in range(0,len(list_0)):
      if list_0[j][2]>31.3:
            count_0=count_0+1
            time_1.append(list_0[j][0])
print("{}次,时间为{}".format(count_0,time_1))
file_0.close()
      
      
      

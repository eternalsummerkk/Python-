#earthweight=float(60)
#moonweight=float(earthweight*0.165)
#weightup=float(0.5)
#earthweight=earthweight+weightup*10
#moonweight=moonweight+weightup*10
#print("未来10年在月球上的重量为{:2f}kg,在地球上的重量为{:2f}kg".format(moonweight,earthweight))

#x=float(input("请输入您在地球上的体重："))
#for i in range(10):
    #x=x+0.5
    #y=x*0.165
#print("未来第{}年在月球上的重量为{:2f}kg,在地球上的重量为{:2f}kg".format(i+1,y,x))

earthweight=float(input("请输入您在地球上的体重："))
weightup=0.5
for i in range(10):
    earthweight=earthweight+weightup
    moonweight=earthweight*0.165
print("未来第{}年在月球上的重量为{:.2f}kg,在地球上的重量为{:.2f}kg".format(i+1,moonweight,earthweight))


#float函数必须加
#earthweight=earthweight+weightup与earthweight=earthweight+weightup*i在for in 循环中有区别


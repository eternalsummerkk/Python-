weight=float(input("请输入你在地球上的体重："))
factor=0.5
for i in range(10):
    weight=weight+factor
    m_weight=weight*0.165
print("十年后地球上的重量为{}，月球上的重量{}".format(weight,m_weight))

    

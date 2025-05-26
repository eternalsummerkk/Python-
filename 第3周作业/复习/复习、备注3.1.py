#e_weight=float(input("请输入你在地球上的体重"))
a_weightup=0.5
for i in range(1,11):
      #e_weight=e_weight+a_weightup
      m_weight=e_weight*0.165
print("十年后在地球上的重量为{}kg，在月球上的重量为{}".format(e_weight,m_weight))

#如果line1不加float line4将无法运行，因为line4成为了str+float,这两种数值类型不能相加减

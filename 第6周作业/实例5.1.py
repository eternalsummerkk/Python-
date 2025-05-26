height,weight=eval(input("请输入你的身高（米）和体重（kg）[用逗号隔开]"))
bmi=weight/pow(height,2)
print("你的bmi指数为{:.2f}".format(bmi))
who,dom="",""
if bmi<18.5:
      who,dom="偏瘦","偏瘦"
elif 18.5<=bmi<24:
       who,dom="正常","正常"
elif 24<=bmi<25:
      who,dom="正常","偏胖"
elif 25<=bmi<28:
     who,dom= "偏胖","偏胖"
elif 28<=bmi<30:
      who,dom="偏胖","肥胖"
else:
      who,dom="肥胖","肥胖"
print("您的国际BMI值为{}，国内BMI值为{}".format(who,dom))


dayup,dayfactor=1,0.01
for i in range(1,366):
    if i%7 in [0,6]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("一年365天，5天向上、2天向下的的效果就是你的能力从1成长为了{:.2f}".format(dayup))

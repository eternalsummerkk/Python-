weekstr="星期一星期二星期三星期四星期五星期六星期日"
week=int(input("请你输入1~7中任意一个数字："))
print("{}".format(weekstr[(week-1)*3:week*3]))

#line2的week必须是int(),eval()函数限制的整数型，因为week是作为索引，出现在line3fomat约束里切分weekstr.\
#其次，format([:])中的切分必须用":"来限制

weekstr="星期一星期二星期三星期四星期五星期六星期日"
weekid=eval(input("请您在1~7选择一个数字输入，程序会将它转换成星期的形式："))
pos=(weekid-1)*3
print("您输入的数字{},转化为星期的形式后为{}".format(weekid,weekstr[pos:pos+3]))


#line2 必须加eval()函数，不然line3的pos无法运算。
#line4的format不限制字符串或数值型，限制数值型的为{：.2f}

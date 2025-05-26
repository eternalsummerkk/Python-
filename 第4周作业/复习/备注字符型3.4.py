palindromic_number=(input("请你输入一个五位数："))
if palindromic_number[0] == palindromic_number[-1] and palindromic_number[1] == palindromic_number[-2]:
      print("是palindromic number")
else:
      print("不是palindromic number")
#line2中 in 与 = 的使用不能混淆，in 表示相同判定，= 则是赋值并不表示相同。并且可以和数值型样，用==号表示相同。

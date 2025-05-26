palindromic_number=float(input("请你输入一个五位数："))
if palindromic_number//10000 == palindromic_number%10 and (palindromic_number//1000-palindromic_number%100)/9 in range(-9,10):
      print("是palindromic number")
else:
      print("不是palindromic number")

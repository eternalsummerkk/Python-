n=input("请你输入一个五位数字，该数字将被命名为n：")
if n[-1] in (n[0]) and n[-2] in (n[1]):
    print("您输入的数字n——'{}'是一个回文数".format(n))
else:
    print("您输入的数字n——'{}不是一个回文数".format(n))
        

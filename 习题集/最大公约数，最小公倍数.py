a,b=eval(input("请输入2个整数，用逗号隔开："))#不加eval()，输入的为单个字符串，不能赋给两个变量
c=0
d=0
if a>b:
      c=a
if a<b:
      c=b
for i in range(2,c+1):
      if a%i==0 and b%i==0:
            d=i
print(d)
e=(a*b)/d
print(e)
            
      

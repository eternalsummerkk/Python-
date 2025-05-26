#索引法
str_visitor=input("请输入一个字符串，将计算机会为你统计其中英文字符、数字、空格和其他字符的个数：")
length_str=len(str_visitor)#计数字符串位数，方便用index切片
index=str_visitor#index作为索引
count_letter=0
count_number=0
count_blank=0
count_else=0
for i in range(length_str):#i在这里是数字而不是字符
      if "A"<=index[i]<="z":#index[i]表示对字符串进行取字符，即切片#attention!"A"这类字母应该是字符，加双引号。
            count_letter=count_letter+1
      elif "0"<=index[i]<="9":#attention!即使是数字也要加双引号，因为是字符之间的比较，只有加了引号才能转化为ASCII码进行比较。
            count_number=count_number+1
      elif index[i]==" ":#“==”是相等，“=”是赋值
            count_blank=count_blank+1
      else:
            count_else=count_else+1
print("您输入的字符串中，有英文字符{}个、数字{}个、空格{}、其他字符{}个".format(count_letter,count_number,count_blank,count_else))

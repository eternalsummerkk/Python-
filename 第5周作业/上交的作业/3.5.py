#第一种
print("+ - - - - + - - - - +")
for i in range(4):
      print("|{:^19}|".format("|"))
print("+ - - - - + - - - - +")
for i in range(4):
      print("|{:^19}|".format("|"))
print("+ - - - - + - - - - +")
 #第二种
for i in range(11):
      if i in(0,5,10):
            print("+ - - - - - + - - - - - +")
      else:
            print("|           |           |")


      

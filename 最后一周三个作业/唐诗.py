fname=input("请输入你想打开、创建的文件名：")
file_0=open(fname,"w+")#"w"与"w+"不同
ls=["唐诗","宋词","元曲"]
file_0.writelines(ls)
file_0.seek(0)
for line in file_0:
      print(line)   
file_0.close

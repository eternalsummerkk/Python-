excludes={"the","and","of","you","a","i","my","in"}
def gettext():
    txt=open("hamlet.txt","r").read()
#open()函数：有两个参数，一个是打开的文件（此处为hamlet.txt）,一个是mode(此处为r,表示只读)
#read()函数：参数为size（读取字节的个数）,此处为默认值全部
#导入后为txt的类型为列表list
    txt=txt.lower()
    for ch in '"!#$%&*=-,.?/<>={[}]^_~`':
        txt=txt.replace(ch," ")
    return txt
hamlet=gettext()
words=hamlet.split()
#字典方法split():根据空格划分单词
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
#counts[word]结果是value（值）
#字典方法get():有两个参数，分别为key对应的value(此处为word)和设置的默认值(此处为0)
#如果字典中没有对应的key,则返回默认值，如果有，返回key对应的value
for word in excludes:
    del(counts[word])
items=list(counts.items())
#字典方法items():返回字典中所有的键值信息，把字典counts变成了dict_items([('tragedy', 3)……)，为了更好地利用，可以转换为列表类型。
items.sort(key=lambda x:x[1],reverse=True)
#列表方法sort():有两个参数key和reverse,key是排序的依据，值一般为函数，reverse是降(从大到小)\升序(从小到大)，值一般为True/False
#匿名函数lambda x:x[1]:x是参数，此处为('tragedy', 3)，x[1]为返回值，此处为”3“.
for i in range (10):
    word,count=items[i]
#items[0]=tragedy,3
    print("{0:<10}{1:>5}".format(word,count))
    

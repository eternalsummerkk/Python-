#设置无效词汇，将它们排除
excludes={"the","and","to","of","i","a","you","my","in","it","that","is","not","his","this","but","with","for","your","s","he","as","be","me","what","o","him"}
#导入文本、全小写、把特殊符号变成空格
def gettext():
      hamlet=open("hamlet.txt","r").read()
      hamlet=hamlet.lower()
      for ch in """""""?><,.;'[]\-=_+!@#$%^&*()`~·`":
            hamlet=hamlet.replace(ch," ")
      return hamlet
hamlet=gettext()
#分词、统计词频、排序
counts={}
words=hamlet.split()
for word in words:
      counts[word]=counts.get(word,0)+1
for i in excludes:
      del(counts[i])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
#打印前10的高频词
for i in range(10):
      word,count=items[i]
      print("{:<10}{:>10}".format(word,count))

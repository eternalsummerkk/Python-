ability=1
dayup=0.01
for i in range(1,366):
      if i%7 in [0,6]:
            ability=ability*(1-dayup)
      else:
            ability=ability*(1+dayup)
print("一年365天，2天向下，5天向上，你的能力值是{:.2f}".format(ability))

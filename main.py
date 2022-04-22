import random
import json
from datetime import datetime

# PDict = 计划模板A.__dict__
记录 = {}

filename = "./记录.json"
with open(filename, "r", encoding='utf-8') as fp:
  历史记录 = json.load(fp)

成员=[
      "陈兆年", 
      "尹崇强",
      "王龙",
      # "申庆涛",
      "梁志远",
      "陈文博",
      # "张国志",
      ]
今日成员={}

for a in 成员:
  if 历史记录. __contains__(a):    
    今日成员[a] = 历史记录[a]
  else:
    今日成员[a] = 1

# 计算概率
# 今日概率
sum = 0
for a in 今日成员.keys():
  sum = sum + 今日成员[a]

count = 0
今日概率 = {}
for a in 今日成员.keys():
  今日概率[a] = sum/今日成员[a]
  count = count + sum/今日成员[a]
  
今日概率2 = {}
print ("| 名称 | 概率 |")

for a in 今日成员.keys():
  今日概率2[a] = round(今日概率[a]/count * 100, 0)
  print ("| " + a + " | " + str(今日概率2[a]) + " | ")

# 所有人概率平等(历史记录参与计算)
randomList = []
for a in 今日概率2.keys():
  for b in range(int(今日概率2[a])):
    randomList.append(a)

random.shuffle(randomList)

randomNum = random.randint(1, len(randomList))

print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : " + randomList[randomNum])

for a in 历史记录.keys():
  if (a == randomList[randomNum]):
    历史记录[a] = 历史记录[a] +1

with open(filename, "w+", encoding='utf-8') as fp:
    json.dump(历史记录, fp, ensure_ascii=False)
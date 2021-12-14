import sys
import fileinput
import time
from copy import deepcopy
from typing import Counter
from math import ceil
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

polymerBase ={}
pir={}
startLine=''
startTime = time.perf_counter()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if not startLine:
      startLine = cleanLine
    elif cleanLine != '':
      pair,sub =cleanLine.split(' -> ')
      pir[pair]=[(list(pair)[0]+sub),(sub+list(pair)[1])]
      polymerBase[pair]=0

polymerTemplate = deepcopy(polymerBase)

for i,val in enumerate(startLine):
      try:
        polymerBase[val+startLine[i+1]]+=1
      except IndexError:
        break

for steps in range(40):
  tempDict= deepcopy(polymerTemplate)
  for k,val in polymerBase.items():
    for pair in pir[k]:
        # print(pair)
        tempDict[pair]+= val
  polymerBase = deepcopy(tempDict)

counts={}
for k,val in polymerBase.items():
  char1,char2 = list(k)
  try:  
    counts[char1]+=val
  except:
    counts[char1]=val
  try:
    counts[char2]+=val
  except:
    counts[char2]=val

counters =Counter(counts)
common = counters.most_common()
print('result: ',ceil(common[0][1]/2)-ceil(common[-1][1]/2))
print("--- %s seconds ---" % (time.perf_counter() - startTime))
import sys
import fileinput
import time
from copy import deepcopy
from typing import Counter
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def updatePolymer(polymer,rules):
  oldPolymer = deepcopy(polymer)
  elementsToInsert=[]
  for i,val in enumerate( oldPolymer):
    try:
      pair = val+oldPolymer[i+1]
    except IndexError:
      continue
    elementsToInsert.append((i+1,rules[pair]))
  elementsToInsert.reverse()

  for element in elementsToInsert:
    polymerBase.insert(element[0],element[1])

polymerBase =[]
pir={}
startTime = time.perf_counter()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if not polymerBase:
      polymerBase.extend(list(cleanLine))
    elif cleanLine != '':
      pair,sub =cleanLine.split(' -> ')
      pir[pair]=sub

# print(polymerBase)
# print(pir)

for steps in range(40):
  updatePolymer(polymerBase,pir)
count = Counter(polymerBase)
common = count.most_common()
print('result: ',common[0][1]-common[-1][1])
print("--- %s seconds ---" % (time.perf_counter() - startTime))
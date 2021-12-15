import sys
import fileinput
import time
from collections import defaultdict
from math import ceil
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

polymerBase =defaultdict(int)
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

for i,val in enumerate(startLine):
      try:
        polymerBase[val+startLine[i+1]]+=1
      except IndexError:
        break
  
if __name__ == "__main__":
  for steps in range(40):
    tempDict= defaultdict(int)
    for k,val in polymerBase.items():
      for pair in pir[k]:
          tempDict[pair]+= val
    polymerBase = tempDict

  counts=defaultdict(int)
  for k,val in polymerBase.items():
    counts[k[0]]+=val
    counts[k[1]]+=val
  
  countvalues = sorted(counts.values())
  print('result: ',ceil(countvalues[-1]/2)-ceil(countvalues[0]/2))
  print("--- %s seconds ---" % (time.perf_counter() - startTime))
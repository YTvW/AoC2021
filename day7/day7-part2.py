import sys
import fileinput
import time
from statistics import mean
from math import ceil, floor
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

positions =[]

for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    positions=list(map(lambda pos: int(pos),cleanLine.split(',')))

startTime = time.time()
meanPos=mean(positions)
avgCommonposMin = floor(meanPos)
avgCommonposMax =ceil(meanPos)

fuelUsedMin = sum(list(map(lambda pos: sum(range(0,abs(avgCommonposMin-pos)+1)) ,positions)))
fuelUsedMax = sum(list(map(lambda pos: sum(range(0,abs(avgCommonposMax-pos)+1)) ,positions)))
if fuelUsedMax > fuelUsedMin:
  print('result: ',fuelUsedMin)
else:
  print('result: ',fuelUsedMax)

print("--- %s seconds ---" % (time.time() - startTime))
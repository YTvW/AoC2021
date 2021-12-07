import sys
import fileinput
import time
from statistics import median

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

positions =[]


for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    positions=list(map(lambda pos: int(pos),cleanLine.split(',')))

startTime = time.time()
avgCommonpos = int(median(positions))
fuelUsed = sum(list(map(lambda pos: abs(avgCommonpos-pos) ,positions)))
print('result: ',fuelUsed)
print("--- %s seconds ---" % (time.time() - startTime))
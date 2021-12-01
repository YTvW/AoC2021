import sys
import fileinput
from re import search
import time
startTime = time.time()
lastNumber = -1
count = 0
for line in fileinput.input("./input1.txt"):
    cleanLine = int(line.encode("utf-8").strip("\n"))
    if lastNumber == -1:
      lastNumber = cleanLine
      continue
    elif cleanLine > lastNumber:
      count +=1
    lastNumber = cleanLine

print('Result: %s' %  count)
print("--- %s seconds ---" % (time.time() - startTime))
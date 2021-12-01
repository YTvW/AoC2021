import sys
import fileinput
from re import search
import time
startTime = time.time()
data = []
lastWindow = None
count=0
for line in fileinput.input("./input1.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    # print(cleanLine)
    data.append(int(cleanLine))


for i in range( 2, len(data),1):
  print(data[i],data[i-1],data[i-2])
  currentWindow = data[i]+ data[i-1]+ data[i-2]
  
  if currentWindow > lastWindow:
    count +=1
  lastWindow = currentWindow
  print( currentWindow)
print(count-1)
print("--- %s seconds ---" % (time.time() - startTime))
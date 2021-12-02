import sys
import fileinput
from re import search
import time
startTime = time.time()
p1=0
p2=0
for line in fileinput.input("./input2.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    cmd = cleanLine.split(' ')[0][0]
    val = int(cleanLine.split(' ')[1])
    print(cmd,val)
    if cmd == 'f':
      p1 += val
    elif cmd == 'd':
      p2 += val
    elif cmd == 'u':
      p2 -= val
print(p1,p2)
print('Result: %s' %  (p1*p2))
print("--- %s seconds ---" % (time.time() - startTime))
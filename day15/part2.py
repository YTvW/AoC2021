import sys
import fileinput
import time
from collections import Counter
if len(sys.argv) >=2:
  fileName = sys.argv[1]
  size=10
else:
  fileName = "input"
  size= 100

coords ={}
paths= []
y =0
startTime = time.perf_counter()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    for x,risk in enumerate(cleanLine[::-1]):
      coords[(x,y)]=risk
    y+=1

      

print(coords)
print('results: ',len(paths))
print("--- %s seconds ---" % (time.perf_counter() - startTime))

#12.589
import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"


startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.encode("utf-8").strip("\n")
    print(cleanLine)


print("--- %s seconds ---" % (time.time() - startTime))
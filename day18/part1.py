import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def explode(data,pair):
  

  pass

def split(data,pair):

  pass

startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    print(cleanLine)


print("--- %s seconds ---" % (time.time() - startTime))
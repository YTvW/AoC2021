import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

data = []

def checkLengths(element):
  length = len(element)
  if length == 2:
    return True
  elif length == 3:
    return True
  elif length == 4:
    return True
  elif length == 7:
    return True
  else:
    return False

startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n").split(' | ')[1].split()
    data.extend(cleanLine)
    # print(cleanLine)
# print(data)
lengths = list(filter(lambda element: checkLengths(element) ,data))
print('result: ',len(lengths))
print("--- %s seconds ---" % (time.time() - startTime))
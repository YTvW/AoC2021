import sys
import fileinput
import time
import pandas as pd
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

population =[]
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    population =list(map(lambda p: int(p),cleanLine.split(',')))

for day in range(1,81):
    for fish in range(len(population)):
      if population[fish] == 0:
        population.append(8)
        population[fish]=6
      else:
        population[fish] -=1
    # print(day,population)
print('result: ',len(population))
print("--- %s seconds ---" % (time.time() - startTime))
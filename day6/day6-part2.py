import sys
import fileinput
import time
import itertools as it
import copy as cp
from numpy import floor
import pandas as pd
if len(sys.argv) >= 2:
    fileName = sys.argv[1]
else:
    fileName = "input"
days = 13
population = []
popDict = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    population = list(map(lambda p: int(p), cleanLine.split(',')))
    for entry in population:
        # print(entry)
        try:
            popDict[entry] = popDict[entry]+1
        except Exception as err:
            popDict[entry] = 1

for day in range(1, 257):
    temp=0
    if popDict[0] >= 1:
        temp+= popDict[0]

    popDict[0] = popDict[1]
    popDict[1] = popDict[2]
    popDict[2] = popDict[3]
    popDict[3] = popDict[4]
    popDict[4] = popDict[5]
    popDict[5] = popDict[6]
    popDict[6] = popDict[7]
    popDict[7] = popDict[8]
    popDict[8] =temp
    popDict[6]+=temp
    
print('result: ', sum(list(popDict.values())))
print("--- %s seconds ---" % (time.time() - startTime))

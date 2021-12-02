import sys
import fileinput
from re import search
import time

fileName = sys.argv[1]
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.encode("utf-8").strip("\n")
    print(cleanLine)


print("--- %s seconds ---" % (time.time() - startTime))
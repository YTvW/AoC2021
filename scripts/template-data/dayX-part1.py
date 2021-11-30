import sys
import fileinput
from re import search
import time
startTime = time.time()
for line in fileinput.input("./input7.txt"):
    cleanLine = line.encode("utf-8").strip("\n")
    print(cleanLine)


print("--- %s seconds ---" % (time.time() - startTime))
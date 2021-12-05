import sys
import fileinput
import time
import pandas as pd

if len(sys.argv) >= 2:
    fileName = sys.argv[1]
else:
    fileName = "input"

coordinates = {}


def setLine(Ax, Ay, Bx, By):
    y1 = 0
    y2 = 0
    x1 = 0
    x2 = 0
    if Ax == Bx:
        if Ay > By:
            y1 = By
            y2 = Ay
        else:
            y1 = Ay
            y2 = By
        for y in range(y1, y2+1):
            try:
                coordinates[(Ax, y)] = coordinates[(Ax, y)]+1
            except Exception as err:
                coordinates[(Ax, y)] = 1
    elif Ay == By:
        if Ax > Bx:
            x1 = Bx
            x2 = Ax
        else:
            x1 = Ax
            x2 = Bx
        for x in range(x1, x2+1):
            try:
                coordinates[(x, Ay)] = coordinates[(x, Ay)]+1
            except:
                coordinates[(x, Ay)] = 1


startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    coordAxs, coordAys = cleanLine.split(' -> ')[0].split(',')
    coordBxs, coordBys = cleanLine.split(' -> ')[1].split(',')
    coordAx = int(coordAxs)
    coordAy = int(coordAys)
    coordBx = int(coordBxs)
    coordBy = int(coordBys)

    setLine(coordAx,
            coordAy,
            coordBx,
            coordBy)

count = 0
for cord in coordinates.values():
    # print(cord)
    if cord >= 2:
        count += 1
print('result: ',count)
# print(xMin, xMax, yMin, yMax)
print("--- %s seconds ---" % (time.time() - startTime))

import sys
import fileinput
import time
from numpy import False_, NaN, True_
import pandas as pd
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

positions={}

startTime = time.time()

x = y= 0
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    y=0
    for char in cleanLine:
      positions[(x,y)] = int(char)
      y+=1
    x+=1
flashes=0

# for step in range(1,101):
step =0
while True:
  step+=1
  positionsToReset = []
  for entry in positions:
    positions[entry]+=1
  check = True
  while check:
    check=False
    for pos in positions:
      if positions[pos] > 9:
        check = True
        positions[pos] = NaN
        positionsToReset.append(pos)
        flashes+=1
        posX = pos[0]
        posY = pos[1]
        posToUpdate =[(posX-1,posY-1),(posX,posY-1),(posX+1,posY-1),(posX-1,posY),(posX+1,posY),(posX-1,posY+1),(posX,posY+1),(posX+1,posY+1)]
        for posUp in posToUpdate:
          try:
            positions[posUp] +=1
          except:
            continue

  for resetPos in positionsToReset:
    positions[resetPos] = 0
  
  if all(value == 0 for value in positions.values()):
    print('result: ',step)
    break

print("--- %s seconds ---" % (time.time() - startTime))
import sys
import fileinput
import time
import copy
import pandas as pd
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

coordinates={}
folds=[]
found=False
startTime = time.perf_counter()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if cleanLine == '':
      found = True
    elif not found:
      x, y = cleanLine.split(',')
      coordinates[(int(x),int(y))]='#'
    else:
      foldInfo = cleanLine.split()[2].split('=')
      folds.append((foldInfo[0],int(foldInfo[1])))

def foldCoords(coordinates, axis,val):
  oldCoords = copy.deepcopy(coordinates) 
  if axis == 'x':
    for coord in oldCoords:
      if coord[0]> val:
        coordinates[((val-(coord[0]-val)),coord[1])]=coordinates[coord]
        del coordinates[coord]
      else: 
        coordinates[coord] = '#'  
  if axis == 'y':    
    for coord in oldCoords:
      if coord[1]> val:
        coordinates[(coord[0],(val-(coord[1]-val)))]=coordinates[coord] 
        del coordinates[coord] 

def print_grid(coordinates):
  grid=[]
  maxX = sorted(list(map(lambda c: c[0],coordinates.keys())))[-1]
  maxY = sorted(list(map(lambda c: c[1],coordinates.keys())))[-1]
  for y in range(0,maxY+1):
    ys=[]
    for x in range(0,maxX+1):
      
      try:
        ys.append(coordinates[(x,y)])
      except:
        ys.append('.')
    grid.append(ys)
  df =pd.DataFrame(grid)
  print(df)

for fold in folds:
  foldCoords(coordinates,fold[0],int(fold[1]))

print_grid(coordinates)
print("--- %s seconds ---" % (time.perf_counter() - startTime))
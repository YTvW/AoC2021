import sys
import fileinput
import time
from itertools import product
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def activateCubes(cubes,xMin,xMax,yMin,yMax,zMin,zMax):
  xRange = list(range(xMin,xMax+1))
  yRange = list(range(yMin,yMax+1))
  zRange = list(range(zMin,zMax+1))
  cubesToActivate = list(product(xRange, yRange, zRange))
  cubes.update(cubesToActivate)

def deActivateCubes(cubes,xMin,xMax,yMin,yMax,zMin,zMax):
  xRange = list(range(xMin,xMax+1))
  yRange = list(range(yMin,yMax+1))
  zRange = list(range(zMin,zMax+1))
  cubesToDeActivate = list(product(xRange, yRange, zRange))
  for point in cubesToDeActivate:
    cubes.discard(point)
  
cubes=set()
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    action, data = line.strip("\n").split(' ')
    xdata,ydata,zdata = data.split(',')
    xMin,xMax = xdata.strip('x=').split('..')
    yMin,yMax = ydata.strip('y=').split('..')
    zMin,zMax = zdata.strip('z=').split('..')
    if action == 'on':
      activateCubes(cubes,int(xMin),int(xMax),int(yMin),int(yMax),int(zMin),int(zMax))
    elif action == 'off':
      deActivateCubes(cubes,int(xMin),int(xMax),int(yMin),int(yMax),int(zMin),int(zMax))

# print(cubes)
print(len(cubes))
print("--- %s seconds ---" % (time.time() - startTime))
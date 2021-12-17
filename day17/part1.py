import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def steps(pos,speed,target):
  posInTarget=False
  x,y = pos
  step=0
  maxY=0
  while not posInTarget:
    step +=1 
    x,y = pos
    if x >= target[0] and  x <= target[1] and y >= target[2] and  y <= target[3]:
      posInTarget = True
      break
    elif y < target[2] or x > target[1]:
      break
    else:
      pos[0]+= speed[0]
      pos[1]+= speed[1]
      if speed[0] > 0:
        speed[0]-=1
      elif speed[0] < 0:
        speed[0]+=1
      speed[1]-=1
      if pos[1]> maxY:
        maxY=pos[1]

  return step, posInTarget,maxY
  

target=[]
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    blocks =cleanLine.split()
    xTargetMin,xTargetMax= blocks[2].replace('x=',"").replace(',',"").split('..')
    yTargetMin,yTargetMax= blocks[3].replace('y=',"").replace(',',"").split('..')
    target.extend([int(xTargetMin),int(xTargetMax),int(yTargetMin),int(yTargetMax)])

startTime = time.time()
maxYval=0
for i in range(100):
  for j in range(100):
    step,result,maxY = steps([0,0],[i,j],target)
    if maxY > maxYval and result:
      maxYval =maxY
      speed=[i,j]

print(maxYval)

print("--- %s seconds ---" % (time.time() - startTime))

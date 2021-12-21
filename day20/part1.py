import sys
import fileinput
import time
from collections import defaultdict
from copy import deepcopy

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def printImage(image):
  img = deepcopy(image)
  sizeY = max([int(x[1]) for x in image.keys() ])+1
  sizeX = max([int(x[0]) for x in image.keys() ])+1
  minSizeY = min([int(x[1]) for x in image.keys() ])-1
  minSizeX = min([int(x[0]) for x in image.keys() ])-1
  for yp in range(minSizeY,sizeY):
    strP=""
    for xp in range(minSizeX,sizeX):
      strP += str(img[xp,yp]).replace('1','#').replace('0',' ')
    print(strP)

def decodePix(img,x,y,algo):
  index =""
  for pos in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
    num = 0
    if img[pos] ==1:
      num=1
    index += str(num)
  return int(algo[int(index,2)])

def filterDarkPx(image):
  newImage= deepcopy(image)
  for key,v in image.items():
    if int(v) == 0:
      del(newImage[key])
  return newImage

image=defaultdict(lambda:0)
lookup=''
startTime = time.time()
x =y=0
data =False
dataLen=0
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if data == True:
      x=0
      for entry in cleanLine:
        if entry == '#':
          image[(x,y)] = 1
        else:
          image[(x,y)] = 0
        x+=1
      y+=1
      dataLen=len(cleanLine)
    elif cleanLine == "":
      data = True
    else:
      lookup+= cleanLine.replace('#','1').replace(".",'0')

expansion=1
maxSizeY = y + expansion 
maxSizeX = dataLen + expansion 
minSizeY = -expansion
minSizeX = -expansion
for i in range(50):
  if i % 2 == 0:
    newImg = defaultdict(lambda:1)
  else:
    newImg = defaultdict(lambda:0)
  for y in range(minSizeY, maxSizeY + 1):
        for x in range(minSizeX, maxSizeX + 1):
            newImg[(x,y)] = decodePix(image, x, y, lookup)
  image = newImg
  minSizeY -= expansion
  minSizeX -= expansion
  maxSizeY += expansion
  maxSizeX += expansion

# printImage(image)
print("result: %d"%len([image[x] for x in image if image[x]==1]))

print("--- %s seconds ---" % (time.time() - startTime))
input("press enter to close.....")
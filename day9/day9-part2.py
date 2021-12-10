import sys
import fileinput
import time
import pandas as pd
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"


def checkNext(postitions,data,positionsChecked):
  positionsToCheck=[]
  checkedPositions=positionsChecked
  count=0
  for i in range(len(postitions)):
    try:
      position =postitions[i]
      value = data[position[0]][position[1]]
      if value != 9:
        count+=1
        positionsToCheck.extend([(position[0],position[1]-1),(position[0],position[1]+1),(position[0]+1,position[1]),(position[0]-1,position[1])])
    except:
      continue
  checkedPositions.extend(postitions)
  positionsToCheck = list(filter(lambda entry: -1 not in entry,list(set(positionsToCheck) - set(checkedPositions))))
  if len(positionsToCheck) >=1 :
    return count + checkNext(positionsToCheck,data,checkedPositions)
  else:
    return count

data=[]
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    data.append(list(map(lambda x:int(x),cleanLine)))
lowPoints =[]

for i in range(0,len(data)):
  row= data[i]
  for j in range(0,len(row)):
    column = row[j]
    # all entries in the middle
    if i>=1 and j>=1 and i < len(data)-1 and j < len(row)-1:
      if column<row[j-1] and  column<row[j+1]  and column < data[i-1][j] and column < data[i+1][j]  :
        lowPoints.append((i,j))
    # entries on the top middle
    elif i==0 and j >=1 and j < len(row)-1:
      if column<row[j-1] and  column<row[j+1]  and column < data[i+1][j]  :
        lowPoints.append((i,j))
    # entries on the right
    elif j == 0 and i >= 1 and i < len(data)-1:
      if  column<row[j+1]  and column < data[i-1][j] and column < data[i+1][j]:
          lowPoints.append((i,j))
      # entries on the right
    elif j == len(row)-1 and i >= 1 and i < len(data)-1:
      if  column<row[j-1]  and column < data[i-1][j] and column < data[i+1][j]:
          lowPoints.append((i,j))
    # entries on the top left
    elif i==0 and j ==0:
      if  column<row[j+1]  and column < data[i+1][j]:
        lowPoints.append((i,j))
    # entries on the top right
    elif i==0 and j == len(row)-1:
      if  column<row[j-1]  and column < data[i+1][j]:
        lowPoints.append((i,j))
    # entries on the bottom middle
    elif  i==len(data)-1 and j >=1 and j < len(row)-1:
      if  column<row[j-1]  and column<row[j+1]  and column < data[i-1][j]:
        lowPoints.append((i,j))
    # entries on the bottom left
    elif  i==len(data)-1 and j ==0:
        if  column<row[j+1]  and column < data[i-1][j]:
          lowPoints.append((i,j))
    # entries on the bottom right
    elif  i==len(data)-1 and j ==len(row)-1:
        if  column<row[j-1]  and column < data[i-1][j]:
          lowPoints.append((i,j))

basins=[]
for point in lowPoints:
  postitions = list(filter(lambda entry: -1 not in entry,[(point[0],point[1]-1),(point[0],point[1]+1),(point[0]+1,point[1]),(point[0]-1,point[1])]))
  sizeOfBasin = checkNext(postitions,data,[])
  # break;
  basins.append(sizeOfBasin)
  basins.sort()

print('result: ',( basins[-1]*basins[-2]*basins[-3]))
print("--- %s seconds ---" % (time.time() - startTime))
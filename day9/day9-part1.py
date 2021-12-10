import sys
import fileinput
import time
import pandas as pd
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"


data=[]
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    # print(cleanLine)
    data.append(list(map(lambda x:int(x),cleanLine)))
totalRisk =0

for i in range(0,len(data)):
  row= data[i]
  for j in range(0,len(row)):
    column = row[j]
    # all entries in the middle
    if i>=1 and j>=1 and i < len(data)-1 and j < len(row)-1:
      if column<row[j-1] and  column<row[j+1]  and column < data[i-1][j] and column < data[i+1][j]  :
        totalRisk+=(column+1)
    # entries on the top middle
    elif i==0 and j >=1 and j < len(row)-1:
      if column<row[j-1] and  column<row[j+1]  and column < data[i+1][j]  :
        totalRisk+=(column+1)
    # entries on the right
    elif j == 0 and i >= 1 and i < len(data)-1:
      if  column<row[j+1]  and column < data[i-1][j] and column < data[i+1][j]:
          totalRisk+=(column+1)
      # entries on the right
    elif j == len(row)-1 and i >= 1 and i < len(data)-1:
      if  column<row[j-1]  and column < data[i-1][j] and column < data[i+1][j]:
          totalRisk+=(column+1)
    # entries on the top left
    elif i==0 and j ==0:
      if  column<row[j+1]  and column < data[i+1][j]:
        totalRisk+=(column+1)
    # entries on the top right
    elif i==0 and j == len(row)-1:
      if  column<row[j-1]  and column < data[i+1][j]:
        totalRisk+=(column+1)
    # entries on the bottom middle
    elif  i==len(data)-1 and j >=1 and j < len(row)-1:
      if  column<row[j-1]  and column<row[j+1]  and column < data[i-1][j]:
        totalRisk+=(column+1)
    # entries on the bottom left
    elif  i==len(data)-1 and j ==0:
        if  column<row[j+1]  and column < data[i-1][j]:
          totalRisk+=(column+1)
    # entries on the bottom right
    elif  i==len(data)-1 and j ==len(row)-1:
        if  column<row[j-1]  and column < data[i-1][j]:
          totalRisk+=(column+1)
    


    # print(data[i][j])
print(totalRisk)
print("--- %s seconds ---" % (time.time() - startTime))
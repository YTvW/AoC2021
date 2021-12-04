import sys
import fileinput
import time
import pandas as pd
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"
frames = []
numbers=[]
boards = {}
boardNr=0
lineLength = 0
startTime = time.time()

for line in fileinput.input('./'+fileName+'.txt'):
  cleanLine = line.strip("\n")
  if cleanLine.find(',') >=0:
    numbers = cleanLine.split(',')
  elif len(cleanLine)==0:
    # print('nextBoard') 
    
    if boardNr >=1:
      frames.append(pd.DataFrame(boards[boardNr]))
    boardNr+=1
    boards[boardNr]=[]
    
  else:
    if lineLength == 0:
      lineLength = len(cleanLine.split())
    # print(boardNr)
    boards[boardNr].append(cleanLine.split())

frames.append(pd.DataFrame(boards[boardNr]))
# print(frames)



print("--- %s seconds ---" % (time.time() - startTime))
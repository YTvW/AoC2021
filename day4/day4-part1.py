from os import nice
import copy
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
    if boardNr >=1:
      frames.append(pd.DataFrame(boards[boardNr]))
    boardNr+=1
    boards[boardNr]=[]
  else:
    if lineLength == 0:
      lineLength = len(cleanLine.split())
    boards[boardNr].append(cleanLine.split())

winningFrame= None
frames.append(pd.DataFrame(boards[boardNr]))
updatedFrames=copy.deepcopy(frames)
winningNumber =-1
done = False

for i in range(len(numbers)):

  for frame in range(len(updatedFrames)):
    updatedFrames[frame].mask(updatedFrames[frame] == numbers[i],False,True)
    if updatedFrames[frame].nunique(axis = 0,dropna =False).eq(1).any() or updatedFrames[frame].nunique(axis = 1,dropna =False).eq(1).any():
      done = True
      winningNumber = numbers[i]
      winningFrame = updatedFrames[frame]
      break
  if done:
    break;

total = 0
for entry in winningFrame.values:
  for value in entry:
    if type(value) == str:
      total+= int(value)

print("result: %d " %int(total*int(winningNumber)))
print("--- %s seconds ---" % (time.time() - startTime))
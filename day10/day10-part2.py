import sys
import fileinput
import time
from math import floor
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

totalScores=[]
failedLines=[]
startTime = time.time()

for line in fileinput.input('./'+fileName+'.txt'):
    groupsOpeners ={'{':1197,'[':57,'<':25137,'(':3}
    groupsClosers ={'}':1197,']':57,'>':25137,')':3}
    groups =[]
    cleanLine = line.strip("\n")
    failedChar = ''
    for i in range(len(cleanLine)):
      if cleanLine[i] in groupsOpeners.keys():
        groups.append(cleanLine[i])
      elif cleanLine[i] == ']':
          if groups[-1] == '[':
            groups.pop(-1)
          else:
            failedChar = cleanLine[i]
            break
      elif cleanLine[i] == '}':
          if groups[-1] == '{':
            groups.pop(-1)
          else:
            failedChar = cleanLine[i]
            break
      elif cleanLine[i] == ')':
          if groups[-1] == '(':
            groups.pop(-1)
          else:
            failedChar = cleanLine[i]
            break
      elif cleanLine[i] == '>':
          if groups[-1] == '<':
            groups.pop(-1)
          else:
            failedChar = cleanLine[i]
            break
    if failedChar != '':
      failedChar = ''
    else:
      scores ={'{':3,'[':2,'<':4,'(':1}
      tempScore=0
      groups.reverse()
      for entry in groups:
        tempScore= tempScore*5 + scores[entry]

      totalScores.append(tempScore)
      # print('\n')
totalScores.sort()
print('result: ',totalScores[floor(len(totalScores)/2)])
print("--- %s seconds ---" % (time.time() - startTime))
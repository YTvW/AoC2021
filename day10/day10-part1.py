import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

totalScore=0
failedLines=[]
startTime = time.time()

for line in fileinput.input('./'+fileName+'.txt'):
    groupsOpeners ={'{':1197,'[':57,'<':25137,'(':3}
    groupsClosers ={'}':1197,']':57,'>':25137,')':3}
    groups =[]
    cleanLine = line.strip("\n")
    failedChar = ''
    if  True: #len(cleanLine) % 2 == 0:
      for i in range(len(cleanLine)):
        if cleanLine[i] in groupsOpeners.keys():
          # groups[cleanLine[i]]+=1
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
      
      failedLines.append(cleanLine)
      totalScore+= groupsClosers[failedChar]
      failedChar = ''
   
print('result: ',totalScore)
print("--- %s seconds ---" % (time.time() - startTime))
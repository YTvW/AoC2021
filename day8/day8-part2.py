import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

data = []

def stringDif(s1,s2):
  set1= set(s1)
  set2 = set(s2)
  return list(set1.symmetric_difference(set2))

def findOcurances(signalPaterns,count):
  temp =[]
  for letter in ["a","b","c","d","e","f","g"]:
    amount = signalPaterns.count(letter)
    if amount == count:
      temp.append(letter)
  return temp

def determineSegments(signalPaterns):
    segmentMap={0:'',1:'',2:'',3:'',4:'',5:'',6:''}
    numbersMap={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
    sp = signalPaterns.split(' ')
    sp = sorted(sp,key=len)
    #   0
    #1    2
    #   3
    #4    5
    #   6 
    numbersMap[1]=sp[0]
    numbersMap[4]=sp[2]
    numbersMap[7]=sp[1]
    numbersMap[8]=sp[9]
    segmentMap[0]=stringDif(numbersMap[1],numbersMap[7])[0]
    segmentMap[1]=findOcurances(signalPaterns,6)[0]
    segmentMap[4]=findOcurances(signalPaterns,4)[0]
    segmentMap[5]=findOcurances(signalPaterns,9)[0]
    segmentMap[2]=list(filter(lambda seg: seg != segmentMap[0] ,findOcurances(signalPaterns,8)))[0]
    segmentMap[3]=numbersMap[4].replace(segmentMap[1],"").replace(segmentMap[2],"").replace(segmentMap[5],"")
    segmentMap[6]=list(filter(lambda seg: seg != segmentMap[3] ,findOcurances(signalPaterns,7)))[0]
    numbersMap[0]= numbersMap[8].replace(segmentMap[3],"")
    numbersMap[6]= numbersMap[8].replace(segmentMap[2],"")
    numbersMap[9]= numbersMap[8].replace(segmentMap[4],"")
    numbersMap[2]= numbersMap[8].replace(segmentMap[1],"").replace(segmentMap[5],"")
    numbersMap[3]= numbersMap[8].replace(segmentMap[1],"").replace(segmentMap[4],"")
    numbersMap[5]= numbersMap[8].replace(segmentMap[2],"").replace(segmentMap[4],"")
    return dict([(value, key) for key, value in numbersMap.items()])

startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n").split(' | ')
    data.append(cleanLine)

result=0
for element in data:
  map = determineSegments(element[0])
  number=''
  for digit in element[1].split():
    for key in map:
      if set(digit)== set(key):
        number+= str(map[key])
  result+=int(number)

print('result: ',result)
print("--- %s seconds ---" % (time.time() - startTime))
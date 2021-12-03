import sys
import fileinput
from socket import htons
import numpy as np
from re import search
import time


if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"
dataLen=0
# bits={}
data=[]
bitLines0 ={}
bitLines1 ={}
lines=0
gamma=np.uint8(0b0000000000)
epsilon =np.uint8(0b00000000000)
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    
    cleanLine = line.strip("\n")
    lines+=1
    if dataLen == 0:
      dataLen=len(cleanLine)
    data.append(cleanLine)

def countBits(data):
  bits={}
  for i in range(0,dataLen,1):
        bits[i] =0
  for line in data:
    for i in range(0,dataLen,1):
      if line[i] == '1':
        bits[i] +=1
  return bits

def determineCo2(data,bit):
  bits = countBits(data)
  tempData = []
  if bits[bit] >= (len(data)/2):
    tempData = list(filter(lambda x: x[bit] =='0',data))
  else:
    tempData = list(filter(lambda x: x[bit] =='1',data))
    
  if len(tempData)==1:
    return int(tempData[0],2)
  else:
    return determineCo2(tempData,bit+1)

def determineOxygen(data,bit):
  bits = countBits(data)
  tempData = []
  if bits[bit] >= (len(data)/2):
    tempData = list(filter(lambda x: x[bit] =='1',data))
  else:
    tempData = list(filter(lambda x: x[bit] =='0',data))
    
  if len(tempData)==1:
    return int(tempData[0],2)
  else:
    return determineOxygen(tempData,bit+1)

oxygen = determineOxygen(data,0)
co2 = determineCo2(data,0)

print('result: %d'% (co2*oxygen) )
print("--- %s seconds ---" % (time.time() - startTime))

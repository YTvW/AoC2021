import sys
import fileinput
import time
from math import floor, prod
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

hexToBinMap={
  '0' : '0000',
  '1' : '0001',
  '2' : '0010',
  '3' : '0011',
  '4' : '0100',
  '5' : '0101',
  '6' : '0110',
  '7' : '0111',
  '8' : '1000',
  '9' : '1001',
  'A' : '1010',
  'B' : '1011',
  'C' : '1100',
  'D' : '1101',
  'E' : '1110',
  'F' : '1111',
}

def decodeBytes(data,level=0):
  offset = 0
  packetVersion = int(data[offset:offset+3],2)
  offset+=3
  packetType = int(data[offset:offset+3],2)
  offset+=3
  value=None
  if packetType == 0:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(nrOfSubPackets):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    value = sum(values)
  elif packetType == 1:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(nrOfSubPackets):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    value = prod(values)
  elif packetType == 2:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(nrOfSubPackets):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    value = min(values)
  elif packetType == 3:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(nrOfSubPackets):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    value = max(values)
  elif packetType == 4:
    resultString=""
    busy = True
    while busy:
      group = data[offset:offset+5]
      resultString+=group[1::]
      if group[0] == '0':
        offset+=5
        break
      offset+=5
    value = int(resultString,2)
  elif packetType == 5:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(2):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    if values[0]> values[1]:
      value = 1
    else:
      value=0
  elif packetType == 6:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(2):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    if values[0] < values[1]:
      value = 1
    else:
      value=0
  elif packetType == 7:
    lengthTypeId = int(data[offset])
    offset+=1
    values =[]
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,value = decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
        used+=usedBytes
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(2):
        usedBytes,value =decodeBytes(data[offset::],level+1)
        values.append(value)
        offset+=usedBytes
    if values[0] == values[1]:
      value = 1
    else:
      value=0
  return offset, value

fullData =""
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    fullData =""
    for char in cleanLine:
      fullData += hexToBinMap[char]
    offset,result = decodeBytes(fullData)
    print('result: ',result)
print("--- %s seconds ---" % (time.time() - startTime))
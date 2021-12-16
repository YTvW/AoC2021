import sys
import fileinput
import time
from math import floor
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
  versions=[]
  offset = 0
  packetVersion = int(data[offset:offset+3],2)
  versions.append(packetVersion)
  offset+=3
  packetType = int(data[offset:offset+3],2)
  offset+=3
  if packetType == 4:
    resultString=""
    busy = True
    while busy:
      group = data[offset:offset+5]
      resultString+=group[1::]
      if group[0] == '0':
        offset+=5
        break
      offset+=5
  elif packetType == 4:
  else:
    lengthTypeId = int(data[offset])
    offset+=1
    if lengthTypeId == 0:
      bitsInsSubPackets = int(data[offset:offset+15],2)
      offset+=15
      used=0
      while used < bitsInsSubPackets:
        usedBytes,newVersion = decodeBytes(data[offset::],level+1)
        offset+=usedBytes
        used+=usedBytes
        versions.extend(newVersion)
    else:
      nrOfSubPackets = int(data[offset:offset+11],2)
      offset+=11
      for i in range(nrOfSubPackets):
        usedBytes,newVersion =decodeBytes(data[offset::],level+1)
        offset+=usedBytes
        versions.extend(newVersion)
  print(versions,packetType)
  input("Press Enter to continue...")

  return offset,versions

fullData =""
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    # print(cleanLine)
    for char in cleanLine:
      fullData += hexToBinMap[char]

    # print (fullData)
    offset,versions = decodeBytes(fullData)
    # print(offset,versions)
    print('result: ',sum(versions))
print("--- %s seconds ---" % (time.time() - startTime))
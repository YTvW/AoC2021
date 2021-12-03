import sys
import fileinput
from socket import htons
import numpy as np

from re import search
import time

def toggleBit(int_type, offset):
  mask = 1 << offset
  return(int_type ^ mask)

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"
dataLen=0
bits={}
lines=0
gamma=np.uint8(0b0000000000)
epsilon =np.uint8(0b00000000000)
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    
    cleanLine = line.strip("\n")
    lines+=1
    # print(cleanLine)
    if dataLen == 0:
      dataLen=len(cleanLine)
      for i in range(0,dataLen,1):
        bits[i] =0
    for i in range(0,dataLen,1):
      if cleanLine[i] == '1':
        bits[i] +=1

for bit in range(0,dataLen,1):
  print(bits[bit],lines/2)
  if bits[bit] > (lines/2):
    gamma = gamma | (1<<dataLen-bit)
    epsilon = epsilon & ~(1<<bit)
  else:
    gamma = gamma & ~(1<<dataLen-bit)
    epsilon = epsilon | (1<<bit)

gamma = gamma>>1
epsilon = gamma ^ 0xFFF

# print('gammaBin:  ',bin((gamma)))
# print('epsilonBin:',bin((~gamma)))
# print('gamma:',int(gamma))
# print('epsilon:',int(epsilon ))
print('result: %d'% (gamma*epsilon) )
print("--- %s seconds ---" % (time.time() - startTime))
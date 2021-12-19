import sys
import fileinput
import time
from copy import deepcopy
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def depth(L): return isinstance(L, list) and max(map(depth, L))+1

def checkExplode(data):
  level = depth(data)
  if level >4:
    return True
  return False

def levels(l, depth = -1):
    if not isinstance(l, list):
        yield (l, depth)
    else:
        for sublist in l:
            yield from levels(sublist, depth + 1)

def reduce(data):
  
  
  pass


def explode(data):
  while checkExplode(data):
    
    pass
  pass

def split(data,pair):

  pass

def stringToArray(str,level=0):
  # print('level: ',level)
  arr=[]
  values=[]
  offset=0
  
  while offset<len(str):
    c = str[offset]
    offset+=1
    if c == '[':
      used,val =stringToArray(str[offset::],level+1)
      values.append(val)
      offset+=used
    elif c == ']':
      break
    elif c.isdigit():
      values.append(int(c))
    else:
      continue
  arr.extend(values)
  return offset, arr

lastLine=str()
tempLine=str()
lastArr=[]
data=[]
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    array = stringToArray(cleanLine)[1][0]
    if len(lastArr)>=1:
      data=[lastArr,array]
      print('data: ',data)

      lastArr=deepcopy(data)
    else:
      lastArr = deepcopy(array)
# print(data)

temp =[[[[[9,8],1],2],3],4]
print(checkExplode(temp))
print(list(levels(temp)))

# l = "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"
# print(l)
# # data = stringToArray(l)[1][0]
# print(data[1])
# print(stringToArray(l)[1][0])

print("--- %s seconds ---" % (time.time() - startTime))
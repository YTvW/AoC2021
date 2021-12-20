import sys
import fileinput
import time
from itertools import product
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

# def distance(A,B):
#   d =  ((A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2)**0.5
#   return d

def rotateScanner(scanner):
    rotations = []
    for i in range(24):
        rotations.append([])
    for coord in scanner:
        #positive x
        rotations[ 0].append((+coord[0],+coord[1],+coord[2]))
        rotations[ 1].append((+coord[0],-coord[2],+coord[1]))
        rotations[ 2].append((+coord[0],-coord[1],-coord[2]))
        rotations[ 3].append((+coord[0],+coord[2],-coord[1]))
        #negative x
        rotations[ 4].append((-coord[0],-coord[1],+coord[2]))
        rotations[ 5].append((-coord[0],+coord[2],+coord[1]))
        rotations[ 6].append((-coord[0],+coord[1],-coord[2]))
        rotations[ 7].append((-coord[0],-coord[2],-coord[1]))
        #positive y
        rotations[ 8].append((+coord[1],+coord[2],+coord[0]))
        rotations[ 9].append((+coord[1],-coord[0],+coord[2]))
        rotations[10].append((+coord[1],-coord[2],-coord[0]))
        rotations[11].append((+coord[1],+coord[0],-coord[2]))
        #negative y
        rotations[12].append((-coord[1],-coord[2],+coord[0]))
        rotations[13].append((-coord[1],+coord[0],+coord[2]))
        rotations[14].append((-coord[1],+coord[2],-coord[0]))
        rotations[15].append((-coord[1],-coord[0],-coord[2]))
        #positive z
        rotations[16].append((+coord[2],+coord[0],+coord[1]))
        rotations[17].append((+coord[2],-coord[1],+coord[0]))
        rotations[18].append((+coord[2],-coord[0],-coord[1]))
        rotations[19].append((+coord[2],+coord[1],-coord[0]))
        #negative z
        rotations[20].append((-coord[2],-coord[0],+coord[1]))
        rotations[21].append((-coord[2],+coord[1],+coord[0]))
        rotations[22].append((-coord[2],+coord[0],-coord[1]))
        rotations[23].append((-coord[2],-coord[1],-coord[0]))
    return rotations

map=[]
scanners={}
scannerCount=-1
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if cleanLine.find("scanner")>0:
      scannerCount+=1
      scanners[scannerCount]=[]#{"points":{}}
    elif len(cleanLine) >= 1:
      x,y,z = cleanLine.split(',')
      scanners[scannerCount].append(((int(x),int(y),int(z))))#]={}
scannerCount+=1
scanners[scannerCount]=[]
# print(scanners)
scan = scanners.pop(0)
for nr,scanner in scanners.items():
  try:
    s2 = scanners[nr+1]
  except:
      pass
  
  
  print(scanner)

# print(rotateScanner(scanners[0]))

# matchDist(scanners)

print("--- %s seconds ---" % (time.time() - startTime))


# for i,scanner in scanners.items():
  # print(scanner)
  # dis= list(product(scanner['points'],scanner['points']))
  # print(dis)
  # distances =[]
  # for A,B in dis:
    # dist = distance(A,B)
    # distances.append(dist)
    # scanners[i]['points'][A][B]=dist
    # scanners[i]['points'][B][A]=dist
  # scanners[i]['distances']=distances

# def matchDist(scanners):
#   matches=[]
#   for i,scanner in scanners.items():
#     print('scanner: ',i)
#     for j,point in scanner['points'].items():
#       for k,entry in point.items():

#         print("entry: ",j,k, entry)
#     # if i == 1:
#     #   break
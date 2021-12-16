import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
  size=10
else:
  fileName = "input"
  size= 100

y =0
def findNeighbours(grid,node):
  x,y=node
  xMax = len(grid[0])-1
  yMax = len(grid)-1
  # print(xMax,yMax)
  # print(node)
  potentialNeighbours=[]#[(x,y-1),(x-1,y),(x+1,y),(x,y+1)]
  if x > 0 and x < xMax:
    potentialNeighbours.extend([(x+1,y),(x-1,y)])
  if y > 0 and y < yMax:
    potentialNeighbours.extend([(x,y+1),(x,y-1)])
  if x == 0:
    potentialNeighbours.append((x+1,y))
  if x == xMax:
    potentialNeighbours.append((x-1,y))
  if y == 0:
    potentialNeighbours.append((x,y+1))
  if y == yMax:
    potentialNeighbours.append((x,y-1))

  # potentialNeighbours=[(x+1,y),(x,y+1)]

  return potentialNeighbours
  # return list(filter(lambda n: n in grid,potentialNeighbours))
grid=[]
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    grid.append(line.strip('\n'))


# print(grid)
risk = {(0,0):0}

visited = set()
for q in range(size**2):

      node = min(visited.symmetric_difference(risk),key= risk.get)
      neighbours = findNeighbours(grid,node)
      # print(node)
      for i,j in neighbours:
        # print(grid)
        val = risk[node]+int(grid[i][j])
        # print('val: ',val)
        if (i,j )in risk:
          if val < risk[(i,j)]:
            risk[i,j]=val
        else:
          risk[(i,j)]= val
      visited.add(node)

      if node == (size-1,size-1):
        print(risk[(size -1,size-1)])
        break


print("--- %s seconds ---" % (time.time() - startTime))

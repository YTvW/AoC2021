import sys
import fileinput
import time
from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    previous = dict()

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        print(previous)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        previous[neighbor]=current_vertex
    return previous,D


if len(sys.argv) >=2:
  fileName = sys.argv[1]
  size=5
else:
  fileName = "input"
  size= 100

map={}
y =0
coords=[]
points=[]
def findNeighbours(nodes,node):
  x,y=node
  potentialNeighbours=[(x,y-1),(x-1,y),(x+1,y),(x,y+1)]
  # potentialNeighbours=[(x+1,y),(x,y+1)]
  return list(filter(lambda n: n in nodes,potentialNeighbours))
graph = Graph(9)
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    coords.append(cleanLine)
    for x,risk in enumerate(cleanLine):
      map[(x,y)]=int(risk)
      # points.append(int(risk))

      # graph.add_edge(x,y,int(risk))
    y+=1
print(map)
graph2 = Graph(size*size)
for i, entry in enumerate(map):
  neighbours = findNeighbours()
  graph2.add_edge(i,i,int(map[entry]))
graph.add_edge(0, 1, 4)
graph.add_edge(0, 6, 7)
graph.add_edge(1, 6, 11)
graph.add_edge(1, 7, 20)
graph.add_edge(1, 2, 9)
graph.add_edge(2, 3, 6)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 4, 10)
graph.add_edge(3, 5, 5)
graph.add_edge(4, 5, 15)
graph.add_edge(4, 7, 1)
graph.add_edge(4, 8, 5)
graph.add_edge(5, 8, 12)
graph.add_edge(6, 7, 1)
graph.add_edge(7, 8, 3) 
for edge in graph.edges:
  print(edge)
path,res = dijkstra(graph,0)
print(res)
print(path)


def calculateCost(path,nodes):
  cost =0
  for node in path:
    cost += nodes[node]
  return cost

def findPaths(nodes, start, end, limit, path=[]):
  paths = []
  if not path:
    path = [0]
  path = path + [start] 
  if start != (0,0):
    path[0] += nodes[start]
  if start == end:
    return [path]
  if len(path) > limit + 1:
    return None
  
  neighbours = findNeighbours(nodes, start)
  for node in neighbours:
    if node not in path:
      
      newPaths = findPaths(nodes, node, end, limit, path)
      if newPaths:
        paths.extend(newPaths)
  return paths

# result= findPaths(map,(0,0),(9,9),18)
# # print(result)
# counts=[]
# for p in result:
#   # print(p)
#   counts.append(p[0])
# s=sorted(counts)
# print(s[0])
# print(len(counts))

print("--- %s seconds ---" % (time.time() - startTime))
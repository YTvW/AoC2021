import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path or (node in path and node.isupper()):
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                  paths.append(newpath)
        return paths

caves ={}
paths= []
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    c1,c2 = line.strip("\n").split('-')
    
    if c1 in caves: caves[c1].append(c2)
    else: caves[c1] = [c2]
    if c2 in caves: caves[c2].append(c1)
    else: caves[c2] = [c1]

# print('caves: ',caves)
paths = find_all_paths(caves,'start','end')
print('results: ',len(paths))
print("--- %s seconds ---" % (time.time() - startTime))
import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def find_paths(caves, start, end, paths=[],path=[]):
        # paths =[]
        path = path + [start]
        if start == end:
            return path
        # print(caves[start][0].isupper())
        for node in caves[start]:
            print(node)
            if node not in path or (node in path and node.isupper()):
                newpath = find_paths(caves, node, end,paths, path)
                if newpath: 
                  return newpath
        # print(paths)
        

caves ={}
paths= []
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    c1,c2 = line.strip("\n").split('-')
    
    if c1 in caves: caves[c1].append(c2)
    else: caves[c1] = [c2]
    if c2 in caves: caves[c2].append(c1)
    else: caves[c2] = [c1]

print('caves: ',caves)
# for nodes in caves['start']:
paths.extend(find_paths(caves,'start','end',[],[]))

print(paths)
print("--- %s seconds ---" % (time.time() - startTime))
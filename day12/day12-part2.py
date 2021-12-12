import sys
import fileinput
import time
from collections import Counter
if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def duplicateCheck(path):
  check = False
  counter = Counter(filter(lambda x: x.islower(),path[1::]))

  for key in counter:
    if counter[key]>2:
      return False
    elif counter[key]>1:
      if check:
        return False
      else:
        check = True
  return True

def find_all_paths(caves, start, end, path=[]):
        if not path:
          path = path + [False]
        path = path + [start]
        if start == end:
            return [path]
        paths = []

        for node in caves[start]:
            if node == 'start':
              continue
            if node not in path or (node in path and node.isupper()):
                newpaths = find_all_paths(caves, node, end, path)
                # for newpath in newpaths:
                paths.extend(newpaths)
            elif node in path and node.islower():
                if path[0]:
                  continue
                elif duplicateCheck(path+[node]):
                  newpaths = find_all_paths(caves, node, end, path)
                  paths.extend(newpaths)
                else:
                 path[0]=True
                 continue
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

paths = find_all_paths(caves,'start','end')
print('results: ',len(paths))
print("--- %s seconds ---" % (time.time() - startTime))

#12.589
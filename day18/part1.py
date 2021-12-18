import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

def explode(data,pair):
  

  pass

def split(data,pair):

  pass
def stringToArray(str):
  arr=[]

  for i,c in enumerate(str):
    print(c)
    if c == '[':
      stringToArray(str[i::])
    elif c == ']':
      return str[::i]
  pass


lastLine=str()
tempLine=str()
startTime = time.time()
for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if len(lastLine)>=1:
      # input("Press Enter to continue...")
      tempLine= f'[{lastLine},{cleanLine}]'
      lastLine=tempLine
    else:
      lastLine = cleanLine
    
    # print(tempLine)

l = "[1,1]"
print(stringToArray(l))

print("--- %s seconds ---" % (time.time() - startTime))
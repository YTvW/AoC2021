import sys
import fileinput
import time

if len(sys.argv) >=2:
  fileName = sys.argv[1]
else:
  fileName = "input"

p1 = p2 =p1Score = p2Score =0
diceRoll =1
diceRolls=0
board=[10,1,2,3,4,5,6,7,8,9]
universes={}




for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if p1 ==0:
      p1= int(cleanLine.split(': ')[1])
    elif p2 ==0:
      p2= int(cleanLine.split(': ')[1])

def roll(p,score,currentDie):
  pass

startTime = time.time()
while p1Score < 1000 and p2Score <1000:
  rolled = diceRoll +(diceRoll+1)+(diceRoll+2)
  
  p1 =  (p1 + rolled)%10
  p1Score += board[p1]
  diceRoll += 3
  diceRolls+=3
  if p1Score >= 1000:
    break
  
  rolled = diceRoll +(diceRoll+1)+(diceRoll+2)
  p2 = (p2 + rolled)%10
  p2Score += board[p2]
  diceRoll += 3
  diceRoll = diceRoll%100
  diceRolls+=3

scores = [p1Score,p2Score]
print('result: ',diceRolls*min(scores))
print("--- %s mS ---" % ((time.time() - startTime)/1000))
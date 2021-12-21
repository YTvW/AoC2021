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

for line in fileinput.input('./'+fileName+'.txt'):
    cleanLine = line.strip("\n")
    if p1 ==0:
      p1= int(cleanLine.split(': ')[1])
    elif p2 ==0:
      p2= int(cleanLine.split(': ')[1])

startTime = time.time()
while p1Score < 1000 and p2Score <1000:
  #do role else break
  # p1
  rolled = diceRoll +(diceRoll+1)+(diceRoll+2)
  
  p1 =  (p1 + rolled)%10
  p1Score += board[p1]
  diceRoll += 3
  diceRolls+=3
  if p1Score >= 1000:
    break
  #p2
  rolled = diceRoll +(diceRoll+1)+(diceRoll+2)
  # p2Score += (p2 + (rolled %10))%10
  p2 = (p2 + rolled)%10
  p2Score += board[p2]
  diceRoll += 3
  diceRoll = diceRoll%100
  diceRolls+=3

  # print('dice: ',diceRoll)
  # print("p1Pos: ",p1)
  # print("p2Pos: ",p2)
  # print("p1Score: ",p1Score)
  # print("p2Score: ",p2Score)
  # print("dice Rolled: ",diceRolls)
  # input('press enter to continue ')
scores = [p1Score,p2Score]
print('result: ',diceRolls*min(scores))
print("--- %s seconds ---" % (time.time() - startTime))
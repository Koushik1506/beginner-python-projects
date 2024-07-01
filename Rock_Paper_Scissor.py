import random
print("welcome to \"ROCK PAPER SCISSOR\" game")
pp=0
cp=0
turn=1
draws=0
while turn<=10:
  g=random.choice(["ROCK","PAPER","SCISSOR"])
  t=input("Choose R for Rock\nChoose P for Paper\nChoose S for Scissor: ").upper()
  if g=="ROCK" and t=="S":
    print(f"Computer Chose {g}")
    print("-----You Loose!------")
    cp+=1
  elif g=="ROCK" and t=="P":
    print(f"Computer Chose {g}")
    print("-----You Win!--------")
    pp+=1
  elif g=="PAPER" and t=="R":
    print(f"Computer Chose {g}")
    print("------You Loose!------")
    cp+=1
  elif g=="PAPER" and t=="S":
    print(f"Computer Chose {g}")
    print("------You Win!------")
    pp+=1
  elif g=="SCISSOR" and t=="P":
    print(f"Computer Chose {g}")
    print("------You Loose!------")
    cp+=1
  elif g=="SCISSOR" and t=="R":
    print(f"Computer Chose {g}")
    print("------You Win!------")
    pp+=1
  else:
    print(f"Computer Chose {g}")
    print("Draw!")
    draws+=1
  turn+=1
print("-------------------GAME OVER------------------")
if pp>cp:
  print("Congats!!! Your are Final Winner!!!")
elif pp<cp:
  print("Computer is the Final Winner!!!")
else:
  print("It is a Final Draw")
turns=turn-1
print(f"Total No.of Turns are {turns}")
print(f"Your Total Score is {pp}")
print(f"Computer Total Score is {cp}")
print(f"No.of Draws are {draws}")

import random
print("welcome to \"ROCK PAPER SCISSOR\" game")
Player_points=0
Computer_points=0
turn=1
draws=0
while turn<=10:
  g=random.choice(["ROCK","PAPER","SCISSOR"])
  t=input("Choose R for Rock\nChoose P for Paper\nChoose S for Scissor: ").upper()
  if g=="ROCK" and t=="S":
    print(f"Computer Chose {g}")
    print("-----You Loose!------")
    Computer_points+=1
  elif g=="ROCK" and t=="P":
    print(f"Computer Chose {g}")
    print("-----You Win!--------")
    Player_points+=1
  elif g=="PAPER" and t=="R":
    print(f"Computer Chose {g}")
    print("------You Loose!------")
    Computer_points+=1
  elif g=="PAPER" and t=="S":
    print(f"Computer Chose {g}")
    print("------You Win!------")
    Player_points+=1
  elif g=="SCISSOR" and t=="P":
    print(f"Computer Chose {g}")
    print("------You Loose!------")
    Computer_points+=1
  elif g=="SCISSOR" and t=="R":
    print(f"Computer Chose {g}")
    print("------You Win!------")
    Player_points+=1
  else:
    print(f"Computer Chose {g}")
    print("Draw!")
    draws+=1
  turn+=1
print("-------------------GAME OVER------------------")
if Player_points>Computer_points:
  print("Congats!!! Your are Final Winner!!!")
elif Player_points<Computer_points:
  print("Computer is the Final Winner!!!")
else:
  print("It is a Final Draw")
turns=turn-1
print(f"Total No.of Turns are {turns}")
print(f"Your Total Score is {Player_points}")
print(f"Computer Total Score is {Computer_points}")
print(f"No.of Draws are {draws}")

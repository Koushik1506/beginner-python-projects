Hidden_Number=22
Number_of_Guess=1
print("Welcome to \"Number Guess\" game")
print("You've to Guess the Hidden Number between 1 to 50")
print("Your guesses are limited to 6 only")
while Number_of_Guess<=6:
  a=int(input("Enter Your Guess:"))
  if a>Hidden_Number:
    print("Your Guess was Greater than Hidden Number")
  elif a<Hidden_Number:
    print("Your Guess was Smaller than Hidden Number")
  else:
    print("Yes! you have Won!!!")
    break
  print("Number of Guesses left:",6-Number_of_Guess)
  Number_of_Guess+=1
print("Number of Guesses you took:",Number_of_Guess)
if Number_of_Guess>6:
  print("Game Over!!!")
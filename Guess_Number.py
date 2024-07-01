n=22
ng=1
print("Welcome to \"Number Guess\" game")
print("You've to Guess the Hidden Number between 1 to 50")
print("Your guesses are limited to 6 only")
while ng<=6:
  a=int(input("Enter Your Guess:"))
  if a>n:
    print("Your Guess was Greater than Hidden Number")
  elif a<n:
    print("Your Guess was Smaller than Hidden Number")
  else:
    print("Yes! you have Won!!!")
    break
  print("Number of Guesses left:",6-ng)
  ng+=1
print("Number of Guesses you took:",ng)
if ng>6:
  print("Game Over!!!")
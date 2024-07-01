qns=["What is capital of India?", "Who invented Electric Bulb?","Wh\o is the Father of Computer?"]
fm=0
for i in qns:
  print(i)
  match i:
     case "What is capital of India?":
       print("Your options are\n A. New Delhi\n B. Kolkata\n C. Banglore\n D. Chennai")
       a=input("Choose Your Option: ")
       if a=="A" or a=="a":
         fm+=100000
         print("Correct Answer\nYou Won Rs.",fm)
       else:
         print("Incorrect Answer ")
         print("Your final amount: ",fm)
         break
       print("\n")
     case "Who invented Electric Bulb?":
       print("Your options are\n A. Isaac Newton\n B. Galileo\n C. Albert Einstein\n D. Thomas Alva Edison")
       c=input("Choose Your Option: ")
       if c=="D" or c=="d":
         fm+=4900000
         print("Correct Answer\nYou Won Rs.", fm)
       else:
         print("Incorrect Answer ")
         print("Your final amount: ",fm)
         break
       print("\n")
     case "Who is the Father of Computer?":
       print("Your options are\n A. Jan Koum\n B. Mark Dean\n C. Charles Babbage\n D. Hamza")
       b=input("Choose Your Option: ")
       if b=="C" or b=="c":
         fm+=5000000
         print("\"Congratulations\"!!! You got all Correct answers. You won Rs: ",fm)
       else:
         print("Incorrect Answer ")
         print("Your final amount: ",fm)
         break 
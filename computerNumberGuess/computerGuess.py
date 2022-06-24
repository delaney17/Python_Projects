import random

guess = 0
x = 0
winningNum = int(input("What number do you choose? (between 1 and 10) "))
# while guess != winningNum and x <= 10:
while True: 
 guess=random.randint(1,10)
 print(f"Computer's guess: {guess}")
#   x+=1
# winningNum = int(input("What number do you choose? (between 1 and 10) "))
 if guess == winningNum: 
      print ("Computer got it!") 
      break
 else:
      print ("Incorrect, guess again") 
        




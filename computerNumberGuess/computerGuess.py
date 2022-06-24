import random

guess = 0
x = 0
winningNum = int(input("What number do you choose? (between 1 and 10) "))
while x<10: 
 guess=random.randint(1,10)
 print(f"Computer's guess: {guess}")
 x+=1
 if guess == winningNum: 
      print ("You lose! Computer guessed your number!") 
      break
 else:
      print ("Incorrect, guess again") 
      if x>=10:
         print("You win! Computer failed to guess number 10 times")




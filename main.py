import random
import time
from colored import fg

colory = fg('red')
colora = fg('blue')
colork = fg('yellow')
colori = fg('green')

print(colori + "Hello, this is the number guessing game, you have five guesses to guess the number between 0 and 100!")
time.sleep(5)

userName = input("What is your name? ")
randomNumber = random.randint(0,100)

randomNumber = random.randint(0,100)
print( "\nHello,", userName.capitalize(), ", lets begin!")

Guesses = 0
totalGuesses = 5

# create a variable "totalGuess" and assign it to how many times the user can guess
while Guesses < 5:
  
  Guess = int(input(colory+ "Guess a number between 0 and 100: "))
  
  Guesses += 1
  Guessesleft = totalGuesses - Guesses
  
  if Guess == randomNumber:
     break
  if Guess < randomNumber:
    print("\nnope, too small you have", Guessesleft , "Guesses left!" )
  if Guess > randomNumber:
    print("\nnope, too big, you have", Guessesleft , "Guesses left!" )
    
  if Guessesleft == 0:  # totalGuesses == 0 
    q = input("Do you want to answer a riddle to get another chance? ")
    if q.lower() == "yes":
      o = input("What is right ahead of you but you can't see it? ")
      
      if o.lower() == "the future":
        
        print("Your riddle answer is correct and you will get another chance to guess the secret number")
        Guess = int(input("Guess a number between 0 and 100: "))
        
        if Guess != randomNumber:
          break
      if o != "the future":
        print(colork + "Sorry, you did not get the correct answer for the riddle and you miss the chance to win another guess")
        break
    else:
      break

if Guess == randomNumber:
  print(colora + "\nNice Job,",userName , "you guessed my number in ",Guesses , "tries!" )
if Guess != randomNumber:
  print(colori + "\nSorry," + userName.capitalize() + " the correct answer was ",randomNumber)
 

# Pycharm, Visual Studio
# 1 guess --> you have 1 guess left
# > 1 guess --> you have 2 guesses left
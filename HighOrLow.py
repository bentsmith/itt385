from random import *

num = randint(1, 100)
run = True
MAX_GUESS = 10
guessCount = 0

while run and guessCount < MAX_GUESS:

    guess = int(input("What is your guess? "))
    guessCount += 1

    if guess < num:
        print("Guess is Too low")
    elif guess > num:
        print("Guess is Too high")
    else:
        print("You guessed it")
        print("Number of Guesses: ", guessCount)
        run = False

print("Sorry, you lost. My number was: ", num, ". Maybe next time!")

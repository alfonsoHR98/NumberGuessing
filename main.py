import random
import time

randomNumber = random.randint(1, 100)
numberOfGuesses = 0

print("Welcome to the Number Guessing Game!")
time.sleep(1)
print("I'm thinking of a number between 1 and 100.")
time.sleep(1)
print("Can you guess what it is?")
time.sleep(1)
while True:
    userGuess = int(input("Enter your guess: "))
    numberOfGuesses += 1
    if userGuess < randomNumber:
        print("Too low! Try again.")
    elif userGuess > randomNumber:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in", numberOfGuesses, "guesses.")
        break


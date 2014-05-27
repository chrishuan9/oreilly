__author__ = 'chris'
"""
Lab 12, Objective 1:
This project tests your ability to use modules and imports.

1.Create a new Python source file named guessing_game.py.
2.Import the random module.
3.Use the help() function on the random module to determine how to generate a random number between 1 and 99 inclusive.
4.Generate a random number between 1 and 99 and store it in a variable.
5.Use a while loop to accept integers from the user (don't forget--you'll need to convert the input string).
6.Compare the user's guess with the saved random number.
7.If the user successfully guesses the target number, inform them and terminate the program.
8.Otherwise, inform the user whether their guess was higher or lower than the saved random number and loop around to allow them to guess again.

Below is an example of possible output from running the program.

Guess a number: 25
Too low
Guess a number: 75
Too high
Guess a number: 60
Too high
Guess a number: 45
Too low
Guess a number: 53
You guessed it!
"""

import random

#generating random number between 1 and 99
numberToGuess = random.randint(0,99)
print("Random Number to guess: {0}".format(numberToGuess))
while True:
    inp = int(input("Guess a number: "))
    if not inp:
        break
    if inp > numberToGuess:
        print("Too high")
    if inp < numberToGuess:
        print("Too low")
    if inp == numberToGuess:
        print("You guessed it!")
        break
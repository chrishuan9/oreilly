__author__ = 'chris'
#Pyton 1: Lesson 4: Lab 4, Quiz 1
"""Create a new Python source file named guess.py.
Write a program that uses a while loop to ask the user to guess a number. Each guess should be checked against a
number stored in the "secret" variable, to which a value between 1 and 20 should be assigned at the start. Otherwise
it should report whether the guess was higher or lower than the secret. If the user guesses correctly,
the loop should terminate. The loop should also keep a count of the user's guesses, and should terminate if the user
makes five incorrect guesses. After the loop is over, the program should print a message if the user guessed the
number correctly."""
#random — Generate pseudo-random numbers, should not be used for security purposes
from random import randrange

secret = randrange(1, 20)  #Integer from 1 to 20
print("Chosen secret", secret)
secretFound = False;
attempt = 0
while (not secretFound and attempt < 5):
    attempt += 1
    guess = int(input("Guess a number: "))
    if guess == secret:
        secretFound = True
    elif guess < secret:
        print("Guess lower")
    elif guess > secret:
        print("Guess higher")
if secretFound:
    print("Correct! Well done, the number was", guess)
else:
    print("Sorry, the number was", secret)
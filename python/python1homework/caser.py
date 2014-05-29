__author__ = 'chris'
"""
Lab 13, Objective 1:
This project further tests your ability to write and use custom functions.

1. Create a new Python source file named caser.py.
2. Create these functions:
    - capitalize accepts a string parameter and applies the capitalize() method.
    - title accepts a string parameter and applies the title() method.
    - upper accepts a string parameter and applies the upper() method.
    - lower accepts a string parameter and applies the lower() method.
    - exit ends the program.

3. Store these functions in a dict with the keys matching the function names.
4. Create a while loop that requests two inputs from the user: one of the above function names, and any string.
5. Use function dispatch to get the correct function based on the first input, and then apply that function to the
second input.

Below is an example of possible output from running the program (note the difference between upper case,
capitalization, and title case).

Enter a function name (capitalize, title, upper, lower, or exit): lower
Enter a string: python is a Dynamic language
python is a dynamic language
Enter a function name (capitalize, title, upper, lower, or exit): upper
Enter a string: python is a Dynamic language
PYTHON IS A DYNAMIC LANGUAGE
Enter a function name (capitalize, title, upper, lower, or exit): capitalize
Enter a string: Python Is A Dynamic language
Python is a dynamic language
Enter a function name (capitalize, title, upper, lower, or exit): title
Enter a string: python is a Dynamic language
Python Is A Dynamic Language
Enter a function name (capitalize, title, upper, lower, or exit): exit
Enter a string: seeya
Goodbye for now!

Can you think of a way you could simplify the creation of the function dispatch table? (Hint: you can use methods of
the string type, str, directly as functions that take a single string argument.)
"""

import sys


def capitalize(text):
    """Prints capitalized string"""
    print(text.capitalize())


def title(text):
    """Prints titled string"""
    print(text.title())


def upper(text):
    """Prints string in all Upercases"""
    print(text.upper())


def lower(text):
    """Prints string in all lowercases"""
    print(text.lower())


def exit(text):
    """Quits the program"""
    print("Goodbye for now!")
    sys.exit()


if __name__ == "__main__":
    switch = {
        'capitalize': capitalize,
        'title': title,
        'upper': upper,
        'lower': lower,
        'exit': exit
    }

options = switch.keys()

prompt = 'Enter a function name ({0}): '.format(', '.join(options))
prompt2 = 'Enter a string: '

while True:
    inputcommand = input(prompt)
    option = switch.get(inputcommand, None)
    if option:
        inputtext = input(prompt2)
        option(inputtext)
    else:
        print('Please select a valid option!')

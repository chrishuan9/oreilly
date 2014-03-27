__author__ = 'chris'
"""
Lab 3, Objective 1
This project tests your ability to use conditional tests and write code that responds differently to different inputs.

Create a new Python source file named check_string.py.
Write a program that asks the user to input a string. Verify with tests that the string is all in upper case and ends with a period. If either of these tests fails, print an appropriate message. If both tests succeed, print a message that indicates the string is acceptable.
Verify that your program works correctly and hand it in.
Here are examples of how the program might appear when run twice:

Please enter an upper-case string ending with a period: lower case input
Input is not all upper case.
Input does not end with a period.

Please enter an upper-case string ending with a period: THIS IS OK.
Input meets both requirements.
"""
inputString = input("Please enter an upper-case string ending with a period: ")
if inputString.isupper() and inputString.endswith("."):
    print("Input meets both requirements.")
else:
    if not inputString.isupper():
        print("Input is not all upper case.")
    if not inputString.endswith("."):
        print("Input does not end with a period.")

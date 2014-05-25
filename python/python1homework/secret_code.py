__author__ = 'chris'
"""
Lab 10, Objective 1:
This project requires you to use built-in functions to perform character manipulations.

1. Create a new Python source file named secret_code.py.
2. Write a program to read a line of input from the user, and encode it using the following cipher:
3. Take each character of the string individually, and make the corresponding character in the output string be that whose ordinal value is 1 more than the ordinal value of the input character. Once the output string has been constructed in this way, the output of the program should be the reverse of the constructed output string.

Below is an example of possible input and output from running the program.

Message: This is it
uj!tj!tjiU
"""
inp = input("Message: ")
output = ""
for char in inp:
    output += chr(ord(char)+1)
print(''.join(reversed(output)))
#print using slicing syntax
#print(output[::-1])
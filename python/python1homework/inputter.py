__author__ = 'chris'
"""
Lab 9, Objective 1:
This project tests your ability to use file objects.

1.Create a new Python source file named inputter.py.
2.Write a program that uses a while loop to accept input from the user (if the user presses Enter, exit the program).
3.Save the input to a file, then print it.
4.Upon starting, the program will display any previous content of the file.

Below is an example of possible output from a first run of the program.

Enter text: Python is fun.
Python is fun.
Enter text: O'Reilly makes good classes.
Python is fun.O'Reilly makes good classes.
Enter text:
Below is an example of possible output from a second run of the program.

Python is fun.O'Reilly makes good classes.
Enter text: The file is saving correctly
Python is fun.O'Reilly makes good classes.The file is saving correctly
Enter text:
"""
empty_input = ''
string_input = 'Enter text: '
while True:
    inp = input(string_input)
    if inp == empty_input:
        break
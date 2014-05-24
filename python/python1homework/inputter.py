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

import os
import os.path

#change to your liking
path_to_tmp_file = "tmpsavefile.txt"

empty_input = ''
#check if file already exists and print out content
if os.path.isfile("tmpsavefile.txt") and os.access("tmpsavefile.txt", os.R_OK):
    #print("Using tmp file: {0}".format(path_to_tmp_file))
    #print file content
    f = open(path_to_tmp_file, 'r')
    for line in f.readlines():
        print(line)
    f.close()
string_input = 'Enter text: '
while True:
    inp = input(string_input)
    if inp == empty_input:
        #quit
        break
    else:
        f = open(path_to_tmp_file, 'a')
        #write new string to file
        if f.writable():
            f.write(inp)
            f.close()
        #print new file content
        f = open(path_to_tmp_file, 'r')
        for line in f.readlines():
            print(line)
            f.close()

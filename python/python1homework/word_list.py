__author__ = 'chris'
"""This project tests your ability to use sequences.

Create a new Python source file named word_list.py.
Make the program read a string from the user and create a list of words from the input.
Create two lists, one containing the words that contain at least one upper-case letter and one of the words that don't contain any upper-case letters.
Use a single for loop to print out the words with upper-case letters in them, followed by the words with no upper-case letters in them, one word per line.
Verify that your program works correctly, and hand it in.
"""

def hasUpperCase(word):
    for character in word:
        if character.isupper():
            return True

def printWordList(list):
    for word in list:
        print(word)


s = input("Enter your string: ")
words = s.strip().split()
upperCaseList = []
noUpperCaseList = []
for word in words:
    if (hasUpperCase(word)):
        print("Adding '" + word + "' to uppercase list")
        upperCaseList.append(word)
    else:
        print("Adding '" + word + "' to nouppercase list")
        noUpperCaseList.append(word)

printWordList(upperCaseList)
printWordList(noUpperCaseList)


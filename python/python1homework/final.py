__author__ = 'chris'
"""
Objective 2:
This project tests your basic ability to build a complex program from the relatively limited amounts of Python you
already know.

1. Create a new Python source file named final.py.
2. Write a program that meets the following specifications:
   - Call the program with an argument, it should treat the argument as a filename, and process the content of the file.
   - The program reads all the input, splitting it up into words, and computes the length of each word. Punctuation
   marks should not be included as a part of the word, so "it's" should be counted as a three-character word,
   and "final." should be counted as a five-character word.
   - The example text includes a "word" of zero length (the "&"); your solution should handle this.
   - When all input has been processed ,the program should print a table showing the word count for each of the word
   lengths that has been encountered. Your tutor will run your code against several standardized inputs to verify the
   correctness of your logic.

Below is an example of output from running the program using the text in this file as input. (The text is the United
States Declaration of Independence). Copy the text in this file. Create a new file and paste the copied text into it,
and save it as declaration.txt in the same folder where your final.py program is located.

Here is some sample output.

 Length Count
 1 16
 2 267
 3 267
 4 169
 5 140
 6 112
 7 99
 8 68
 9 61
 10 56
 11 35
 12 13
 13 9
 14 7
 15 2
Also, you will probably want to define a function to return the length of each word, since the built-in len()
function will include punctuation characters.
"""


def word_length(filename):
    """
    >>> word_length("declaration.txt")
    Length Count
    1 16
    2 267
    3 267
    4 169
    5 140
    6 112
    7 99
    8 68
    9 61
    10 56
    11 35
    12 13
    13 9
    14 7
    15 2
    """

    try:
        f = open("declaration.txt", 'r')
        inputlines = f.readlines()
        #Python removes the punctuation to ensure that only words are present in the text.
        #"It's" is not the same as "It's," # (with a comma), so the punctuation must be removed
        for punc in ",?;.'":
            text = text.replace(punc, "")
    except FileNotFoundError:
        print("File Not found, check path")


def _test():
    import doctest, refactory

    return doctest.testmod(refactory)


if __name__ == "__main__":
    #_test()
    word_length("declaration.txt")
__author__ = 'chris'
#Lab6, Objective 1
"""
Objective 1:
This project tests your ability to use sets and dicts, and your ability to follow an algorithm (recipe) exactly.

1.Create a new Python source file named input_counter.py.
2.Write a program that creates an empty set and dict.
3.Write a while loop that repeatedly creates a list of words from a line of input from the user.
4.Loop through the list of words and add each one to the set. If the set increases in size (indicating this word has not been processed before), add the word to the dict as a key with the value being the new length of the set.
5.Using another loop, display the list of words in the dict along with their value, which represents the order in which they were discovered by the program.
6.If the user presses Enter without any text, print Finished and exit.

Below is an example of output from running the program.

Enter text: how now brown cow
how 1
now 2
cow 4
brown 3
Enter text: the cow jumped over the moon
brown 3
cow 4
jumped 6
over 7
moon 8
how 1
the 5
now 2
Enter text:
Finished
"""
quitProgram = False
#creates set
s = set()
#creates empty dic
d = {}
while (not quitProgram):
    inputList = list(input("Enter text: ").lower().split())
    if not inputList:
        print("empty input, quitting ...")
        quitProgram = True
        break;
    print("Non empty input")
    for word in inputList:
        oldSize = len(s)
        s.add(word)
        #check if size has increased
        newSize = len(s)
        if newSize > oldSize:
            d[word] = newSize
print(s)
print(d)
__author__ = 'chris'
#Python 1: Lesson 4: Iteration: For and While Loops
"""Program to locate the first space in the input string."""
s = input("Enter any string: ")
pos = 0
for c in s:
    if c == " ":
        break
    pos += 1
print("First space occurred at position", pos)
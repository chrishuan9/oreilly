__author__ = 'chris'
#Python 1: Lesson 4: Iteration: For and While Loops
"""Counts the vowels in a user input string."""
s = input("Enter any string: ")
vcount = 0
for c in s:
    if c in "aeiouAEIOU":
        vcount += 1
print("Vowel count:", vcount);
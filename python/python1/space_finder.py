__author__ = 'chris'
#Python 1: Lesson 4: Iteration: For and While Loops
"""Program to locate the first space in the input string."""
s = input("Enter any string: ")
pos = 0
for c in s:
    if c == " ":
        print("First space occurred at position ", pos)
        break
    pos += 1
else:
    #Python loops come with such extra logic built in, in the shape of the optional else clause. This clause is placed
    # at the same indentation level as the for or while loop that it matches, and (just as with the if statement) is
    # followed by an indented suite of one or more statements. This suite is only executed if the loop terminates
    # normally.
    # If the loop ends because a break statement is executed, then the interpreter just skips over the else suite.
    print("No spaces in that string ")
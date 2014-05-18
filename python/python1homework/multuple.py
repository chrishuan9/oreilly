__author__ = 'chris'
"""
Lab 7, Objective 1:
This project tests your ability to handle string formatting.

Create a new Python source file named multuple.py.
Write a program that takes as data a tuple of two-element tuples, such as ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98)).
This and/or similar data should be hard-coded (no need for user input).
Loop over the tuple and print out the results of multiplying the two numbers together, and use string formatting to
display nicely.
Below is an example of output from running the program with the sample data above. Preserve the spacing, assuming that no input number is greater than 99.

   1 =  1 x  1
   4 =  2 x  2
 156 = 12 x 13
  16 =  4 x  4
9702 = 99 x 98
"""
data = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

# Formatting syntax:
#
# >: The field is right-aligned in the available space, with any padding to its left.
# 4,2,2: Minimum field width, Note that unless a minimum field width is defined, the field width will always be the
# same size as the data to fill it, so that the alignment option has no meaning in this case.
# d: Denotes the type, determines how the data should be presented = Decimal: formats the integer in base 10.
#
for tup in data:
    print("{0:>4d} = {1:2d} x {2:2d}".format(tup[0]*tup[1],tup[0],tup[1]))
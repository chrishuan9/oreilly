__author__ = 'chris'
"""Produce a listing of people's names, ages and weights."""
data = [
    ("Steve", 59, 202),
    ("Dorothy", 49, 156),
    ("Simon", 39, 155),
    ("David", 61, 135)
]
# format syntax explanation: for details see <https://docs.python.org/3.3/library/string.html>
##
# 0 : arg_name: either number or a keyword: number = positional argument, keyword = named keyword,
# it denotes the specific parameter passed by in the format(arg_name_1, arg_name_2, etc).
# [0]: element_index: denotes the specific element in tuple: 0: String, 1: first integer, 2: second integer
# :< : '<' Forces the field to be left-aligned within the available space (this is the default for most objects)
# 12 : Minimum field width, Note that unless a minimum field width is defined, the field width will always be the same
# size as the data to fill it, so that the alignment option has no meaning in this case.
# s/d: Denotes the type, determines how the data should be presented
# 's': String format. This is the default type for strings and may be omitted.
# None: Same as 's'
# 'd': Decimal Integer. Outputs the number in base 10.
for row in data:
    print("{0[0]:<12s} {0[1]:4d} {0[2]:4d}".format(row))
# While this program works, the correspondence between related data items seems a little obscure.
# the program as shown below to extract the individual items from the row and pass them as separate
# arguments to the format() call:
for name, age, weight in data:
    print("{0:<12s} {1:4d} {2:4d}".format(name, age, weight))
# Okay, now let's make the name field wider. We'll use the period as a pad character to help the reader follow the line
# from the name to the age and weight. Modify the program a third time—add a padding character before the alignment
# indication and increase the field width:
for name, age, weight in data:
    print("{0:.<30s} {1:4d} {2:4d}".format(name, age, weight))

for name, age, weight in data:
    print("{0:.^30s} {1:4d} {2:4d}".format(name, age, weight))
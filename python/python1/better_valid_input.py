__author__ = 'chris'
"""Validate user input"""

valid_inputs = ['yes','no','maybe']
# The % operator can also be used for string formatting.
# It interprets the left argument much like a sprintf()-style format string to be applied to the right argument,
# and returns the string resulting from this formatting operation.
input_query_string = 'Type %s: ' % ' or '.join(valid_inputs)
while True:
    s = input(input_query_string)
    if s in valid_inputs:
        break
    print("Wrong! Try again.")
print(s)
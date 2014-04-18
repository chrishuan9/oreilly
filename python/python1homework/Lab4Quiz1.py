__author__ = 'chris'
"""
Write a for statement to bind each character of the lower-case alphabet to the name "c"
(there is no need to write a loop body).
"""
#String in python are immutable, therefore a string cannot be treated as a list
inputstring = "testlala"
for i in range(len(inputstring)):
    if inputstring[i] in 'abcdefghijklmnopqrstuvwxyz':
        #string are immutable - modifying a string actually creates a new object
        #we need to bind the new object to the variable
        inputstring = inputstring.replace(inputstring[i], 'c')
print(inputstring)

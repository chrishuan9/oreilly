__author__ = 'chris'
"""
Lab 11, Objective 1:
This project tests your basic ability to write, use, and understand custom functions.

1.Create a new Python source file named three_param.py.
2. Write a program that has a function named my_func with three parameters, 'a', 'b', and 'c'. The first parameter is
required, and the second two parameters have the default values of 'b was not entered' and 'c was not entered'. The
function must print the value of each parameter.
3. In your program, call my_func three times. The first time, just provide a value for the first parameter. The
second time, provide values for the first and second parameters. The third time, provide values for all three
parameters.
4. In your program, print the function itself.
Below is an example of possible output from running the program using the word 'test' as the value for all arguments
provided to calls.

test
b was not entered
c was not entered
test
test
c was not entered
test
test
test
<function my_func at 0x397588>

"""


def my_func(a, b='b was not entered', c='c was not entered'):
    print(a)
    print(b)
    print(c)


print(my_func("test"))
print(my_func("test", "test"))
print(my_func("test", "test", "test"))
print(my_func)

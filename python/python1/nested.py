__author__ = 'chris'
""" Nested exception handling

Example output:
====================
a:  1 / b:  string
Invalid types for division
None
====================
a:  string / b:  0
Invalid types for division
None
====================
a:  2 / b:  0
Divide by zero
None
====================
a:  123 / b:  4
30.75

"""


def divide(a, b):
    """ Return result of dividing a by b """
    print("=" * 20)
    print("a: ", a, "/ b: ", b)
    try:
        result = a / b
    #Tuple: matches if one of entries in the tuple matches
    except (ZeroDivisionError, TypeError):
        print("Something went wrong!")
        raise


if __name__ == "__main__":
    for arg1, arg2 in ((1, "string"), (2, 0), (123, 4)):
        try:
            print(divide(arg1, arg2))
        except Exception as msg:
            print("Problem: {0}".format(msg))

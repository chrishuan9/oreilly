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
        print("Sometimes executed")
        return result
    except TypeError:
        print("Invalid types for division")
    except ZeroDivisionError:
        print("Divide by zero")

if __name__ == "__main__":
    print(divide(1, "string"))
    print(divide("string", 0))
    print(divide(2, 0))
    print(divide(123, 4))

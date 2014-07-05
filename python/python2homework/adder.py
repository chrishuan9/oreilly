__author__ = 'chris'
"adder.py: defines an adder function according to a slightly unusual " \
"definition."
import numbers

def adder(x, y):
    if isinstance(x, list):
        return x + [y]
    elif isinstance(y, list):
        return y + [x]
    elif isinstance(x, numbers.Number) and isinstance(y, str):
        return str(x) + y
    return x + y
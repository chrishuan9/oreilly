__author__ = 'chris'


def multiplier(*args):
    """ Multiply the arguments together and return the result.
        Return 0 if nothing is provided.
    """
    if not args:
        return 0
    product = args[0]
    for a in args[1:]:
        product *= a
    return product


print(multiplier())
print(multiplier(1, 2, 3, 4))
print(multiplier(6, 7, 8, 9, 10, 11, 12, 13))
print(multiplier(10, 20, 100))

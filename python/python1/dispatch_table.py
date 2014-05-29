__author__ = 'chris'
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

sw = {'adder':add, 'subber':sub}
print(sw['adder'](3,2))
print(sw['subber'](3,2))
print(sw)
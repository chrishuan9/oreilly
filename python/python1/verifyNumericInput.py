__author__ = 'chris'
"""Exception Handling example using input verification
    Example:
    Integer: thing
    Please enter an integer
    Integer: python
    Please enter an integer
    Integer: 12.3
    Please enter an integer
    Integer: 12
    22
>>>
"""

while True:
    inp = input("Integer: ")
    try:
        print(int(inp) + 10)
        break
    except ValueError:
        print("Please enter an Integer")
__author__ = 'chris'
inputString = input("Please enter an upper-case string ending with a period: ")
if inputString.isupper() and inputString.endswith("."):
    print("Input meets both requirements.")
else:
    if not inputString.isupper():
        print("Input is not all upper case.")
    if not inputString.endswith("."):
        print("Input does not end with a period.")

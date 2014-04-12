__author__ = 'chris'
"""Program to split a sentence into words."""
s = input("Please enter a sentence: ")
while True:
    # removes double spacing between words
    # as long as there is a space between the words use string slicing to remove the space from the string
    # by slicing the string from the second character thereby omitting the space
    while s.startswith(" "):
        s = s[1:]
    pos = 0
    for c in s:
        if c == " ":
            print(s[:pos])
            s = s[pos + 1:]
            break
        pos += 1
    else:
        print(s)
        break

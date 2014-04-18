__author__ = 'chris'
#!/usr/local/bin/python3
"""Count the words, lines and characters in a chunk of text."""

gettysburg = """\Four score and seven years ago ourfathers brought forth on this continent,a new nation,
conceived in Liberty, anddedicated to the proposition thatall men are created equal.
Now we are engaged in a great civil war,testing whether that nation, orany nation so conceived and so dedicated,
can long endure. We are met ona great battle-field of that war. We havecome to dedicate a portion of thatfield,
as a final resting place for thosewho here gave their lives that thatnation might live. It is altogetherfitting
and proper that we should do this."""

lengthct = [0] * 20  # a list of 20 zeroes
charct = len(gettysburg)

lines = gettysburg.split("\n")
linect = len(lines)

wordct = 0
for line in lines:
    words = line.split()
    wordct += len(words)
    for word in words:
        lengthct[len(word)] += 1

print("The text contains", linect, "lines,", wordct, "words, and", charct, "characters.")
for i, ct in enumerate(lengthct):
    if ct:
        print("Length", i, ":", ct)
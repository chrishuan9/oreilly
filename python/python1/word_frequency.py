__author__ = 'chris'
"""Count the number of different words in a text."""

text = """\
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full;
One for the master,
And one for the dame,
And one for the little boy
Who lives down the lane."""

#Python removes the punctuation to ensure that only words are present in the text.
#"Baa" is not the same as "Baa," # (with a comma), so the punctuation must be removed
for punc in ",?;.":
    text = text.replace(punc, "")
freq = {}
for word in text.lower().split()
    if word in freq:
        freq[word] +=1
    else:
        freq[word] = 1
for word in sorted(freq.keys()):
    print(word, freq[word])
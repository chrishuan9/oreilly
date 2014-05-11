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
for word in text.lower().split():
    #uses the get() method with a default value of zero to retrieve the existing count,
    #so if the word hasn't been seen before, the assignment inserts a value of one against the new key.
    freq[word] = freq.get(word,0)+1
for word in sorted(freq.keys()):
    print(word, freq[word])
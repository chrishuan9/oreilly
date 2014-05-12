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
words = {}
textwords = text.lower().split()
firstword = textwords[0]
for nextword in textwords[1:]:
    if firstword not in words:
        #For each word in the input, we will keep a count of the number of times
        #it was followed by each of the other words that immediately follow it in the text
        words[firstword] = {}
        words[firstword][nextword] = words[firstword].get(nextword, 0)+1
        firstword = nextword
for word in sorted(words.keys()):
    d = words[word]
    for word2 in sorted(d.keys()):
        print(word, ":", word2, d[word2])
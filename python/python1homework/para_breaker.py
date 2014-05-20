__author__ = 'chris'
"""
Lab 8, Objective 1:
This project tests your ability to use more sophisticated loops.

1. Create a new Python source file named para_breaker.py.
2. Write a program to break up a paragraph into sentences and phrases. Sentences are delineated by periods and phrases are delineated by commas.
3. Print the results to the screen. You will need to use a loop within a loop.
4. Use the text from the second paragraph of the United States Declaration of Independence (provided below).

United States Declaration of Independence to be used in the example

Example output:

**************************************************
Sentence #1
Phrase 1: We hold these truths to be self-evident
Phrase 2: that all men are created equal
Phrase 3: that they are endowed by their Creator with certain unalienable Rights
Phrase 4: that among these are Life
Phrase 5: Liberty and the pursuit of Happiness
**************************************************
Sentence #2
Phrase 1: - That to secure these rights
Phrase 2: Governments are instituted among Men
Phrase 3: deriving their just powers from the consent of the governed
Phrase 4: - That whenever any Form of Government becomes destructive of these ends
"""
seperator = "**************************************************"
#delimiters = ['.',',']
delimiter_sentence = '.'
delimiter_phrase = ','
input_text = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.  - Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Systems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world."
sentences = {}
phrases = {}
for sentence_no, sentence in enumerate(input_text.split(delimiter_sentence)):
    sentences[sentence_no] = {}
    print(seperator)
    print("Sentence #{0}".format(sentence_no+1))
    for phrase_no,phrase in enumerate(sentence.split(delimiter_phrase)):
        sentences[sentence_no][phrase_no] = phrase
        print("Phrase {0}: {1}".format(phrase_no+1,phrase))
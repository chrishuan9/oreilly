__author__ = 'chris'
"""
Lab 16, Objective 1:
This project tests your understanding of analyzing the structure of code, and your ability to mercilessly refactor.

1. Create a new Python source file named refactory.py.
2. Copy the code below into the refactory.py file.
3. Run the program. If you copied it correctly, no errors will occur. The program works, but the code is less than
Pythonic.
4. Refactor the code mercilessly to be leaner and easier to understand. The example includes a lot of unnecessary
code, some of which is difficult to understand, and individual lines of code are not documented.
5. Make sure all tests pass.

There is no example of possible output from running the program, because successful tests are silent so nothing
should be displayed.

Here's the refactory.py code:"""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')


def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    lst_of_words = title.lower().split()
    num_of_words = len(lst_of_words)
    if num_of_words < 1:
        return ''
    new_title = lst_of_words.pop(0)
    new_title = new_title[0].upper() + new_title[1:]
    tpl_of_words = tuple(lst_of_words)
    for word in tpl_of_words:
        prep_word = False
        for prep in small_words:
            if prep == word:
                new_title = new_title + ' '
                new_title = new_title + word
                prep_word = True
                break
        if prep_word == True:
            continue
        new_title = new_title + ' '
        new_title = new_title + word[0].upper()
        new_title = new_title + word[1:]
    return new_title


def _test():
    import doctest, refactory

    return doctest.testmod(refactory)


if __name__ == "__main__":
    _test()
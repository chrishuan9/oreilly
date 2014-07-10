__author__ = 'chris'
"""Reads a list from a file and writes a list to a file."""


def write_list(fn, lst):
    """Writes a list to a named file. Each list item will be on
    a separate line. Overwrites the file if it already exists.
    """
    # 'w' for only writing (an existing file with the same name will be erased)
    f = open(fn, "w")
    for item in lst:
        f.write("%s\n" % item)
    f.close()


def read_list(fn):
    """Reads a list from a file without using readline.
    Uses standard line endings ("\n") to delimit list items.
    """
    f = open(fn, "r")
    s = f.read()
    l = s.split("\n")
    return l
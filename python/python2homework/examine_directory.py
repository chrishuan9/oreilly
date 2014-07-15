__author__ = 'chris'
import glob
import os


def examine(path="."):
    files = glob.glob(os.path.join(path, "*"))
    extension_count = {}
    for fn in files:
        name, extension = os.path.splitext(fn)
        if extension not in extension_count:
            extension_count[extension] = 0
        extension_count[extension] += 1
    return extension_count
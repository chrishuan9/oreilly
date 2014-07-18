__author__ = 'chris'
import glob
import os


def examine(path="."):
    files = glob.glob(os.path.join(path, "*"))
    #print(files)
    extension_count = {}
    for fn in files:
        name, extension = os.path.splitext(fn)
       #print("Checking {0} : {1}".format(name,extension))
        if extension not in extension_count:
            #print("Found new File extensions ".format(extension))
            extension_count[extension] = 0
        extension_count[extension] += 1
    return extension_count
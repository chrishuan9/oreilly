__author__ = 'chris'
"""
Simple program to dump the command line arguments
"""

import sys
for n, arg in enumerate(sys.argv):
    print (n, ":", arg)
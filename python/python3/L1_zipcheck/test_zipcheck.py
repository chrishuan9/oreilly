'''
Created on Nov 22, 2014

@author: cyereazt

Test the zip_errors() function from the zipcheck module 
'''
import unittest
from zipcheck import zip_errors

class Test(unittest.TestCase):


    def test_zip_errors(self):
        "Test ensuring errors in data cause validation failures"
        pass
    
    def test_zip_success(self):
        "Test ensuring that valid data passes"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_zip_errors']
    unittest.main()
__author__ = 'chris'
"""

The test_1() method includes code to verify that the test directory contains
only the files created by the for loop. Hint: You might create a set
containing the list of three filenames, and then create a set from the
os.listdir() method.

A test_3() method creates a binary file that contains exactly a million bytes,
closes it and then uses os.stat to verify that the file on disk is of
the correct length (with os.stat, statinfo.st_size returns the size in bytes).

"""
import unittest
import tempfile
import shutil
import glob
import os


class FileTest(unittest.TestCase):
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        # print("Created", self.dirname)
        os.chdir(self.dirname)

    def test_1(self):
        "Verify creation of files is possible"
        filenamelist = ["this.txt", "that.txt", "the_other.txt"]
        for filename in filenamelist:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        files = os.listdir(self.dirname);
        # need to sort the lists because python won't treat the lists as
        #being equal if the order of the element differs
        self.assertEqual(filenamelist.sort(), files.sort())

    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        "Verify creation of a binary file that contains exactly a million bytes"
        filename = "AmillionBytes.txt"
        filesize = 1000000
        f = open(filename, "wb")
        for i in range(0, filesize):
            f.write(bytes([0]))
        f.close()
        # make sure file is closed
        self.assertTrue(f.closed)
        fileinfo = os.stat(filename)
        self.assertEqual(filesize, fileinfo.st_size)


    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        # print("Deleted", self.dirname)


if __name__ == "__main__":
    unittest.main()
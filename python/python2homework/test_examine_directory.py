__author__ = 'chris'
import unittest
import tempfile
import examine_directory
import time
import os

# Make a FileHandling_Homework project and assign it to your Python2_Homework
# working set. In that project, write a module containing a function to
# examine the contents of the current working directory and print out a count
# of how many files have each extension (".txt", ".doc", etc.)

# PATHSTEM = "v:\\workspace\\FileHandling\\src\\"
# PATHSTEM = "/Users/chris/Documents/dev/oreilly/python/python2homework/"


class TestLatest(unittest.TestCase):
    def setUp(self):
        self.path = PATHSTEM
        self.tempdirectory = tempfile.mkdtemp("testdir")
        self.dummy_files = ["file1.doc", "file1.txt", "file2.txt"]
        for fn in self.dummy_files:
            #print(os.path.join(self.tempdirectory,fn))
            f = open(os.path.join(self.tempdirectory,fn), "w")
            f.close()
            time.sleep(1)

    def test_empty_directory(self):
        """
        Ensure that calling the function on an empty directory returns
        nothing / empty list
        """
        self.emptydirectory = tempfile.TemporaryDirectory("emptydir")
        expected = {}
        extension_count = examine_directory.examine(path=self.emptydirectory)
        self.assertEqual(extension_count, expected)
        self.emptydirectory.cleanup()
        self.assertFalse(os.path.exists(self.emptydirectory))

    def test_current_directory(self):
        """
        Ensure that calling the function with no arguments returns
        the contents of the current directory
        """
        expected = {".doc": 1, ".txt": 2}
        extensions_count = examine_directory.examine(path=self.tempdirectory)
        self.assertEqual(extensions_count, expected)


    def tearDown(self):
        for fn in self.dummy_files:
            os.remove(os.path.join(self.tempdirectory,fn))


if __name__ == "__main__":
    unittest.main()
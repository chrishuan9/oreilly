__author__ = 'chris'
import unittest
import tempfile
import examine_directory
import time
import os
import shutil

# Make a FileHandling_Homework project and assign it to your Python2_Homework
# working set. In that project, write a module containing a function to
# examine the contents of the current working directory and print out a count
# of how many files have each extension (".txt", ".doc", etc.)

class TestLatest(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.tempdirectory = tempfile.mkdtemp("testdir")
        print("Created Temp Directory ", self.tempdirectory)
        self.dummy_files = ["file1.doc", "file1.txt", "file2.txt"]
        os.chdir(self.tempdirectory)
        for fn in self.dummy_files:
            print(fn)
            f = open(fn, "w")
            f.close()
            time.sleep(1)

    def test_empty_directory(self):
        """
        Ensure that calling the function on an empty directory returns
        nothing / empty list
        """
        self.emptydirectory = tempfile.mkdtemp("emptydir")
        expected = {}
        extension_count = examine_directory.examine(path=self.emptydirectory)
        self.assertEqual(extension_count, expected)
        #cleanup
        shutil.rmtree(self.emptydirectory)
        print("Deleted ", self.emptydirectory)

    def test_current_directory(self):
        """
        Ensure that calling the function with no arguments returns
        the contents of the current working directory
        """
        expected = {".doc": 1, ".txt": 2}
        extensions_count = examine_directory.examine(path=self.tempdirectory)
        self.assertEqual(extensions_count, expected)


    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tempdirectory)
        print("Deleted ", self.tempdirectory)


if __name__ == "__main__":
    unittest.main()
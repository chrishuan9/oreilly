__author__ = 'chris'
import unittest
import ziplatest
import time
import os
import shutil
import zipfile


class TestZip(unittest.TestCase):
    def setUp(self):
        self.path = r"/Users/chris/Documents/dev/oreilly/python/python2/L6_ZiptLatest/zip_test"
        self.zip_filename = os.path.join(self.path, "test_zip_latest.zip")
        os.mkdir(self.path)
        self.file_names = ["old", "newer", "newest"]
        for fn in self.file_names:
            f = open(os.path.join(self.path, fn), "w")
            f.close()
            time.sleep(1)

    def test_zip_latest(self):
        ziplatest.zip_latest(self.zip_filename, 2, self.path)
        zf = zipfile.ZipFile(self.zip_filename, "w")
        files_in_archive = zf.namelist()
        zf.close()
        observed = set([os.path.basename(f) for f in files_in_archive])
        expected = set(self.file_names[1:3])
        self.assertEqual(observed, expected)

    def tearDown(self):
        os.remove(self.zip_filename)
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass

    if __name__ == "__main__":    unittest.main()
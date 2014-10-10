__author__ = 'chris'
import unittest
import os
import glob
import tempfile
import logging
import shutil
import archiver

class TestLibrary(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(message)s')
        logger = logging.getLogger("archiver")
        self.tmpdirectory = tempfile.mkdtemp(dir=os.path.
                                             dirname(__file__))
        logger.debug("Using temporary directory " + self.tmpdirectory)

    def tearDown(self):
        # The user of mkdtemp() is responsible for deleting
        # the temporary directory and its contents when done with it.
        shutil.rmtree(self.tmpdirectory)


    def testArchiver(self):
        logger = logging.getLogger("archiver")
        archivefolder = "archive_me"
        archivefile = "my_archive.zip"
        filenames = ["groucho", "harpo", "chico"]
        path = os.path.join(self.tmpdirectory, archivefolder)
        os.mkdir(path)
        for filename in filenames:
            f = open(os.path.join(path,filename),"w")
            f.close();
        logger.debug(glob.glob(os.path.join(path,"*")))
        archive_fn = os.path.join(path,archivefile)
        zf = archiver.zipFilesinPath(path,archivefile)
        #using list comprehension concatenate working directory wiht filename
        expectedList = [archivefolder+"/{0}".format(i) for i in filenames]
        #check archives content
        self.assertEqual(sorted(zf.namelist()),sorted(expectedList))


if __name__ == "__main__":    unittest.main()
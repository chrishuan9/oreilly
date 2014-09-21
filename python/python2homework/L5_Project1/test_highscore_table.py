import unittest
import os
import glob
import highscoretable
import tempfile
import logging


class TestLibrary(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
        logger = logging.getLogger("highscoretable")
        logger.debug("setup()")
        tmpdirectory = tempfile.mkdtemp(dir=os.path.dirname(__file__))
        logger.debug("tmpdirectory " + tmpdirectory)
        tmpfn = os.path.join(tmpdirectory,"highscore.shelve")
        logger.debug("tmpfn " + tmpfn)
        self.lib_fn = "r"+"'"+tmpfn+"'"
        logger.debug("libfn " + self.lib_fn)

    def tearDown(self):
        shelve_files = glob.glob(self.lib_fn + '*')
        for fn in shelve_files:
            os.remove(fn)


    def testNewPlayerNewHighScore(self):
        #add new score
        highscore = highscoretable.writehighscore('chris',2)
        self.assertEqual(highscore, 2)


    def testExistingPlayerOverwritingHighScore(self):
        highscore = highscoretable.writehighscore('chris',4)
        self.assertEqual(highscore, 4)
        same_highscore =  highscoretable.writehighscore('chris',5)
        self.assertEqual(same_highscore, 5)

    def testExistingPlayerExistingHighScore(self):
        highscore = highscoretable.writehighscore('chris',5)
        self.assertEqual(highscore, 5)
        same_highscore = highscoretable.writehighscore('chris',4)
        self.assertEqual(same_highscore, 5)


if __name__ == "__main__":    unittest.main()
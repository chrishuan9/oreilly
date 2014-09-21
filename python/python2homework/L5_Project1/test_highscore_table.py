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
        self.tmpdirectory = tempfile.mkdtemp(dir=os.path.dirname(
            __file__))
        logger.debug("Using temporary directory " + self.tmpdirectory)
        self.lib_fn = os.path.join(self.tmpdirectory, "highscore.shelve")

    def tearDown(self):
        # No file clean-up necessary since mkdtemp takes care of deleting the
        # files after succesful execution
        pass


    def testNewPlayerNewHighScore(self):
        #add new score
        highscore = highscoretable.writehighscore('chris', 2, self.lib_fn)
        self.assertEqual(highscore, 2)


    def testExistingPlayerOverwritingHighScore(self):
        highscore = highscoretable.writehighscore('chris', 4, self.lib_fn)
        self.assertEqual(highscore, 4)
        same_highscore = highscoretable.writehighscore('chris', 5, self.lib_fn)
        self.assertEqual(same_highscore, 5)

    def testExistingPlayerExistingHighScore(self):
        highscore = highscoretable.writehighscore('chris', 5, self.lib_fn)
        self.assertEqual(highscore, 5)
        same_highscore = highscoretable.writehighscore('chris', 4, self.lib_fn)
        self.assertEqual(same_highscore, 5)


if __name__ == "__main__":    unittest.main()
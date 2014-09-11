import unittest
import os
import glob
import highscoretable


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib_fn = r'/Users/chris/Documents/dev/oreilly/python/python2homework/L5_Project1/highscore.shelve'

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
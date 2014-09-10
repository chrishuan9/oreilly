import unittest
import os
import glob
import highscoretable


class TestLibrary(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def testNewPlayerNewHighScore(self):
        #add new score
        highscore = highscoretable.writehighscore('chris',2)
        self.assertEqual(highscore, 2)
        new_highscore = highscoretable.writehighscore('chris',5)
        self.assertEqual(new_highscore, 5)
        same_highscore =  highscoretable.writehighscore('chris',4)
        self.assertEqual(same_highscore, 5)


    def testExistingPlayerNewHighScore(self):
        pass

    def testExistingPlayerOverwritingHighScore(self):
        pass

    if __name__ == "__main__":    unittest.main()
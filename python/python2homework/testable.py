__author__ = 'chris'
 #!/usr/local/bin/python3
#
# testtitle.py
#
"""Python 2: Lessong 2, Project 1"""
import unittest


def title(self):
    "How close is this function to str.title()"
    return self[0].upper() + self[1:].lower()


class TestTitle(unittest.TestCase):
    def test_title_capitalisation(self):
        s = "First"
        expected = title(s)
        errormsg = "Should return a titlecased \
            version of the string where words start with an uppercase character\
            and the remaining characters are lowercase."
        self.assertEqual(s, expected, errormsg)

    def test_title_capitalisation_randomcase(self):
        self.assertEqual("First", title("firST"), "Should return a titlecased \
            version of the string where words start with an uppercase character\
            and the remaining characters are lowercase.")

    def test_title_divergence(self):
        self.assertNotEqual("First, Second, Third", title("firST, sEconD, tHiRD"),
                            "Every word in the string should be titlecased,\
                            snot just the first")

    def test_title_native(self):
        s = "First, secOnD, thIRD, FourTH"
        self.assertEqual(title(s), s.title(), "Outcome differs compared to\
                                                 natve method")

if __name__ == "__main__":
    unittest.main()
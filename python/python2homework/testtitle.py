# !/usr/local/bin/python3
#
#testtitle.py
# Dear Pat, thanks for the thorough feedback. I tried to implement most changes
# you suggessted.
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
        expected = s.title()
        errormsg = "Expected: {0} (built-in method) but got: {1} (home made method)"
        self.assertEqual(title(s), expected, errormsg.format(expected, title(s)))


if __name__ == "__main__":
    unittest.main()

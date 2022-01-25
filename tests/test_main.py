import unittest
import sys
import os

# sys.path.append("..")
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import frequency    # noqa: E402 (impossible to import at top of file)
import bigram       # noqa: E402

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):

        self.assertEqual(frequency.clean("\n tieni solo questo 414!\n"),
                         "  tieni solo questo      ")
        self.assertEqual(frequency.frequencies(
                "Nel mezzo del cammin di nostra vita")['a'], 3)
        self.assertEqual(bigram.present_bigrams("hello"),
                         ["he", "el", "ll", "lo"])
        self.assertEqual(bigram.swap("palo", "p", "l"), "lapo")

    # invalid inputs
    def test_wrong_values(self):

        self.assertEqual(frequency.keys("Exactlytwentysixcharacters",
                         "too_few_characters"), None)

    # corner case: empty string
    def test_empty_string(self):

        self.assertEqual(frequency.clean(""), None)


if __name__ == '__main__':

    unittest.main(verbosity=2)

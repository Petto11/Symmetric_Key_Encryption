import unittest
import sys
import os

#sys.path.append("..")
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import frequency

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class TestInput(unittest.TestCase):

    # smoke test: valid inputs
    def test_correct_values(self):
        # you should select some valid inputs, for which the output is known
        self.assertEqual(frequency.frequencies("Nel mezzo del cammin di nostra vita")['a'], 3)

    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(frequency.keys("qwertyuioplkjhgfdsazxcvbnm","qwertyudsazxcvbnmioplkjhssgf"), None)

        # NOTE: the following test passing an empty list will fail!
        # self.assertEqual(return_birthday([]), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(frequency.clean(""), None)


if __name__ == '__main__':

    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)

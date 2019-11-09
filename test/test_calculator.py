'''
This module contains the testing code for the cumulative profit calculators

TODO: make into custom testing class (with suites)
'''

import unittest
import numpy as np
import sys
# Import packages/modules to be tested
sys.path.append('./.')
import application
from application.compound_interest_calculator import compound_profit

class TestCalculator(unittest.TestCase):
    '''This class contains methods for testing the calculators in /application'''

    def test_input(self):
        '''Method to test compound_interest_calculator'''
        input = np.random.random((2,1))
        compound_profit(input[0], input[1])


if __name__ == '__main__':
    unittest.main()
'''
This module contains the testing code for the cumulative profit calculators
'''

import unittest
import numpy as np
# Import packages/modules to be tested
import application
from application.compound_interest_calculator import compound_profit

class TestCalculator(unittest.TestCase):
    '''This class contains the methods for testing the calculators'''

    def test_compound_interest_calculator(self):
        '''Method to test compound_interest_calculator'''
        input = np.random.random((2,1))
        compound_profit(input[0], input[1])


if __name__ == '__main__':
    unittest.main()
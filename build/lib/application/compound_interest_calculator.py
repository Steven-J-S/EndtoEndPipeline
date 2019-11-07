'''
Module that contains the compound interest calculator

TODO: turn into class
TODO: add unittesting functions
TODO: add exception handling/assertions
TODO: as instance of class is a compound_calculator, it will keep running untill turned "off"
TODO: add testing directory for all testing code
TODO: add performance/profiling/timing directory for all performance code
        - Profile the code over a range of inputs and output the performance analysis, this shows where bottlenecks might be
'''

import numpy as np

def compound_profit(init_value, interest, period=1, monthly_influx=0):
    '''
    Function to calculate the compounded profit of interest over initial value

    :param init_value: initial value of fund
    :param interest: monthly interest
    :param period: amount of periods (months) over which to compound interest
    :param monthly: amount of monthly influx

    :return: value of the fund after compounded interest

    TODO: add list/np.ndarray of interest rates over time
    TODO: add monthly influx (as a list/np.ndarray)
    '''
    # Check the type of input
    if isinstance(monthly_influx, (int, float)):
        pass
    elif isinstance(monthly_influx, (list, np.ndarray)):
        pass
    else:
        pass

    return init_value*(1 + interest)**period


''''
This module contains the main script to run the compound interest calculators

TODO: make custom exception class? i.e. CalculatorError(Exception)
'''

from compound_interest_calculator import compound_profit

def main():
    '''Main script function to run the compound interest calculators'''
    try:
        init_value = float(input('Input initial value:'))
        interest = float(input('Input interest:'))
        try:
            cprofit = compound_profit(init_value, interest)
            print('Profit with ${} initial value, and {} interest after 1 period: $'.format(init_value, interest), cprofit)
        except:
            print('Something went wrong in the calculation!') # TODO: use explicit exception
    except ValueError as e:
        print('Input values should be integers or floats!\n Args: ', e.args)
    finally:
        print('Script ended!')


if __name__ == '__main__':
    # Run the scripts
    main()
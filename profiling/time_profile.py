'''
This module contains the time profiling code of the application

TODO: make into custom profiler classd
'''

import subprocess
import pstats
import sys
import os
sys.path.append('./.')
current_path = os.path.dirname(os.path.abspath(__file__))

def profiler(test_path, profile_directory = current_path + '\\', profile_file = 'time_profile_raw'):
    '''This function profiles file using cProfile and outputs raw file'''
    # File to write results to
    with open(profile_directory + profile_file, 'w') as f:
        subprocess.call(['python', '-m', 'cProfile', '-s', 'tottime', test_path], stdout=f)

def store_stats(time_profile_raw, profile_directory = current_path + '\\', profile_file = 'time_profile'):
    '''This model processes raw cProfile file and stores output'''
    with open(profile_directory + profile_file, 'w') as stream:
        stats = pstats.Stats(profile_directory + time_profile_raw, stream=stream)
        stats.print_stats()

if __name__ == '__main__':
    # Run raw profiler
    # Test directory
    test_directory = 'test'
    # File to profile
    test_file = 'test_calculator.py'
    test_path = test_directory + '\\' + test_file
    # Run profiler
    profiler(test_path)


    '''
    # Run profile interpreter
    raw_profile_file = 'time_profile_raw'
    store_stats(raw_profile_file)
    '''

'''
This module contains the metadata for the package to be distributed
'''

from distutils.core import setup
with open('README.md') as file:
    readme = file.read()

setup(
    name='cumulative_profit_calculators',
    version='1.0.0',
    packages=['application'],
    license='LICENSE.txt',
    description='Application to calculate cumulative profit from compounded interest',
    long_description=readme
)
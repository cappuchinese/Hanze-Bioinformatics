#!/usr/bin/env python3

"""
A silly program with a collection of syntax errors.py
"""

__author__ = "Tsjerk A. Wassenaar"


# IMPORTS
import sys


# CONSTANTS
two_times_pi = 6.283185
mass = {
    "H": 1.008,
    "C": 12.011,
    "O": 15.998,
    }


# FUNCTIONS
def fun(a, b, c):
x = "Error"
    return a + b * c


# MAIN
def main(args):
    print(fun(mass['H'], mass['C'], mass['O']))
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)

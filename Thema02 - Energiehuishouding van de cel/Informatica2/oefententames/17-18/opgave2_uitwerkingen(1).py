#!/usr/bin/env python3
"""
This module calculates the GC percentage of a DNA sequence.
    usage: ./opgave2.py sequence
    example: ./opgave2.py acgctt
    output example: The GC percentage of sequence ACGCTT is: 50.0
"""

__author__ = 'Jurre Hageman'
__version__ = 0.1

#imports
import sys
import pydoc
import dna_tools


def main():
    """
    The main function of the module gets arguments, calls the functions and prints the result
    """
    #check if the length of the list of command line arguments is OK.
    args = sys.argv[1:]
    if len(args) != 1:
        #call the pydoc help function in case the number of command line arguments is not ok
        pydoc.help(__name__)
        #exit main and thereby the program
        sys.exit()
    #get arguments
    seq = args[0].upper()
    #DO WORK
    if not dna_tools.check_if_dna(seq):
        print("Found invalid character in DNA sequence {}".format(seq))
        print("Program will exit...")
        sys.exit()
    perc_GC = dna_tools.calculate_gc_percentage(seq)
    #print the results
    print("The GC percentage of sequence {} is: {}".format(seq, perc_GC))
    #all went well. exit with exit code 0
    return 0

if __name__ == "__main__":
    sys.exit(main())
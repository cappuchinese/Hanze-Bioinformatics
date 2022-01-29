#!/usr/bin/env python3
"""
This module contains functions that validates a DNA sequence and calculates its GC percentage.
"""

__author__ = 'jurrehageman'
__version__ = 0.1

#imports
import sys

def check_if_dna(seq):
    """
    This function checks if a string is dna
    """
    dna = "ATCG"
    for base in seq:
        if not base in dna:
            return False
    return True


def calculate_gc_percentage(seq):
    """
    This function calculates the GC percentage of a DNA sequence
    """
    #calculate the GC percentage
    base_G = seq.count("G")
    base_C = seq.count("C")
    len_seq = len(seq)
    perc_GC = (base_G + base_C)/len_seq *100
    return perc_GC


def main():
    """
    Testing module
    """
    print(check_if_dna("ATCG"))
    print(check_if_dna("ATCX"))
    print(calculate_gc_percentage("ATCG"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
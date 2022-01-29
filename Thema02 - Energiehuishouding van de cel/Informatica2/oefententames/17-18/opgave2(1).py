#!/usr/bin/env python3

__author__ = "Lisa Hu"
__version__ = 1.0

#imports
import sys
import pydoc

# TODO aparte file maken voor deze 2 functies en dna_tools.py noemen

def check_if_dna(seq):
    dna = "ATCG"
    for base in seq:
        if not base in dna:
            print(f"Found invalid character in DNA sequence {seq}")
            print("Program will exit...")
            return False

    return True


def calculate_gc_percentage(seq):
    #calculate the GC percentage
    base_G = seq.count("G")
    base_C = seq.count("C")
    len_seq = len(seq)
    perc_GC = (base_G + base_C)/len_seq *100

    return perc_GC


def main():
    if len(sys.argv) < 1:
        pydoc.help(__name__)
        sys.exit()

    #get arguments
    args = sys.argv[1:]
    #get sequence and make upper case
    seq = args[0].upper()

    if check_if_dna(seq):
        perc_GC = calculate_gc_percentage(seq)
        #print the output
        print(f"The GC percentage of sequence {seq} is: {perc_GC}")

    else:
        print(f"Sequence is not DNA: {seq}")


if __name__ == "__main__":
    sys.exit(main())

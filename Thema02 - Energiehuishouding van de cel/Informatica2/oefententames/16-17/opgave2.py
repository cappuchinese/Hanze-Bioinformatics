#!/usr/bin/env python3

import sys


def get_bisulphite_unmethylated(seq):
    """
    translates all C to T if DNA is unmethylated
    :param seq: the DNA sequence
    :return: modificated DNA sequence
    """
    seq_unmethylated = seq.replace("C", "T")
    return seq_unmethylated


def get_bisulphite_methylated(seq):
    """
    translates C to T if DNA is methylated
    :param seq: the DNA sequence
    :return: modificated DNA sequence
    """
    #for the methylated state first change CG to XG
    seq_methylated_mod_cg = seq.replace("CG", "XG")
    #now change all remaining C's to T's
    seq_methylated_mod_c = seq_methylated_mod_cg.replace("C", "T")
    #Replace all X's back to C's
    seq_methylated_mod_x = seq_methylated_mod_c.replace("X", "C")

    return seq_methylated_mod_x


def main():
    #get arguments
    args = sys.argv[1:]
    #get sequence and make upper case
    seq = args[0].upper()

    #run functions
    seq_unmethylated = get_bisulphite_unmethylated(seq)
    seq_methylated_mod_x = get_bisulphite_methylated(seq)

    #print the results
    print(f"Original sequence: {seq}")
    print(f"Unmethylated DNA after bisulphite treatment: {seq_unmethylated}")
    print(f"Methylated DNA after bisulphite treatment: {seq_methylated_mod_x}")


if __name__ == "__main__":
    sys.exit(main())
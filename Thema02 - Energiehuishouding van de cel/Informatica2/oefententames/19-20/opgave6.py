#!usr/bin/python3

__author__ = "Lisa Hu"
__version__ = 1.0

import sys
import pydoc


def dna_check(seq):
    """
    checks if sequence is DNA
    :param seq:
    :return: booleans
    """
    for char in seq:
        if char.upper() not in "ACTG":
            return False
        else:
            return True


def codon_list(seq):
    """
    makes a list of codons in the sequence
    :param seq:
    :return: list of codons
    """
    codons = []
    for startpos in range(0, len(seq), 3):
        codon = seq[startpos:startpos+3]

        if len(codon) == 3:
            if codon not in codons:
                codons.append(codon)
        else:
            pass

    return codons


def main():
    if len(sys.argv) < 2:
        pydoc.help(__name__)
        sys.exit()
    #     seq = "ACGACGTACGATCGTACGATCGATCAGCTA"
    else:
        seq = sys.argv[1:]
        print(seq)

        for i in seq:
            if dna_check(i):
                print("hi")
                print(i)
                codons = codon_list(seq)
                print(f"Unique codons: {len(codons)}  {codons}")


if __name__ == "__main__":
    sys.exit(main())

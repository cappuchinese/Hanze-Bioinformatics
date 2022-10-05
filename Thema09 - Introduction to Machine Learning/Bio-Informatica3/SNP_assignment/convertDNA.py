#!/usr/bin/python3

"""
Convert a DNA sequence to a protein sequence with offset
"""

__author__ = "Lisa Hu"
__date__ = 10.2022

from _data import codons


class DNAConverter:
    """
    Class that converts a DNA sequence into a protein sequence
    """

    def __init__(self, infile: str, offset: int = 0):
        """
        Initialize class variables
        :param infile: Path of a single DNA sequence in FASTA format
        :param offset: n ϵ {0, 1, 2} to offset the reading frame (default 0)
        """
        self.infile = infile
        self.offset = offset
        self.inseq = {}

        self.main()

    def __str__(self) -> str:
        """
        String representation of the class
        """
        return f"Input file: {self.infile}\nOffset: {self.offset}"

    def __load_input(self):
        """
        Read the input sequence into a dictionary
        :return: string with the input sequence
        """
        with open(self.infile, encoding="utf8") as inseq:
            header = [line.strip() for line in inseq if line.startswith(">")]
            lines = [line.strip() for line in inseq if not line.startswith(">")]
            self.inseq[header] = "".join(lines)

    def __convert_dna(self):
        """
        Convert the DNA sequence to the protein sequence with the offset
        """
        protein = ""
        for i in self.inseq:
            seq = self.inseq[i]
            # Input sequence with the given offset
            seq = seq[self.offset:]
            # Get the steps to go through the sequence
            for startpos in range(0, len(seq), 3):
                codon = seq[startpos:startpos+3]
                protein += codons[codon]
            self.inseq[i] = protein

    def main(self):
        self.__load_input()
        self.__convert_dna()

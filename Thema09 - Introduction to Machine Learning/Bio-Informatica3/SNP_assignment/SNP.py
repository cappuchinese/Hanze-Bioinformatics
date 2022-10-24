#!/usr/bin/python3

"""
Program description
"""

__author__ = "Lisa Hu"
__date__ = 09.2022

# IMPORT
import blosum
from _data import codons


class SeveritySNP:
    """
    TODO
    """

    def __init__(self, proref: dict, matrix: int = 62):
        """
        Initialize class variables
        :param proref: Reference protein that is aligned other sequences
        :param matrix: Either n ϵ {45,50,62,80,90} or path to create BLOSUM matrix (default 62)
        """
        self.proref = proref
        self.matrix = blosum.BLOSUM(matrix, 0)
        self.data = {}

    def __str__(self) -> str:
        """
        String representation of the class
        """
        return "TODO"

    def _load_msa(self, filename: str):
        """
        Read the MSA file and create a dictionary entry for each protein sequence:
            {"header" : "protein sequence"}
        :param filename: name of the MSA file
        """
        header = ""
        with open(filename, encoding="utf8") as msa_file:
            for line in msa_file:
                # Dictionary entry of the headers
                if line.startswith(">"):
                    line = line.strip()
                    self.data[line] = []
                    header = line
                # Add each line of the sequence of according header to its list
                else:
                    self.data[header].append(line.strip())

        # Join the list of sequence lines to create 1 string
        for i in self.data:
            self.data[i] = "".join(self.data[i])

    def calc_score(self):
        """
        TODO
        """
        pass


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

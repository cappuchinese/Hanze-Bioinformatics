#!/usr/bin/python3

"""
Program description
"""

__author__ = "Lisa Hu"
__date__ = 09.2022

# IMPORT
import blosum


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

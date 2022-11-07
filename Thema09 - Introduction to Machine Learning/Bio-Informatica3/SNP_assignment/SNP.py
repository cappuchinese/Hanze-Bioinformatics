#!/usr/bin/python3

"""
Calculate the severity score of the mutation on a single position in the sequence, based on the MSA.
"""

__author__ = "Lisa Hu"
__date__ = 09.2022

# IMPORT
import sys
import argparse
import csv
import blosum

# Possible amino acids
aminos = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T",
          "V", "W", "Y"]


class SNP:
    """
    Check how conserved the sequence is for each position
    """
    def __init__(self, msa, matrix=62):
        self.msa_file = msa
        self.matrix = blosum.BLOSUM(matrix, 0)
        self.data = {}
        self.scores = {}
        self.__load_msa(self.msa_file)

    def __str__(self):
        return f"Score the alignments of myoglobin with BLOSUM matrix"

    def run(self, position, mutation, out_file):
        self._calculate_score(position, mutation)
        if out_file:
            self._write_out()
        else:
            for key, value in self.scores.items():
                print(f"{key}: {value}")

    def __load_msa(self, filename: str):
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
                    # Change the gap symbol to the one used in the blosum
                    line = line.replace("-", "*")
                    self.data[header].append(line.strip())

        # Join the list of sequence lines to create 1 string
        for i in self.data:
            self.data[i] = "".join(self.data[i])

    def _calculate_score(self, position: int = None, mutation: str = None):
        """
        Calculate the score of each alignment
        :param position: The position of the mutation in the sequence.
                         Default is None -> calculates the scores of MSA
        :return:
        """
        # Get a list of all the sequences
        seqs = list(self.data.values())

        # Maximum and minimum score of each position and the division number
        min_score = min(self.matrix.values()) * len(seqs)
        max_score = max(self.matrix.values()) * len(seqs)
        points_factor = (abs(min_score) + abs(max_score)) / 10
        score = abs(min_score)

        # Zip through the sequences
        alignments = list(zip(*seqs))
        if position is None:
            for i, align in enumerate(alignments):
                for letter in align[1:]:
                    score += self.matrix[f"{align[0]}{letter}"]
                score /= points_factor
                self.scores[i] = score
                score = abs(min_score)
        else:
            # Check if position is not out of bounds
            try:
                alignments[position - 1]
            except Exception as e:
                print(e)

            # Add the mutation to the alignment of given position
            letters = (*alignments[position - 1], mutation)  # position-1 due to 0 indexing
            # Score the mutation
            for letter in letters[1:]:
                score += self.matrix[f"{letters[0]}{letter}"]
                score /= points_factor
                self.scores[position] = score

    def _write_out(self):
        with open("output.csv", "w") as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow(["Position", "Score"])
            for key, value in self.scores.items():
                writer.writerow([key, value])


def main():
    parser = argparse.ArgumentParser(description="Calculates the score for SNPs at a given position"
                                                 " based on given MSA. "
                                                 "Score is based on a scale from 1-10.")
    parser.add_argument("-f",
                        metavar="file",
                        type=str,
                        required=True,
                        help="Path to the MSA (MultiFASTA only) [REQUIRED]")
    parser.add_argument("-matrix",
                        type=int,
                        default=62,
                        choices=[45, 50, 62, 80, 90],
                        help="BLOSUM matrix for calculating. Options: [45, 50, 62, 80, 90]"
                             "(Default = 62)")
    parser.add_argument("-out",
                        action="store_true",
                        default=False,
                        help="Option for creating an output file. "
                             "If not given, scores will print in terminal")
    parser.add_argument("-p",
                        metavar="position",
                        type=int,
                        default=None,
                        required="-m" in sys.argv,
                        help="Position of the mutation. "
                             "If none is given, the scores of every position will be given")
    parser.add_argument("-m",
                        metavar="mutation",
                        type=str,
                        default=None,
                        choices=aminos,
                        required="-p" in sys.argv,
                        help="The amino acid mutation of given position.")
    args = parser.parse_args()  # Parse commandline arguments

    # Initialize SNP
    snp = SNP(args.f, args.matrix)
    snp.run(args.p, args.m, args.out)

    # Continuous mutation input
    flag = 1
    while flag:
        flag = input("Do you want to give a new mutation? (Y/n): ")
        if flag.lower() == "y":
            position = int(input("Position: "))
            mutation = input("Mutation: ")
            snp.run(position, mutation, args.out)
            continue
        elif flag.lower() == "n":
            flag = 0
        else:
            print("Input error: Exiting program...")
            return 1
    return flag


if __name__ == '__main__':
    EXITCODE = main()
    sys.exit(EXITCODE)

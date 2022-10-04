"""
Program description
"""

__author__ = "Lisa Hu"
__date__ = 09.2022


# IMPORT
from Bio import SeqIO, AlignIO


def parse_fasta(fasta_file):
    identifiers = [seq_rec.id for seq_rec in SeqIO.parse(fasta_file, "fasta")]
    seqs = [seq_rec.seq for seq_rec in SeqIO.parse(fasta_file, "fasta")]
    x = SeqIO.parse(fasta_file, "fasta")
    for i in x:
        print(len(i.seq))
    # print(identifiers, seqs)


parse_fasta("myoglobin.fasta")

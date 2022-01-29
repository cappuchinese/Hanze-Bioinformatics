#!/usr/env python3

"""
This is a program that calculates
- Phredscore (Ascii value - 33)
- Accuracy: (exponent =(-1*numscore/10); Q = 1 - (10**exponent))

input: a file with reads from a sequencer (default reads.fq)
Each read constists of:

A first line describing the machine it was run on, the chip identifier and
-the actual coordinates from the chip where the base was read :@M01785:20:0...
-The actual read sequence                    :NTCATGTACGGTCAGGATGG...
-The plus sign                               :+
-The predicted read base quality ASCII value :#>>1A1B3B11BAEFFBECA...

The purpose is to read the line with the quality ASCII values (line after +)
and calculates Phredscore and quality base

The outcome of the test string #>>1A should be:

Quality score: #>>1A
Phredscore   :    2    |   29   |   29   |   16   |   32   |
Accuracy     :  36.90% | 99.87% | 99.87% | 97.49% | 99.94% |

"""

__author__ = 'Fenna Feenstra'
__version__ = '0.2'

#imports
import sys

#functions
def phredScore(char):
    """ this function scores the base by converting the ascii value to a
    number and substract this with the offset """
    # correct this line
    num_score = ord(char) - 30
    return num_score


def base_call_accuracy(numscore):
    """ this function calculates the quality percentage"""
    exponent =(-1*numscore/10)
    Q = 1 - (10**exponent)
    return Q


def fetch_read(file):
    flag = False
    with open(file) as f:
        for line in f:
                if flag == True:
                    return line.strip()
                if line.startswith('+'):
                    flag = True
    return 0


def calc_phred_accur(sequence):
    """ for each character in sequence calculate PhredScore and accuracy """
    #create empty lists
    phreds = ""
    accurs = ""
    for character in sequence:
        QS = base_call_accuracy(phredScore(character))
        length = len("{:.2%}".format(QS)) -1
        phreds += " {:^{length}} |".format(phredScore(character), length=length)
        accurs += " {:.2%} |".format(QS)
    return (phreds, accurs)

#main
def main(args):
    """ fetch file with reads from command line and
        determine the phredscore and quality score
    """
    sequence = '#>>1A'
    phreds, accurs = calc_phred_accur(sequence)
    print("Quality score: {}".format(sequence))
    print("Phredscore   : {}".format(phreds))
    print("Accuracy     : {}".format(accurs))
    print(len(sequence))
    return 0


#entryppoint
if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)

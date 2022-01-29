# shebang

"""
program description
"""

__author__ = "Lisa Hu"
__version__ = 1.0

import sys


def open_file():
    """
    Function tries to open file
    :return: opened file
    """
    try:
        opened = open("reads.fq")
    except FileNotFoundError:
        print("Such file was not found in this directory")

    return opened


def read_file(opened_file):
    """
    Function goes through file and stores needed info
    :param opened_file:
    :return:
    """
    for line in opened_file:
        line = line.strip()
        if line.startswith("@"):
            header = line
        elif len(line) < 2:
            pass
        for char in line:
            if char not in "ACTG":
                quality_line = line
            seq = line
        print(seq)

    return header, seq, quality_line


def calc_quality(quality_line):
    qual_dict = {}
    for char in quality_line:
        numerical_score = ord(char) - 33
        accuracy = 1 - 10**(-numerical_score/10)
        qual_dict[numerical_score] = accuracy*100

    return qual_dict


def out_file():
    try:
        output = open("output.txt", "w")
    except IOError:
        print("Something went wrong...") #TODO

    return output


def main():
    opened = open_file()
    header, seq, quality = read_file(opened)
    qual_dict = calc_quality(quality)
    output_file = out_file()

    for x, y in zip(seq, quality):
        output_file.write(f"Base: {x}")
        output_file.write(f"Quality char: {quality}")

    # output_file.write("Base", "Quality char", "Numerical score", "Base call acc")
    # output_file.write()

    for key in qual_dict:
        print(key, ":", qual_dict[key], "%")
    # for x, y in zip(numerical_score, accuracy):
    #     print(x, ":", y)


if __name__ == "__main__":
    sys.exit(main())

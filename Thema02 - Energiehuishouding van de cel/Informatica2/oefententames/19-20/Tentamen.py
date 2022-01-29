#!usr/bin/python3

__author__ = "Lisa Hu"
__version__ = 1.0

import sys

# vraag 1
def opg1():
    file_name = 'sequentie.txt'
    try:
        opened = open(file_name)
    except FileNotFoundError:
        print("File was not found")

    seq_dict = {}
    for line in opened:
        if line.startswith(">"):
            header = line.strip()
        else:
            seq = line.strip()
            header += f"_{(len(seq))}"

            seq_dict[header] = seq

    return seq_dict


def opg2(*args):
    total_squared = 0
    for i in args:
        squared = i**2
        total_squared += squared

    return total_squared

#TODO fix this bitch
def opg3():
    rev_dict = {"G":"C", "A":"T", "T":"A", "C":"G"}
    forward = "GGACCCTTT"
    for i in range(-1, 0, -1):
        pass
    rev_comp = [forward.replace(i, rev_dict[i]) for i in forward]
    return rev_comp


def opg4():
    bases = ['g', 'a', 't', 'c']
    codons = [x+y+z for x in bases for y in bases for z in bases]
    return codons


def opg5():

    return


def main():
    opgave1 = opg1()
    print("OPGAVE 1")
    for i in opgave1:
        print(f"{i} : {opgave1[i]}")

    print("OPGAVE 2")
    print(opg2(1,2,3,4,5,0,6,8,9))

    # print("OPGAVE 3")
    # print(opg3())

    print("OPGAVE 4")
    print(opg4())


if __name__ == "__main__":
    sys.exit(main())
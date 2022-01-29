#!/usr/bin/python3

"""Calculating the atomweight of given PDB file"""

__author__ = "Lisa"
__version__ = 1.0

import sys


def calc_weight(atom):
    """
    sum up the masses of the atoms
    Parameter:
        atom in given PDB file
    Return:
        mass of the atom
    """
    weight = 0
    mass = {'C': 12.011,
            'N': 14.007,
            'O': 15.998,
            'P': 30.974,
            'S': 32.065,
            'H': 1.008
            }
    for element in atom:
        if element in mass:
            weight += mass[element]
        else:
            print('not in table mass table')
    return weight


def process_file(input_file_name):
    """
    reads file and filters atom info
    Parameter:
        name of input file (PDB file)
    Return:
        total mass of atoms
    """
    f = open(input_file_name)
    count = 0
    for line in f:
        if line.strip().startswith('ATOM'):
            line = line[13:]
            l = line.split(' ')
            atom = l[0]
            count += calc_weight(atom)
    f.close()
    return count


def store_atomweigth(y, output_file_name):
    """
    writes atomweight into file
    Parameters:
        total weight of atoms
        name of output file
    Return:
        file with atomweight
    """
    o = open(output_file_name, 'w')
    o.write('atomweigth:' + str(y) + '\n')
    o.close()
    return o


def main(sys_argv):
    """
    main function
    Parameter:
        commands in terminal
    Return:
        file with content
    """
    argv = sys_argv
    if len(argv) < 3:
        print("please provide the name of an input and an output file")
        print("Program stopping...")
        sys.exit()
    input_file_name = argv[1]
    output_file_name = argv[2]
    y = process_file(input_file_name)
    result = store_atomweigth(y, output_file_name)
    return result


# executing main
if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)

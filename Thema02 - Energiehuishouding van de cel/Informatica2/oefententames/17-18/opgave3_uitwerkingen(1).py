#!/usr/bin/env python3

"""
In the main() function a name for the inputfile(fasta.txt) and the outputfile (out.txt)
are fetched from the commandline [5 points]

the main function checks whether the correct number of arguments are parsed on the command line
if not the pydoc.help function calls the documentation of this module [5 points]

In the add_index(..,..) function the inputfile and the outputfile are opened
with automatic closure construction [5 points]

each line from the inputfile is read and written to the outputfile with an index prefix (starting with 01)
using the enumerate construct [5 points]

example input line from inputfile:     "CAAGAGAGCTGAGCTTGGA"
example output line outputfile:     "1 CAAGAGAGCTGAGCTTGGA"

the index_function handles the IOError in case the inputfile does not exist [5 points]

"""

__author__ = 'student_name'
__version__ = 0.1

#imports
import sys
import pydoc

#defs
def add_index(input, output):
    """
    read a file and write to a new file. For each line an index needs to be written
    :param input: file that needs to be read (for example fasta.txt)
    :param output: file that needs to be written to (for example out.txt)
    """
    try:
        with open(input, 'r') as inp, open(output, 'w') as out:
            for index, line in enumerate(inp):
                    out.write('{} {}'.format(index+1, line))
    except IOError as e:
        print('{} ({}) for {}'.format(type(e).__name__, e.args[0],input))
    finally:
       return 0


def main():
    """
    fetch from commandline the name of the inputfile and outputfile and parse to indexed_line
    use exception handling when no input file and output file are given
    """
    try:
        add_index(sys.argv[1], sys.argv[2])
    except IndexError:
        pydoc.help(__name__)
        sys.exit()
    finally:
        return 0


if __name__ == "__main__":
    sys.exit(main())



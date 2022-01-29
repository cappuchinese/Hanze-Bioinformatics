#!/usr/bin/env python3

"""
In the main() function a name for the inputfile(fasta.txt) and the outputfile (out.txt)
are fetched from the commandline [5 points]

the main function checks whether the correct number of arguments are parsed on the command line
if not, the function calls the documentation of this module [5 points]

In the add_index(..,..) function the inputfile and the outputfile are opened
with automatic closure construction [5 points]

each line from the inputfile is read and written to the outputfile with an index prefix (starting with 01)
using the enumerate construct [5 points]

example input line from inputfile:     "CAAGAGAGCTGAGCTTGGA"
example output line outputfile:     "1 CAAGAGAGCTGAGCTTGGA"

the add_index function handles the IOError in case the inputfile does not exist [5 points]

"""


#imports
import sys
import pydoc


#defs
def add_index(in_file, out_file): #change this
    """
    read a file and write the content to a new file with linenumber prefix
    :param in_file: file that needs to be read (for example fasta.txt)
    :param out_file: file that needs to be written to (for example out.txt)
    """
    try:
        open_in = open(in_file, "r")
        open_out = open(out_file, "w")
    except IOError:
        print("There's an IO Error")
        sys.exit()

    line = enumerate(open_in)
    for i in line:
        open_out.write(str(i) + "\n")

    open_in.close()
    open_out.close()


    #open the files and close automatically
    #each line of input needs to be write to output with linenumber prefix using enumerate
    #in case of IOError catch the error and print a message


def main():
    """
    fetch from commandline the name of the inputfile and outputfile and parse to indexed_line
    use exception handling when no input file and output file names are given
    """
    # fetch from commandline input and output and parse to add_index
    try:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    #in case of an IndexError call pydoc.help and exit
    except IndexError:
        pydoc.help(__doc__)

    add_index(in_file, out_file)



#call main
if __name__ == "__main__":
    sys.exit(main())

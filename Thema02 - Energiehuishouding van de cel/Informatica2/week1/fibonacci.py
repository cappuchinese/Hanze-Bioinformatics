#!/usr/bin/python3

"""Making a fibonacci sequence"""

__author__ = "Lisa Hu"
__version__ = 1.0

import sys


def conditions(sys_argv):
    """
    checking if user input is valid
    Parameter:
        input in terminal
    Return:
        True or False
    """
    max_amount = int(sys_argv)
    if max_amount > 0:
        return True
    else:
        print("input is invalid")
        return False


def make_fib_seq(sys_argv):
    """
    make Fibonacci sequence until the user input
    Parameter:
        input in terminal
    Return:
        list of Fibonacci sequence
    """
    fib_list = []
    n1, n2 = 0, 1
    condition = conditions(sys_argv)

    while condition:
        fib_list.append(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if n1 > int(sys_argv):
            condition = False

    return fib_list


def format_fib(fib_list):
    """
    Fibonacci sequence, but only the last 10 and '*' as second item
    Parameter:
        list of Fibonacci sequence
    Return:
        Fibonacci sequence in right format
    """
    form = fib_list[-10:]
    form[1] = "*"
    return form


def output_file(out_name, form):
    """
    writing output file
    Parameters:
        name of output file
        list of Fibonacci sequence in right format
    Return:
        written output file
    """
    output_file = open(out_name, "w")
    output_file.write(str(form))
    output_file.close()

    return output_file


def main(sys_argv):
    """
    main function
    Parameter:
        input in terminal
    Return:
        written output file
    """
    argv = sys_argv
    if len(argv) < 2:
        print("please enter maximum and output file")
        print("stopping program")
        sys.exit()
    max_num = argv[1]
    out_name = argv[2]
    fib_list = make_fib_seq(max_num)
    form = format_fib(fib_list)
    o = output_file(out_name, form)

    return o


# executing main
if __name__ == "__main__":
    sys.exit(main(sys.argv))

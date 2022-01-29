#!usr/bin/python3

"""program writes terminal commands backwards"""

__author__ = "Lisa Hu"
__version__ = 2020.11


import sys


def reverse_line(*args):
    """
    reversing the line
    :param args: terminal commands
    """
    count = 0
    for words in args:
        # range starts with last item, until first item, stepping backwards
        for i in range(-1, -len(words)-1, -1):
            count += 1
            print(count, words[i])


def main(args):
    """executing function"""
    if len(args) > 2:
        reverse_line(args)
    else:
        sys.exit()


# running main
if __name__ == "__main__":
    sys.exit(main(sys.argv))

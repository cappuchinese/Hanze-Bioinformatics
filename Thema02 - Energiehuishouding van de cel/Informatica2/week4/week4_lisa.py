#!usr/bin/python3

"""
Program description
"""

# IMPORTS
import sys

sys.path.append("D:/PycharmProjects/Informatica/j1k2/week4")
from .errors import err1


# FUNCTIONS
def error_doc(error):
    return getattr(__builtins__, error).__doc__


def attr_err():
    try:
        var1 = 2020
        var1.append(2021)
    except AttributeError:
        return "AttributeError"


def fnf_err():
    try:
        opened_file = open("unknown_file.txt", "r")
    except FileNotFoundError:
        return "FileNotFoundError"


def imp_err():
    try:
        from math import z
    except ImportError:
        return "ImportError"


def indent_err():
    try:
        err1()
    except IndentationError:
        return "IndentationError"


def index_err():
    random_list = ["Item0", "Item1", "Item2"]
    try:
        print(random_list[3])
    except IndexError:
        return "IndexError"


def module_err():
    try:
        import Unknown
    except ModuleNotFoundError:
        return "ModuleNotFoundError"


def key_name_err():
    random_dict = {"1": "Name", "2": "Age", "3": "Job"}
    try:
        print(random_dict[4])
        print(random_dic["1"])

    except KeyError:
        return "KeyError"

    except NameError:
        return "NameError"


def main():
    func_list = [attr_err(), fnf_err(), imp_err(), key_name_err()]
    for func in func_list:
        print(func + ":", error_doc(func))


if __name__ == "__main__":
    main()

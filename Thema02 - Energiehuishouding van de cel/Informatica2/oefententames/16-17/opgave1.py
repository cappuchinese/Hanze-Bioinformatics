#!/usr/bin/env python3

#voornaam: Lisa
#achternaam: Hu

__author__ = "Lisa Hu"


#opgave 1A

text = "hello"


def modify_text(text):
    text = text + " you" #deze regel mag niet veranderd worden
    return text #deze regel mag niet veranderd worden

print("1A", modify_text(text))

#opgave 1B
sequences = ["ATGTTGTGCC", "ATGTTGTGCC", "ATGTTGTGTGCC", "ATGTTGCC"]
print("1B", print(*sequences))

#opgave 1C

sequences = ["ATGTTGTGCC", "ATGTTGTGCC", "ATGTTGTGTGCC", "ATGTTGCC"]

with open('foo.txt', 'w') as fo:
    for seq in sequences:
        fo.write(seq+ '\n')
    fo.flush()
    fo.close()

with open('foo.txt', 'r') as fo:
    for line in fo:
        print(line)
    fo.flush()
    fo.close()

#opgave 1D
#IMPORTS
import time

#FUNCTIONS
def timestamp():
    """ get a time stamp according format dd-mm-yy hh:mm:ss """
    print(time.strftime("%d-%m-%Y %H:%M:%S"))
    return time.ctime()

print(timestamp())

#opgave 1E
def nuc_list(nucleotide_list = ["aatc", "acggg", "autgc", "ccc", "acucc"]):
    return nucleotide_list
new_list = []
map(lambda x: [new_list.append(y.upper()) for y in x], new_list)

print(new_list)


#opgave 1F

new_list_2 = "hier je antwoord"
print(new_list_2)


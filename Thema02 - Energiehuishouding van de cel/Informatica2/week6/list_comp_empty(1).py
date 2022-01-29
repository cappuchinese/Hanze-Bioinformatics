#!/usr/bin/env python3

"""
Geef steeds een list comprehension voor het resultaat
let op: alleen list comprehension mogen gebruikt worden
"""

__author__ = 'Jurre Hageman en Fenna Feenstra'
__version__ = '2.0'

import math
import random
import sys


def opg1():
    """
    gebruik range() voor het genereren van een getallenvolgorde
    resultaat [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    lc = [i for i in range(0,10)]
    return lc


def opg2(l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    """
    gebruik float() voor het omzetten naar floats
    resultaat: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    """
    lc = [float(i) for i in l]
    return lc


def opg3(l = ['h', 'a', 'l', 'l', 'o']):
    """
    gebruik str.upper() voor het omzetten naar hoofdletters
    resultaat ['H', 'A', 'L', 'L', 'O']
    """
    lc = [i.upper() for i in l]
    return lc


def opg4():
    """
    gebruik range() voor het maken van een lijst van getallen van 0 tot 10.
    Selecteer vervolgens de even getallen met een if statement
    resultaat: [0, 2, 4, 6, 8]
    """
    lc = [i for i in range(0, 10) if i%2 == 0]
    return lc


def opg5(l = [0, 1, 2, 3], s = "abc"):
    """
    gebruik een nested list comprehension
    resultaat
    ['a0', 'a1', 'a2', 'a3', 'b0', 'b1', 'b2', 'b3', 'c0', 'c1', 'c2', 'c3']
    """
    lc = [r+str(k) for k in l for r in s]
    return lc


def opg6(l = [0, 1, 2, 3], s = "abc"):
    """
    gebruik nu een nested expression.
    Gebruik if om elementen met een 2 over te slaan
    resultaat: ['a0', 'a1', 'a3', 'c0', 'c1', 'c3']
    """
    lc = [r+str(k)  for r in s for k in l if k!=2]
    return lc


def opg7(l= [1, 2, 3, 4, 5]):
    """
    geef de kwadraten mbv een list comprehension
    resultaat: [1, 4, 9, 16, 25]
    """
    lc = [i**2 for i in range(1, 6)]
    return lc


def opg8(l = [4, 9, 16, 25, 36]):
    """
    geef de wortel van elk item uit de lijst in een nieuwe lijst
    resultaat: [2.0, 3.0, 4.0, 5.0, 6.0]
    """
    lc = [math.sqrt(i) for i in l]
    return lc


def opg9(l = ['1', '2'], s = "atcg"):
    """
    maak een lijst van tuples voor elke combinatie
    resultaat [('a', '1'), ('a', '2'), ('t', '1'), ('t', '2'),
               ('c', '1'), ('c', '2'), ('g', '1'), ('g', '2')]
    """
    lc = [(r, k) for r in s for k in l]
    return lc


def opg10(s = "tcag"):
    """
    maak een lijst van tuples met alle codons
    resultaat
    [('t', 't', 't'), ('t', 't', 'c'), ('t', 't', 'a'),
    ('t', 't', 'g'), ('t', 'c', 't'), ('t', 'c', 'c'),
    ('t', 'c', 'a'), ('t', 'c', 'g'), ('t', 'a', 't'),
    ('t', 'a', 'c'), ('t', 'a', 'a'), ('t', 'a', 'g'),
    ('t', 'g', 't'), ('t', 'g', 'c'), ('t', 'g', 'a'),
    ('t', 'g', 'g'), ('c', 't', 't'), ('c', 't', 'c'),
    ('c', 't', 'a'), ('c', 't', 'g'), ('c', 'c', 't'),
    ('c', 'c', 'c'), ('c', 'c', 'a'), ('c', 'c', 'g'),
    ('c', 'a', 't'), ('c', 'a', 'c'), ('c', 'a', 'a'),
    ('c', 'a', 'g'), ('c', 'g', 't'), ('c', 'g', 'c'),
    ('c', 'g', 'a'), ('c', 'g', 'g'), ('a', 't', 't'),
    ('a', 't', 'c'), ('a', 't', 'a'), ('a', 't', 'g'),
    ('a', 'c', 't'), ('a', 'c', 'c'), ('a', 'c', 'a'),
    ('a', 'c', 'g'), ('a', 'a', 't'), ('a', 'a', 'c'),
    ('a', 'a', 'a'), ('a', 'a', 'g'), ('a', 'g', 't'),
    ('a', 'g', 'c'), ('a', 'g', 'a'), ('a', 'g', 'g'),
    ('g', 't', 't'), ('g', 't', 'c'), ('g', 't', 'a'),
    ('g', 't', 'g'), ('g', 'c', 't'), ('g', 'c', 'c'),
    ('g', 'c', 'a'), ('g', 'c', 'g'), ('g', 'a', 't'),
    ('g', 'a', 'c'), ('g', 'a', 'a'), ('g', 'a', 'g'),
    ('g', 'g', 't'), ('g', 'g', 'c'), ('g', 'g', 'a'),
    ('g', 'g', 'g')]
     """
    lc = [(i, j, k) for i in s for j in s for k in s]
    return lc


def opg11(s = "tcag"):
    """
    maak een lijst van strings met alle codons
    resultaat: ['ttt', 'ttc', 'tta', 'ttg', 'tct', 'tcc',
                'tca', 'tcg', 'tat', 'tac', 'taa', 'tag',
                'tgt', 'tgc', 'tga', 'tgg', 'ctt', 'ctc',
                'cta', 'ctg', 'cct', 'ccc', 'cca', 'ccg',
                'cat', 'cac', 'caa', 'cag', 'cgt', 'cgc',
                'cga', 'cgg', 'att', 'atc', 'ata', 'atg',
                'act', 'acc', 'aca', 'acg', 'aat', 'aac',
                'aaa', 'aag', 'agt', 'agc', 'aga', 'agg',
                'gtt', 'gtc', 'gta', 'gtg', 'gct', 'gcc',
                'gca', 'gcg', 'gat', 'gac', 'gaa', 'gag',
                'ggt', 'ggc', 'gga', 'ggg']
    """
    lc = [i+j+k for i in s for j in s for k in s]
    return lc


def opg12():
    """
    maak een twee-dimensionele matrix met behulp van range
    resultaat [[0, 1], [1, 2]]
    """
    lc = [[x,x+1] for x in range(0,2)]
    return lc


def opg13():
    """
    maak een twee-dimensionele matrix met behulp van range
    Zorg er voor dat de getallen oplopend zijn.
    resultaat [[1, 2], [3, 4], [5, 6]]
    """
    lc = [[x,x+1] for x in range(1,6,2)]
    return lc


def opg14(l = [[1, 2], [3, 4], [5, 6]]):
    """
    maak een lijst van de tweede kolom van de matrix
    resultaat [2, 4, 6]
    """
    lc = [x[1] for x in l]
    return lc


def opg15(l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
    """
    Maak een lijst van de diagonaal van de matrix
    resultaat [1, 5, 9]
    """
    lc = [l[x][x] for x in range(3)]
    return lc


def opg16(l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
    """
    Maak een lijst van 10 worpen met een dobbelsteen
    resultaat bijv: [4, 2, 1, 1, 4, 3, 4, 3, 1, 4]
    """
    lc = [random.randint(1, 6) for i in range(10)]
    return lc


def opg17(s = "cube"):
    """
    Maak een 3-dimensionale matrix. Elk element bevat de string:
    "cube". Dimensies zijn: 3x3x3
    resultaat [[['cube', 'cube', 'cube'], ['cube', 'cube', 'cube'],
                ['cube', 'cube', 'cube']], [['cube', 'cube', 'cube'],
                ['cube', 'cube', 'cube'], ['cube', 'cube', 'cube']],
                [['cube', 'cube', 'cube'], ['cube', 'cube', 'cube'],
                ['cube', 'cube', 'cube']]]
    """
    lc = [[["cube" for i in range(3)] for i in range(3)] for i in range(3)]
    return lc


def opg18():
    """
    Maak een setcomprehension van unieke worpen na 10 worpen
    met een dobbelsteen
    """
    sc = {x:str(random.randint(1,6)) for x in range(10)}
    return sc


def opg19():
    """
    Maak een dict comprehension. sleutels 1 t/m 10.
    De waarde per sleutel is het kwadraat van de sleutel.
    resultaat:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    dc = {x:x**2 for x in range(1,11)}
    return dc


def opg20(s = "tcag", aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"):
    """
    creeer een complete codon tabel.
    Maak eerst een list comprehension van de codons zoals vraag 11
    Dit resulteert in list_of_codons
    Maak daarna de codon table met de volgende code:
    codon_table = dict(zip(list_of_codons, aa))
    resultaat:
    {'ggc': 'G', 'agg': 'R', 'tta': 'L', 'tca': 'S', 'ctc': 'L', 'gct': 'A', 'tgc': 'C', 'gga': 'G', 'gtg': 'V', 'ggg': 'G', 'aga': 'R', 'gat': 'D', 'ggt': 'G', 'atc': 'I', 'gcg': 'A', 'cca': 'P', 'gac': 'D', 'aaa': 'K', 'gaa': 'E', 'tat': 'Y', 'agc': 'S', 'gtc': 'V', 'tct': 'S', 'cgg': 'R', 'gca': 'A', 'tcg': 'S', 'att': 'I', 'cag': 'Q', 'gta': 'V', 'tag': '*', 'ttg': 'L', 'aat': 'N', 'agt': 'S', 'gtt': 'V', 'ccg': 'P', 'cct': 'P', 'ctt': 'L', 'tgg': 'W', 'ctg': 'L', 'tcc': 'S', 'ttc': 'F', 'cac': 'H', 'act': 'T', 'gcc': 'A', 'ccc': 'P', 'atg': 'M', 'aag': 'K', 'cat': 'H', 'tga': '*', 'caa': 'Q', 'cta': 'L', 'acg': 'T', 'taa': '*', 'aca': 'T', 'cgc': 'R', 'cgt': 'R', 'ata': 'I', 'cga': 'R', 'aac': 'N', 'tgt': 'C', 'ttt': 'F', 'gag': 'E', 'tac': 'Y', 'acc': 'T'}
    """
    lc = [x+y+z for x in s for y in s for z in s]
    d = dict(zip(lc, aa))
    return d


def main():
    print(1, opg1())
    print(2, opg2())
    print(3, opg3())
    print(4, opg4())
    print(5, opg5())
    print(6, opg6())
    print(7, opg7())
    print(8, opg8())
    print(9, opg9())
    print(10, opg10())
    print(11, opg11())
    print(12, opg12())
    print(13, opg13())
    print(14, opg14())
    print(15, opg15())
    print(16, opg16())
    print(17, opg17())
    print(18, opg18())
    print(19, opg19())
    print(20, opg20())


if __name__ == "__main__":
    exitcode = (main())
    sys.exit(exitcode)

""" usage: python3 -m unittest test_list_comp.py
"""

import unittest
import list_comp
import random
import re

__author__ = 'Fenna Feenstra'
__version__ = '1.0'

class TestList_Comp(unittest.TestCase):

    def test_opg1(self):
        result = [i for i in range(10)]
        self.assertEqual(list_comp.opg1(), result)


    def test_opg2(self):
        result = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.assertEqual(list_comp.opg2(), result)


    def test_opg3(self):
        result = ['H', 'A', 'L', 'L', 'O']
        self.assertEqual(list_comp.opg3(), result)


    def test_opg4(self):
        result = [0, 2, 4, 6, 8]
        self.assertEqual(list_comp.opg4(), result)


    def test_opg5(self):
        result = ['a0', 'a1', 'a2', 'a3', 'b0', 'b1', 'b2', 'b3', 'c0', 'c1', 'c2', 'c3']
        self.assertEqual(list_comp.opg5(), result)


    def test_opg6(self):
        result = ['a0', 'a1', 'a3', 'c0', 'c1', 'c3']
        self.assertEqual(list_comp.opg6(), result)


    def test_opg7(self):
        result = [1, 4, 9, 16, 25]
        self.assertEqual(list_comp.opg7(), result)


    def test_opg8(self):
        result = [2.0, 3.0, 4.0, 5.0, 6.0]
        self.assertEqual(list_comp.opg8(), result)


    def test_opg9(self):
        result = [('a', '1'), ('a', '2'), ('t', '1'), ('t', '2'), ('c', '1'), ('c', '2'), ('g', '1'), ('g', '2')]
        self.assertEqual(list_comp.opg9(), result)


    def test_opg10(self):
        s = "tcag"
        result = [(i, j, k) for i in s for j in s for k in s]
        self.assertEqual(list_comp.opg10(), result)


    def test_opg11(self):
        s = "tcag"
        result = ["".join((i, j, k)) for i in s for j in s for k in s]
        self.assertEqual(list_comp.opg11(), result)


    def test_opg12(self):
        result = [[x, x+1] for x in range(2)]
        self.assertEqual(list_comp.opg12(), result)


    def test_opg13(self):
        result = [[x, x+1] for x in range(6) if x % 2 == 1]
        self.assertEqual(list_comp.opg13(), result)


    def test_opg14(self):
       result = [2, 4, 6]
       self.assertEqual(list_comp.opg14(), result)


    def test_opg15(self):
       result = [1, 5, 9]
       self.assertEqual(list_comp.opg15(), result)


    def test_opg16(self):
        result = re.findall(r'[1-6]',str(list_comp.opg16()))
        self.assertEqual(len(result), 10)
        self.assertIs(type(result), list)


    def test_opg17(self):
        s = "cube"
        result = [[[s for i in range(3)] for j in range(3)] for k in range(3)]
        self.assertEqual(list_comp.opg17(), result)


    def test_opg18(self):
        result = list_comp.opg18()
        self.assertIs(type(result), set)
        m = re.findall(r'[1-6]',str(result))
        self.assertEqual(len(m), len(result))


    def test_opg19(self):
        result = list_comp.opg19()
        self.assertIs(type(result), dict)
        for k, v in result.items():
            self.assertIs(v, k**2)


    def test_opg20(self):
        result = list_comp.opg20()
        codon = {'ggc': 'G', 'agg': 'R', 'tta': 'L', 'tca': 'S',
                  'ctc': 'L', 'gct': 'A', 'tgc': 'C', 'gga': 'G',
                  'gtg': 'V', 'ggg': 'G', 'aga': 'R', 'gat': 'D',
                  'ggt': 'G', 'atc': 'I', 'gcg': 'A', 'cca': 'P',
                  'gac': 'D', 'aaa': 'K', 'gaa': 'E', 'tat': 'Y',
                  'agc': 'S', 'gtc': 'V', 'tct': 'S', 'cgg': 'R',
                  'gca': 'A', 'tcg': 'S', 'att': 'I', 'cag': 'Q',
                  'gta': 'V', 'tag': '*', 'ttg': 'L', 'aat': 'N',
                  'agt': 'S', 'gtt': 'V', 'ccg': 'P', 'cct': 'P',
                  'ctt': 'L', 'tgg': 'W', 'ctg': 'L', 'tcc': 'S',
                  'ttc': 'F', 'cac': 'H', 'act': 'T', 'gcc': 'A',
                  'ccc': 'P', 'atg': 'M', 'aag': 'K', 'cat': 'H',
                  'tga': '*', 'caa': 'Q', 'cta': 'L', 'acg': 'T',
                  'taa': '*', 'aca': 'T', 'cgc': 'R', 'cgt': 'R',
                  'ata': 'I', 'cga': 'R', 'aac': 'N', 'tgt': 'C',
                  'ttt': 'F', 'gag': 'E', 'tac': 'Y', 'acc': 'T'}
        self.assertDictEqual(result, codon)


if __name__ == '__main__':
    unittest.main()

"""
   unit test program for person class in week_5.py
   usage: python3 -m unittest test_week5_full.py

"""

import unittest
from weekopdracht_5 import Regex


class TestRegex(unittest.TestCase):

    def test_vragen(self):
        r = Regex()
        self.assertEqual(r.vraag1(), ['add', 'cdd'])
        self.assertEqual(r.vraag2(), ['acdf', 'aaff'])
        self.assertEqual(r.vraag3(), ['add', 'A000', 'gggg', 'ggggH', 'R0v1', '15bb'])
        self.assertEqual(r.vraag4(), ['aaa', 'aba', 'aca', 'ada'])
        self.assertEqual(r.vraag5(), ['aad', 'aAd', 'a2d', 'a6D'])
        self.assertEqual(r.vraag6(), ['aaad', 'aAddd', 'aaa2ddd', 'a6dD'])
        self.assertEqual(r.vraag7(), ['12a34', '254a1', '011aa56', '878a9'])
        self.assertEqual(r.vraag8(), ['1 &abcdefghijklm', '2 &abcdefgh', '3 &abcdefghi', '4 &abcd'])
        self.assertEqual(r.vraag9(), ['foo 123|', 'bar 211\\', 'baz 2339|', 'eek 831\\'])
        self.assertEqual(r.vraag10(), ['01 Rose programmeur', '02 Reindert programmeur', '32 Piet systeemmanager', '42 Marcel ontwikkelaar'])
        self.assertEqual(r.vraag11(), ['GAGAGCTCA', 'GAGAAGCTCA', 'GAGAGGCTCA', 'AAGAAGGCTCA', 'AAGAAGCTCA'])
        self.assertEqual(r.vraag12(), ['QLHAHAHGL', 'QHIHSHGL', 'QIHVHTHAL', 'NLHAHSHGI', 'NHIHAHAI', 'QIHAHAHAL'])
        self.assertEqual(r.vraag13(), ['AGQRQRQRTSG', 'AGQRQRTTG', 'AGQRTSA', 'AGNRQRQRTSG', 'AGQRNRQRTTA', 'AGQRNRTSG'])


    def test_bonus(self):
        r = Regex()
        self.assertEqual(r.vraag14(), ['Maison du Beau, Gasthuisstraatje 9 9712 AS Groningen',
                                     "Attie's Special Flowers, Weerdingerstraat 201 7822 BK Emmen",
                                     'Bloemen Mozaiek, Van Lenneplaan 115/1 9721 PE Groningen',
                                     'Alex Aalders Bloemist, Nieuwe Huizen 7 9401 JS Assen',
                                     'Groenland Bloemdecoraties, S.O.J. Palmelaan 297 9728 VJ Groningen'])


#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()

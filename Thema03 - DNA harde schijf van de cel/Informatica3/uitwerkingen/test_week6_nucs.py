import unittest
from weekopdracht_6 import Nucliotides


class TestNucliotides(unittest.TestCase):

    def test_methods_nucliotides(self):
        nucs = Nucliotides()
        self.assertEqual(nucs.short(), ['A', 'C', 'G', 'T'])
        self.assertEqual(nucs.filter_pyrimidines(), ['Cytosine', 'Thymine'])


#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()

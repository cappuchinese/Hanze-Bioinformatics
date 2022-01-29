
import unittest

from weekopdracht_6 import Seqreq

class TestSeqreq(unittest.TestCase):
    
    def test_methods_seqrec(self):
        s = Seqreq()
        sa = [{'name': 'FHIT human', 'accno': 'NP|1234', 'seq': 'MRTEHIILVC'}, 
              {'name': 'FHIT mouse', 'accno': 'NP|2315', 'seq': 'MKSEHLVLVC'}, 
              {'name': 'FHIT gorilla', 'accno': 'NP|6645', 'seq': 'MRTDWAILAC'}, 
              {'name': 'FHIT fruitfly', 'accno': 'NP|9732', 'seq': 'MKSDHVILVC'}]
        sm = [{'name': 'FHIT fruitfly', 'accno': 'NP|9732', 'seq': 'MKSDHVILVC'}, 
              {'name': 'FHIT mouse', 'accno': 'NP|2315', 'seq': 'MKSEHLVLVC'}, 
              {'name': 'FHIT gorilla', 'accno': 'NP|6645', 'seq': 'MRTDWAILAC'}, 
              {'name': 'FHIT human', 'accno': 'NP|1234', 'seq': 'MRTEHIILVC'}]
        sr = [{'name': 'FHIT fruitfly', 'accno': 'NP|9732', 'seq': 'MKSDHVILVC'}, 
              {'name': 'FHIT gorilla', 'accno': 'NP|6645', 'seq': 'MRTDWAILAC'}, 
              {'name': 'FHIT human', 'accno': 'NP|1234', 'seq': 'MRTEHIILVC'}, 
              {'name': 'FHIT mouse', 'accno': 'NP|2315', 'seq': 'MKSEHLVLVC'}]

        self.assertEqual(s.sort_assession(), sa)
        self.assertEqual(s.sort_molweight(), sm)
        self.assertEqual(s.sort_seqrec(), sr)
 

#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()

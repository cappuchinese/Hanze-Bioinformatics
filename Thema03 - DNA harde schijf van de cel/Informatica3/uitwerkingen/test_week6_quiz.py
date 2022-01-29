
import unittest
from weekopdracht_6 import Somequiz

class TestSomequiz(unittest.TestCase):

    def test_methods_quiz(self):
        q = Somequiz()
        self.assertEqual(q.q1(), [1, 1, 3, 5, 6, 2, 0] )
        self.assertEqual(q.q2(), [3, 5, 7, 8, 4])
        self.assertAlmostEqual(q.q3(), [2.0, 2.5, 5.0, 7.0, 2.3333333333333335])
        self.assertEqual(q.q4(), [(1, 3), (1, 5, 3, 1), (7, 3, 5), (), (1,)])


#to run directly from editor
if __name__ == '__main__':
    #will run all of the tests
    unittest.main()

import unittest
from challenges05 import *


class Test_ch05(unittest.TestCase):

    def test(self):
        self.assertEqual(i(1), m(left(1)))
        self.assertEqual(i(5), m(left(5)))
        self.assertEqual(j(True), m(right(True)))
        self.assertEqual(j(False), m(right(False)))

        self.assertEqual(i1(1), m1(left(1)))
        self.assertEqual(i1(5), m1(left(5)))
        self.assertEqual(j1(True), m1(right(True)))
        self.assertEqual(j1(False), m1(right(False)))

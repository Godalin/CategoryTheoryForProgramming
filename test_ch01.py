import unittest
from challenges01 import *


class Test_ch02(unittest.TestCase):

    def test_compose(self):
        fun = compose(lambda x: x + 1, sum)

        self.assertEqual(fun([1, 2, 3]), 7)

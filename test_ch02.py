import unittest
import random
from challenges02 import *


class Test_ch02(unittest.TestCase):

    def test_memorize(self):
        madd256 = memorize(lambda x: x + 256)

        self.assertEqual(madd256(3), 256 + 3)
        self.assertEqual(madd256(1), 256 + 1)
        self.assertEqual(madd256(3), 256 + 3)
        self.assertEqual(madd256(1), 256 + 1)

    def test_random_memory(self):

        def receive1_ran(_):
            return random.random()

        fun = memorize(receive1_ran)

        self.assertNotEqual(receive1_ran(1), fun(1))
        self.assertNotEqual(receive1_ran(1), fun(1))
        self.assertNotEqual(receive1_ran(1), fun(1))
        self.assertNotEqual(receive1_ran(1), fun(1))
        self.assertNotEqual(receive1_ran(1), fun(1))

    def test_random_memory_with_seed(self):

        def with_seed(seed):
            random.seed(seed)
            return random.random()

        fun = memorize(with_seed)

        self.assertEqual(with_seed(1), fun(1))
        self.assertEqual(with_seed(1), fun(1))
        self.assertEqual(with_seed(2), fun(2))
        self.assertEqual(with_seed(2), fun(2))

    def test_bool_fns(self):
        self.assertEqual(same_(True), True)
        self.assertEqual(same_(False), False)
        self.assertEqual(diff_(True), False)
        self.assertEqual(diff_(False), True)
        self.assertEqual(true_(True), True)
        self.assertEqual(true_(False), True)
        self.assertEqual(fals_(True), False)
        self.assertEqual(fals_(False), False)

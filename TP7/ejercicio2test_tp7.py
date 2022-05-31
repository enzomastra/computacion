from ejercicio2_tp7 import*
import unittest
class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(validate_pin("1234"), True)
    def test2(self):
        self.assertEqual(validate_pin("12345"), False)
    def test3(self):
        self.assertEqual(validate_pin("a234"), False)
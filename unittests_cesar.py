import unittest
from cesar import encrypt
from cesar import decrypt


class TestEncrypt(unittest.TestCase):
    def test_simple_encrypt(self):
        self.assertEqual(encrypt("A", 1), "C")

class TestDecrypt(unittest.TestCase):
    def test_simple_decrypt(self):
        self.assertEqual(encrypt("C", 1), "A")
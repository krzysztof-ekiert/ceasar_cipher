import unittest
from cesar import encrypt
from cesar import decrypt


class TestEncrypt(unittest.TestCase):
    def test_simple_encrypt(self):
        self.assertEqual(encrypt("A", 1), "B")

class TestEncrypt2(unittest.TestCase):
    def test_simple_encrypt(self):
        self.assertEqual(encrypt("CEASER CIPHER DEMO", 4), "GIEWIV GMTLIV HIQS")

class TestDecrypt(unittest.TestCase):
    def test_simple_decrypt(self):
        self.assertEqual(encrypt("B", 1), "A")

class TestDecrypt2(unittest.TestCase):
    def test_simple_decrypt(self):
        self.assertEqual(encrypt("GIEWIV GMTLIV HIQS", 4), "CEASER CIPHER DEMO")
import unittest
from cesar import encrypt
from cesar import decrypt


class TestEncrypt(unittest.TestCase):
    def test_simple_encrypt(self):
        self.assertEqual(encrypt("A", 1), "B")
        self.assertEqual(encrypt("CEASER CIPHER DEMO", 4), "GIEWIV GMTLIV HIQS")

class TestDecrypt(unittest.TestCase):
    def test_simple_decrypt(self):
        self.assertEqual(decrypt("B", 1), "A")
        self.assertEqual(decrypt("GIEWIV GMTLIV HIQS", 4), "CEASER CIPHER DEMO")


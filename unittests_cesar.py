import unittest
from cesar import encrypt
from cesar import decrypt


class TestEncrypt(unittest.TestCase):
    def test_simple_encrypt(self):
        self.assertEqual(encrypt("A", 1), "B")
    def test_text_encrypt(self):
        self.assertEqual(encrypt("CEASER CIPHER DEMO", 4), "GIEWIV GMTLIV HIQS")
    def test_small_encrypt(self):
        self.assertEqual(encrypt("a", 2), "c")
    def test_space_encrypt(self):
        self.assertEqual(encrypt(" ", 5), " ")

class TestDecrypt(unittest.TestCase):
    def test_simple_decrypt(self):
        self.assertEqual(decrypt("B", 1), "A")
    def test_text_decrypt(self):
        self.assertEqual(decrypt("GIEWIV GMTLIV HIQS", 4), "CEASER CIPHER DEMO")
    def test_small_decrypt(self):
        self.assertEqual(decrypt("d", 3), "a")
    def test_space_decrypt(self):
        self.assertEqual(decrypt(" ", 7), " ")


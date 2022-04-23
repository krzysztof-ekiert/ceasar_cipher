
import pytest

from cesar import encrypt
from cesar import decrypt

@pytest.mark.parametrize(
    "text,shift,result",
    (
         ("A", 1, "B"),
         ("a", 2, "c"),
         ("CEASER CIPHER DEMO", 4, "GIEWIV GMTLIV HIQS"),
         (" ", 4, " ")
)
)

def test_encrypt(text, shift, result):
    assert encrypt(text, shift) == result

# class TestEncrypt:
#     def test_simple_encrypt(self):
#         assert encrypt("A", 1) == "B"
#     def test_text_encrypt(self):
#         assert encrypt("CEASER CIPHER DEMO", 4) == "GIEWIV GMTLIV HIQS"
#     def test_small_encrypt(self):
#         assert encrypt("a", 2) == "c"
#     def test_space_encrypt(self):
#         assert encrypt(" ", 5) == " "
#
# class TestDecrypt:
#     def test_simple_decrypt(self):
#         assert decrypt("B", 1) == "A"
#     def test_text_decrypt(self):
#         assert decrypt("GIEWIV GMTLIV HIQS", 4) == "CEASER CIPHER DEMO"
#     def test_small_decrypt(self):
#         assert decrypt("d", 3) == "a"
#     def test_space_decrypt(self):
#         assert decrypt(" ", 7) == " "


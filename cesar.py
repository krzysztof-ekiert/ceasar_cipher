# funkcja encrypt szyfruje tekst szyfrem cezara

# oraz decrypt ktora odkoduje

## >>>> encrypt("tekst", 4)
## >>>> decrypt("tekst", 4)


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if ord(char) == 32:
            result += " "
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if ord(char) == 32:
            result += " "
        elif char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


print(ord(" "))
assert encrypt("CEASER CIPHER DEMO", 4) == "GIEWIV GMTLIV HIQS"

assert encrypt("A", 4) == "E"
assert decrypt("GIEWIV GMTLIV HIQS", 4) == "CEASER CIPHER DEMO"

text = "CEASER CIPHER DEMO"
s = 4

print("Tekst: " + text)
print("Przesunięcie: " + str(s))
a = encrypt(text, s)
print("Encrypt: " + a)
print("Decrypt: " + decrypt(a, s))

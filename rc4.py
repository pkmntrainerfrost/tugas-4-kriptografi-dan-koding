# 18221102 | Salman Ma'arif Achsien
# 18221115 | Christopher Febrian Nugraha

import random
import base64
import sys

# Fungsi untuk menghilangkan karakter selain spasi + mengubah kapitalisasi

def preprocess(string:str):

    preprocessed_string = ""

    for char in string:

        if char.isalpha():
            preprocessed_string += char.upper()

    return preprocessed_string

# Fungsi-fungsi untuk mengubah output ke base64 / mengubah input base64 ke ASCII

def base64Encrypt(string:str):

    plaintext_bytes = string.encode("utf-8")

    base64_bytes = base64.b64encode(plaintext_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string

def base64Decrypt(string:str):

    base64_bytes = string.encode("ascii")

    plaintext_bytes = base64.b64decode(base64_bytes)
    plaintext_string = plaintext_bytes.decode("utf-8")

    return plaintext_string

# Fungsi-fungsi RC4

def rc4KSA(key:str,vigenere_key:str):

    s = [i for i in range(256)]

    j = 0

    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]

    # Modified affine for keyschedule
        
    m = sum([ord(char) for char in vigenere_key]) % 256

    if (m == 0 or m == 1):
        m = 3
    elif (m % 2 == 0):
        m = m + 1

    b = len(vigenere_key)

    for i in range(256):
        s[i] = ((m * (s[i]) + b) % 256)
    
    return s

def rc4PRGA(s:str):
    
    i = j = 0

    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        yield k

def rc4Keystream(key:str, vigenere_key:str):

    s = rc4KSA(key, vigenere_key)
    return rc4PRGA(s)

# For text input

def rc4(plaintext:str, key:str, vigenere_key:str):

    random.seed(vigenere_key)

    plaintext_array = [ord(i) for i in plaintext]
    key_array = [ord(key[i]) for i in range(len(key))]
    vigenere_key_array = [ord(key[i]) for i in range(len(key)) if ord(key[i]) <= 255]

    keystream = rc4Keystream(key_array,vigenere_key)

    ciphertext = []

    i = 0

    for char in plaintext_array:

        # extended vigenere to keystream

        add_vigenere = random.randint(0,1)
        k = (next(keystream) + (add_vigenere * vigenere_key_array[i])) % 256
        i = (i + add_vigenere) % len(vigenere_key_array)

        # XOR

        new_char = (char ^ k)

        ciphertext.append(chr(new_char))

    return ''.join(ciphertext)

# For byte input

def rc4Bytes(plainbytes, key:str, vigenere_key:str):

    random.seed(vigenere_key)

    key_array = [ord(key[i]) for i in range(len(key))]
    vigenere_key_array = [ord(key[i]) for i in range(len(key)) if ord(key[i]) <= 255]

    keystream = rc4Keystream(key_array,vigenere_key)

    cipherbytes = b""

    i = 0

    while (byte := plainbytes.read(1)):

        byte_int = int.from_bytes(byte,"little")

        # extended vigenere to keystream
        
        add_vigenere = random.randint(0,1)
        k = (next(keystream) + (add_vigenere * vigenere_key_array[i])) % 256
        i = (i + add_vigenere) % len(vigenere_key_array)

        # XOR

        new_byte = (byte_int ^ k)

        print(new_byte)

        cipherbytes += (new_byte.to_bytes(1,"little"))

    return cipherbytes

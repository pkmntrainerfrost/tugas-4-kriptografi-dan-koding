# 18221102 | Salman Ma'arif Achsien
# 18221115 | Christopher Febrian Nugraha

import math
import sympy
import random
import base64
import time
import os

# Pembangkit kunci - mengembalikan pasangan kunci publik dan kunci privat
def rsaGenerateKeyPair( p : int = 0, q : int = 0, e : int = 0):
    
    # Cek prima bila dimasukkan secara manual
    if (p != 0 and not (sympy.isprime(p))) or (q != 0 and not (sympy.isprime(q))):
        raise ValueError("P dan Q harus berupa bilangan prima!")
    
    # Cek ketidaksamaan P dan Q bila dimasukkan secara manual
    if p == q and p != 0:
        raise ValueError("P dan Q harus berbeda!")
    
    if p != 0 and q != 0:
        n = p * q
        if n < 256:
            raise ValueError("P * Q terlalu kecil!")
        
    given_p = p
    given_q = q

    # Percobaan pertama pembangkitan P dan Q secara acak
    while p == 0 or p == q:
        p = sympy.randprime(1,100)
    while q == 0 or p == q:
        q = sympy.randprime(1,100)
    
    # Hitung N dan Totient
    n = p * q
    t = (p - 1) * (q - 1)

    # Kalo random kekecilan
    while n < 256 or p == q:
        if given_p == 0:
            p = sympy.randprime(1,100)
        if given_q == 0:
            q = q = sympy.randprime(1,100)
        n = p * q
        t = (p - 1) * (q - 1)

    # Cek koprima
    if e != 0 and math.gcd(e,t) != 1:
        raise ValueError("Nilai E yang dimasukkan tidak koprima dengan totient!")

    # Pembangkitan E secara acak
    while e == 0 or math.gcd(e,t) != 1:
        e = random.randrange(2,t)

    # Pembangkitan D
    d = pow(e,-1,t)

    return {"primes" : {"p" : p, "q" :q},"key" : {"public" : {"e" : e,"n" : n}, "private" : {"d" : d,"n": n}}}

# Cek valid
def rsaValid(p,q,e):

    # Cek prima bila dimasukkan secara manual
    try:
        if (p != 0 and not (sympy.isprime(p))) or (q != 0 and not (sympy.isprime(q))):
            raise ValueError("P dan Q harus berupa bilangan prima!")
        
        # Cek ketidaksamaan P dan Q bila dimasukkan secara manual
        if p == q and p != 0:
            raise ValueError("P dan Q harus berbeda!")
        
        if p != 0 and q != 0:
            n = p * q
            if n < 256:
                raise ValueError("P * Q terlalu kecil!")
            
        n = p * q
        t = (p - 1) * (q - 1)
        
        if e != 0 and math.gcd(e,t) != 1:
            raise ValueError("Nilai E yang dimasukkan tidak koprima dengan totient!")
        return True
    except:
        return False


# Enkripsi
def rsaEncrypt(m : int, public_key : dict):

    if (m < 0):
        raise ValueError("M tidak boleh negatif!")
    if (m >= public_key["n"] - 1):
        raise ValueError("M tidak boleh lebih dari atau sama dengan N + 1!")
    
    return (pow(m,public_key["e"]) % public_key["n"])

def rsaEncryptText(m : str, public_key : dict):

    m_bytes = m.encode("utf-8")
    m_numbers_string = ""

    for byte in m_bytes:
        m_numbers_string += str(byte).zfill(3)

    m_numbers = [int(m_numbers_string[i:i+len(str(public_key["n"]))-1]) for i in range (0,len(m_numbers_string),len(str(public_key["n"]))-1)]

    m_numbers_encrypted = []

    for number in m_numbers:
        result = (rsaEncrypt(number,public_key))
        m_numbers_encrypted.append(result)

    m_numbers_encrypted_padded = []
    
    for i in m_numbers_encrypted:
        result = (str(i).zfill(len(str(public_key["n"]))))
        m_numbers_encrypted_padded.append(result)

    result = base64.b64encode(''.join(m_numbers_encrypted_padded).encode('utf-8')).decode("utf-8")
    return result

def rsaEncryptBytes(m : list, public_key : dict):

    m_numbers_string = ""

    for byte in m:
        m_numbers_string += str(byte).zfill(3)

    m_numbers = [int(m_numbers_string[i:i+len(str(public_key["n"]))-1]) for i in range (0,len(m_numbers_string),len(str(public_key["n"]))-1)]

    m_numbers_encrypted = []

    for number in m_numbers:
        result = (rsaEncrypt(number,public_key))
        m_numbers_encrypted.append(result)

    m_numbers_encrypted_padded = []
    
    for i in m_numbers_encrypted:
        result = (str(i).zfill(len(str(public_key["n"]))))
        m_numbers_encrypted_padded.append(result)

    result = base64.b64encode(''.join(m_numbers_encrypted_padded).encode('ascii')).decode("ascii")
    return result

# Dekripsi
def rsaDecrypt(c : int, private_key : dict):

    if (c < 0):
        raise ValueError("C tidak boleh negatif!")
    if (c >= private_key["n"] - 1):
        raise ValueError("C tidak boleh lebih dari atau sama dengan N + 1!")
    
    return (pow(c,private_key["d"]) % private_key["n"])

def rsaDecryptText(c : str, private_key : dict):

    c_bytes = base64.b64decode(c).decode("utf-8")
    c_numbers_string = ""

    for byte in c_bytes:
        c_numbers_string += str(byte)

    # Padding
    c_numbers = [int(c_numbers_string[i:i+len(str(private_key["n"]))]) for i in range (0,len(c_numbers_string),len(str(private_key["n"])))]

    c_numbers_decrypted = []

    for number in c_numbers:
        c_numbers_decrypted.append(rsaDecrypt(number,private_key))
    
    c_numbers_decrypted_string = ''.join([str(i).zfill(len(str(private_key["n"]))-1) for i in c_numbers_decrypted])

    c_numbers_decrypted_bytes = bytes([int(c_numbers_decrypted_string[i:i+3]) for i in range (0,len(c_numbers_decrypted_string),3)])

    result = c_numbers_decrypted_bytes.decode("utf-8")
    return result

def rsaDecryptBytes(c : str, private_key : dict):

    c_bytes = base64.b64decode(c).decode("ascii")
    c_numbers_string = ""

    for byte in c_bytes:
        c_numbers_string += str(byte)

    # Padding
    c_numbers = [int(c_numbers_string[i:i+len(str(private_key["n"]))]) for i in range (0,len(c_numbers_string),len(str(private_key["n"])))]

    c_numbers_decrypted = []

    for number in c_numbers:
        c_numbers_decrypted.append(rsaDecrypt(number,private_key))
    
    c_numbers_decrypted_string = ''.join([str(i).zfill(len(str(private_key["n"]))-1) for i in c_numbers_decrypted])

    c_numbers_decrypted_bytes = bytes([int(c_numbers_decrypted_string[i:i+3]) for i in range (0,len(c_numbers_decrypted_string),3)])

    return c_numbers_decrypted_bytes

def rsaSaveKeyPair(name : str, key : dict):

    timestamp = str(time.time()).replace(".","")

    filenamepri = f"keys/{name}_{timestamp}.pri"

    os.makedirs(os.path.dirname(filenamepri), exist_ok=True)
    
    with open(filenamepri,"w+") as file:   

        p = key["primes"]["p"]
        q = key["primes"]["q"]
        n = key["key"]["public"]["n"]
        e = key["key"]["public"]["e"]
        d = key["key"]["private"]["d"]

        file.write(f'p = {p}\n')
        file.write(f'q = {q}\n')
        file.write(f'n = {n}\n')
        file.write(f'e = {e}\n')
        file.write(f'd = {d}\n')
    
    filenamepub = f"keys/{name}_{timestamp}.pub"

    os.makedirs(os.path.dirname(filenamepri), exist_ok=True)
    
    with open(filenamepub,"w+") as file:   

        n = key["key"]["public"]["n"]
        e = key["key"]["public"]["e"]

        file.write(f'n = {n}\n')
        file.write(f'e = {e}\n')

    return filenamepri

# Driver
if __name__ == "__main__":

    keys = rsaGenerateKeyPair()

    print(keys)

    x = rsaEncrypt(69,keys["public"])

    print(x)
    print(rsaDecrypt(x,keys["private"]))

    y = "The Raiden Shogun is the awesome and terrible power of thunder incarnate, the exalted ruler of the Inazuma Shogunate. With the might of lightning at her disposal, she commits herself to the solitary pursuit of eternity."

    y_c = rsaEncryptText(y,keys["public"])

    print(y_c)

    y_d = rsaDecryptText(y_c,keys["private"])

    print(y_d)
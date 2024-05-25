# 18221102 | Salman Ma'arif Achsien
# 18221115 | Christopher Febrian Nugraha

import pandas as pd
from sys import exit
from keccak import sha3
import pyAesCrypt
import rsa
import glob
import os.path
import pdfkit

# REFERENCE
header = [  "NIM","Nama",
            "MK0","Matkul0","Nilai0","SKS0",
            "MK1","Matkul1","Nilai1","SKS1",
            "MK2","Matkul2","Nilai2","SKS2",
            "MK3","Matkul3","Nilai3","SKS3",
            "MK4","Matkul4","Nilai4","SKS4",
            "MK5","Matkul5","Nilai5","SKS5",
            "MK6","Matkul6","Nilai6","SKS6",
            "MK7","Matkul7","Nilai7","SKS7",
            "MK8","Matkul8","Nilai8","SKS8",
            "MK9","Matkul9","Nilai9","SKS9",
            "IPK","Sign"
        ]

# GLOBAL VAR
pri_path = ""
pub_path = ""

# DUMMY DATA
data = ["18218000", "Hatsune Miku",
         "II2221", "ManProy",   "AB","3",		
         "II3220", "AE",        "AB","3",	
         "II3230", "InfoSec",   "A", "3",		
         "II3240", "RekSTI",    "B", "3",		
         "II3260", "PPAM",      "AB","3",		
         "II4031", "KriptoSTI", "A", "2",	
         "II4035", "SisCer",    "C", "2",
         "II4038", "CC",        "A", "2",
         "II4062", "DWBI",      "BC","2",		
         "II4472", "KomInter",  "A", "2"]

def loadKunci():
    folder_path = r"D:\sem6\tugas-4-kriptografi-dan-koding\keys"
    pri = r"\*pri"
    pub = r"\*pub"
    pri_files = glob.glob(folder_path + pri)
    pub_files = glob.glob(folder_path + pub)
    global pri_path
    global pub_path
    if len(glob.glob(folder_path)) == 0:
        print("Kunci Kaprodi tidak ditemukan di "+folder_path+".")
    else:
        pri_path = max(pri_files, key=os.path.getctime)
        pub_path = max(pub_files, key=os.path.getctime)

def generateKunci():
    keys = rsa.rsaGenerateKeyPair()
    print(keys)
    rsa.rsaSaveKeyPair("kaprodi", keys)
    global pri_path
    pri_path = "keys/kaprodi_17165732240259767.pri"
    global pub_path
    pub_path = pri_path.replace(".pri", ".pub")

def idxToGrade(idx:str):
    ret = 0.0
    match idx:
        case "A":
            ret = 4
        case "AB":
            ret = 3.5
        case "B":
            ret = 3
        case "BC":
            ret = 2.5
        case "C":
            ret = 2
        case "D":
            ret = 1
        case "E":
            ret = 0
        case _:
            exit("Indeks nilai mata kuliah salah.")
    return ret

def countIpk(rec):
    ipk = 0
    sks = 0
    for i in range(len(rec)):
        if(i != 0 and i % 4 == 0):
            ipk += idxToGrade(rec[i])*int(rec[i+1])
            sks += int(rec[i+1])
    ipk = round(ipk/sks, 2)
    return ipk

def signRecord(rec, useHex):
    s = ""
    for e in rec:
        s += e
    digest = sha3(s, 256)
    f = open(pub_path, 'r')
    arr = f.readlines()
    pubkey = {arr[0][0] : int(arr[0][4:].strip("\r\n")), arr[1][0] : int(arr[1][4:].strip("\r\n"))}
    sign = rsa.rsaEncryptText(digest, pubkey, useHex)

    return sign

def addToDatabase(data, useHex=True):
    ipk = countIpk(data)
    data.append(str(ipk))
    sign = signRecord(data, useHex)
    data.append(str(sign))

    data = [data]
    data = pd.DataFrame(data, columns=header)
    data.to_csv("./db/nilai-siswa.csv", mode="a", index=False, header=False, encoding='utf-8')
    print(pd.read_csv("./db/nilai-siswa.csv"))

def removeFromDatabase(nim):
    frame = pd.read_csv("./db/nilai-siswa.csv", index_col=0)
    frame.drop(frame.loc[[nim]].index, inplace=True)
    frame.reset_index(names="NIM", inplace=True)
    frame.to_csv("./db/nilai-siswa.csv", index=False, header=header)
    print(pd.read_csv("./db/nilai-siswa.csv"))

def verifikasiSign(nim, useHex=True):
    f = open(pri_path, 'r')
    arr = f.readlines()
    prikey = {arr[0][0] : int(arr[0][4:].strip("\r\n")),
            arr[1][0] : int(arr[1][4:].strip("\r\n")),
            arr[2][0] : int(arr[2][4:].strip("\r\n")),
            arr[3][0] : int(arr[3][4:].strip("\r\n")),
            arr[4][0] : int(arr[4][4:].strip("\r\n"))}
    frame = pd.read_csv("./db/nilai-siswa.csv", index_col=0)
    rec = frame.loc[nim]

    decrypted = rsa.rsaDecryptText(rec[42], prikey, useHex)
    # print(decrypted)
    frame.drop(labels="Sign", axis=1, inplace=True)
    rec = frame.loc[nim]
    frame.reset_index(names="NIM", inplace=True)
    
    s = str(nim)
    for e in rec:
        s += str(e)
    hashed = sha3(s, 256)
    # print(hashed)
    print("Verifikasi berhasil." if decrypted == hashed else "Data tidak tervalidasi integritasnya.")

def enkripsiPDF(key, path : str):
    output = path+".enc"
    pyAesCrypt.encryptFile(path, output, key)
    print("File berhasil dienkripsi dan disimpan sebagai "+output+".")

def dekripsiPDF(key, path : str):
    name = path.split(".")
    output = name[0]+"dec."+name[1]
    pyAesCrypt.decryptFile(path, output, key)
    print("File "+path+" berhasil didekripsi dan disimpan sebagai "+output+".")

def downloadTranskrip(key, nim):
    save_as = "transkrip_"+nim+".pdf"
    pdfkit.from_file("transkrip.html", save_as)
    enkripsiPDF(key, save_as)
    if os.path.exists(save_as):
        os.remove(save_as)


# loadKunci()
# verifikasiSign(18218000)
# downloadTranskrip("PERSONA3RELOAD","18218000")
dekripsiPDF("PERSONA3RELOAD", "transkrip_18218000.pdf.enc")
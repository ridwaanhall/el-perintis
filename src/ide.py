import random

IDE_LIST = [
    "Jual jamu kekinian",
    "Platform edukasi syariah",
    "Konten motivasi anak",
    "Website trading pemula",
    "Gerobak ayam viral ala Ryu"
]

def ambil_ide():
    return random.choice(IDE_LIST)

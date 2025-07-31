"""
Narasi perjuangan dalam bentuk fungsi Python
"""

def narasi_perjuangan(nama, tipe):
    if tipe == "perintis":
        return f"{nama} menapaki jalan sunyi, membangun dari puing, jatuh-bangun, hingga akhirnya berdiri tegak."
    elif tipe == "pewaris":
        return f"{nama} menjaga bara warisan, menambah nilai, dan memastikan api tetap menyala di generasi berikutnya."
    else:
        return f"{nama} memilih jalannya sendiri."

if __name__ == "__main__":
    print(narasi_perjuangan("Ryu Kintaro", "perintis"))
    print(narasi_perjuangan("Ryu Kintaro", "pewaris"))

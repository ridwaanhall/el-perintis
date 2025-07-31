"""
Simulasi OOP vs non-OOP sebagai analogi perintis (bangun dari nol) vs pewaris (lanjutkan legacy)
"""

# Non-OOP: Pewaris (melanjutkan pola lama)
def perjuangan_pewaris(nama, legacy):
    print(f"{nama} melanjutkan perjuangan dengan fondasi: {legacy}")
    for langkah in range(1, 4):
        print(f"Langkah {langkah}: Menjaga dan mengembangkan {legacy}")
    print(f"{nama} berhasil menjaga warisan!")

# OOP: Perintis (membangun dari nol)
class Perintis:
    def __init__(self, nama, visi):
        self.nama = nama
        self.visi = visi
        self.progress = []

    def berjuang(self):
        print(f"{self.nama} memulai perjuangan dari nol dengan visi: {self.visi}")
        for tahap in ['Riset', 'Eksekusi', 'Iterasi']:
            self.progress.append(tahap)
            print(f"Tahap: {tahap}")
        print(f"{self.nama} berhasil membangun sesuatu yang baru!")

if __name__ == "__main__":
    print("=== Pewaris ===")
    perjuangan_pewaris("Ryu Kintaro", "Perusahaan Keluarga")
    print("\n=== Perintis ===")
    ryu = Perintis("Ryu Kintaro", "Membawa inovasi digital")
    ryu.berjuang()

import random
from .legacy import Legacy

class Pewaris:
    """
    Pewaris yang mencoba melanjutkan dan mengembangkan warisan digital.
    """
    def __init__(self, nama: str) -> None:
        self.nama = nama

    def adaptasi(self, legacy: Legacy) -> str:
        """
        Simulasi adaptasi terhadap warisan digital.
        """
        hasil = random.choices(
            ["Berhasil Diperkuat", "Gagal Menyesuaikan", "Konflik Internal", "Inovasi Baru"],
            weights=[0.3, 0.3, 0.2, 0.2],
            k=1
        )[0]
        return hasil

    def narasi(self, legacy: Legacy, hasil: str) -> str:
        """
        Narasi reflektif berdasarkan hasil adaptasi.
        """
        if hasil == "Berhasil Diperkuat":
            return f"{self.nama} berhasil memperkuat legacy '{legacy.nama}' dan membuatnya relevan kembali."
        elif hasil == "Gagal Menyesuaikan":
            return f"{self.nama} gagal menyesuaikan legacy '{legacy.nama}' dengan zaman."
        elif hasil == "Konflik Internal":
            return f"{self.nama} mengalami konflik internal saat melanjutkan legacy '{legacy.nama}'."
        elif hasil == "Inovasi Baru":
            return f"{self.nama} mengubah legacy '{legacy.nama}' menjadi inovasi baru yang melampaui generasi sebelumnya."
        return "Narasi tidak tersedia."

from typing import List
from legacy import Legacy
from pewaris import Pewaris

class Simulator:
    """
    Simulasi pewarisan digital antara pewaris dan legacy.
    """
    def __init__(self, pewaris: Pewaris, legacy_pool: List[Legacy]) -> None:
        self.pewaris = pewaris
        self.legacy_pool = legacy_pool

    def jalankan(self) -> None:
        legacy = self.pilih_legacy()
        hasil = self.pewaris.adaptasi(legacy)
        narasi = self.pewaris.narasi(legacy, hasil)
        print(legacy.tampilkan_info())
        print(f"🎬 Hasil: {hasil}")
        print(f"📖 Narasi: {narasi}")
        self.simpan_log(legacy.nama, hasil, narasi)

    def pilih_legacy(self) -> Legacy:
        import random
        return random.choice(self.legacy_pool)

    def simpan_log(self, nama_legacy: str, hasil: str, narasi: str) -> None:
        with open("log_pewaris.txt", "a") as f:
            from time import ctime
            f.write(f"[{ctime()}] Legacy: {nama_legacy} | Hasil: {hasil} | Narasi: {narasi}\n")

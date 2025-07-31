from ide import ambil_ide
from eksekusi import eksekusi
from narasi import buat_narasi
from log import simpan_log

def jalankan():
    print("🎬 Hidup sebagai perintis ala Ryu Kintaro dimulai...")
    ide = ambil_ide()
    hasil = eksekusi(ide)
    narasi = buat_narasi(ide, hasil)
    print(f"📖 {narasi}")
    simpan_log(ide, hasil, narasi)
    print("✅ Selesai. Besok coba lagi!")

if __name__ == "__main__":
    jalankan()

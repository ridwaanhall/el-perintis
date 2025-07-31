from src.ide import ambil_ide
from src.eksekusi import eksekusi
from src.narasi import buat_narasi

def test_simulasi():
    ide = ambil_ide()
    hasil = eksekusi(ide)
    narasi = buat_narasi(ide, hasil)
    assert isinstance(narasi, str)
    print("✅ Test simulasi perintis berhasil.")

test_simulasi()

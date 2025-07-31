from src.legacy import Legacy
from src.pewaris import Pewaris

def test_adaptasi() -> None:
    legacy = Legacy("Test Legacy", ["Tantangan A", "Tantangan B"])
    pewaris = Pewaris("Tester")
    hasil = pewaris.adaptasi(legacy)
    narasi = pewaris.narasi(legacy, hasil)
    assert isinstance(narasi, str)
    print("✅ Test pewaris OOP berhasil.")

test_adaptasi()

from src.perjuangan import narasi_perjuangan

def test_narasi_perintis():
    hasil = narasi_perjuangan("Ryu", "perintis")
    assert "menapaki jalan sunyi" in hasil

def test_narasi_pewaris():
    hasil = narasi_perjuangan("Ryu", "pewaris")
    assert "menjaga bara warisan" in hasil

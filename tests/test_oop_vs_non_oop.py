from src.oop_vs_non_oop import Perintis, perjuangan_pewaris

def test_perintis(capsys):
    ryu = Perintis("Ryu", "Inovasi")
    ryu.berjuang()
    captured = capsys.readouterr()
    assert "memulai perjuangan" in captured.out
    assert "berhasil membangun" in captured.out

def test_pewaris(capsys):
    perjuangan_pewaris("Ryu", "Legacy")
    captured = capsys.readouterr()
    assert "melanjutkan perjuangan" in captured.out
    assert "berhasil menjaga warisan" in captured.out

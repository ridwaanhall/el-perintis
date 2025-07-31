from typing import List

class Legacy:
    """
    Representasi warisan digital yang bisa dilanjutkan oleh pewaris.
    """
    def __init__(self, nama: str, tantangan: List[str]) -> None:
        self.nama = nama
        self.tantangan = tantangan

    def tampilkan_info(self) -> str:
        return f"📜 Legacy: {self.nama} | Tantangan: {', '.join(self.tantangan)}"

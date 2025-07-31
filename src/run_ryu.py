import requests

class NarasiClient:
    """
    Client untuk berinteraksi dengan API Narasi.
    """

    def __init__(self, base_url: str):
        """
        Inisialisasi client dengan base URL dari API.
        """
        self.base_url = base_url

    def post_narasi(self, nama: str, tipe: str) -> dict:
        """
        Mengirim permintaan POST ke endpoint /narasi dengan data yang diberikan.

        Argumen:
            nama (str): Nama yang akan dikirim.
            tipe (str): Tipe yang akan dikirim.

        Mengembalikan:
            dict: Respons JSON dari server.
        """
        endpoint = f"{self.base_url}/narasi"
        payload = {"nama": nama, "tipe": tipe}
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()  # Menghasilkan error jika respons buruk
        return response.json()

if __name__ == "__main__":
    # Membuat instance client dengan base URL API
    client = NarasiClient("http://127.0.0.1:8000")
    # Mengirim permintaan POST dan mencetak responsnya
    result = client.post_narasi("Ryu", "perintis")
    print(result)
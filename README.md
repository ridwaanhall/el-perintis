# el-perintis

> "Menjadi perintis adalah menulis takdir sendiri. Menjadi pewaris adalah menjaga bara yang telah menyala."

Repositori ini mengeksplorasi filosofi membangun dari nol (perintis) versus melanjutkan legacy (pewaris) melalui analogi kode Python, narasi perjuangan, dan API sederhana. Inspirasi diambil dari kisah viral seperti Ryu Kintaro—antara membangun jalan sendiri atau meneruskan jejak yang ada.

## Fitur

- Simulasi OOP vs non-OOP: Analogi perintis (OOP, membangun fondasi baru) vs pewaris (non-OOP, melanjutkan pola lama).
- Narasi perjuangan: Fungsi Python yang menggambarkan perjalanan, kegagalan, dan kemenangan.
- API sederhana: Endpoint untuk menghasilkan narasi perjuangan secara dinamis.

## Struktur

- `src/`: Kode utama (simulasi, narasi, API)
- `tests/`: Unit test untuk setiap modul
- `requirements.txt`: Dependensi Python

## Filosofi

Setiap baris kode adalah pilihan: menulis ulang dunia atau memperbaiki warisan. Di dunia nyata, perintis dan pewaris saling melengkapi—seperti OOP dan non-OOP dalam pemrograman.

## Cara Menjalankan

```bash
pip install -r requirements.txt
python src/oop_vs_non_oop.py
python src/perjuangan.py
uvicorn src.api:app --reload
```

## Kontribusi

Buka PR untuk menambah narasi, analogi, atau memperluas API. Mari berdiskusi: mana yang lebih berat, membangun dari nol atau menjaga warisan?

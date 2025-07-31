# 🚀 el-perintis

_Simulasi hidup sebagai perintis digital, terinspirasi dari filosofi Ryu Kintaro._

> “Yang paling seru itu justru hidup sebagai perintis. Nggak ada yang nunjukin arah, nggak ada yang ngejamin hasil.” — Ryu Kintaro

---

## 🎯 Tujuan

**el-perintis** adalah skrip Python yang mensimulasikan perjalanan seorang perintis: mulai dari ide mentah, eksekusi, kegagalan, pivot, hingga potensi viral. Cocok untuk refleksi harian, konten motivasi, atau sebagai fondasi proyek digital yang lebih besar.

---

## 🧩 Fitur Utama

- 🔀 Randomisasi ide bisnis perintis
- ⚙️ Simulasi eksekusi dengan hasil dinamis (sukses, gagal, viral, pivot)
- 📖 Narasi reflektif berdasarkan hasil
- 📝 Logging otomatis ke `log_perintis.txt`
- 🧪 Unit test sederhana untuk validasi alur

---

## 📁 Struktur Proyek

```txt
el-perintis/
├── src/
│   ├── ide.py           # Generator ide bisnis
│   ├── eksekusi.py      # Simulasi eksekusi ide
│   ├── narasi.py        # Narasi berdasarkan hasil
│   ├── log.py           # Logging ke file
│   └── run_ryu.py       # Entry point utama
├── tests/
│   └── test_simulasi.py # Unit test sederhana
├── README.md
└── requirements.txt
```

---

## 🚀 Cara Menjalankan

```bash
python src/run_ryu.py
```

Setiap eksekusi akan menghasilkan satu narasi perintis dan mencatatnya ke `log_perintis.txt`.

---

## 🧪 Testing

```bash
python tests/test_simulasi.py
```

---

## 🔮 Potensi Pengembangan

- CLI interaktif dengan `argparse`
- Integrasi dengan API motivasi harian
- Dashboard web dengan Flask atau Django
- Mode komunitas: simpan ide dan narasi dari banyak pengguna

---

## 🧠 Filosofi

Proyek ini bukan sekadar skrip—ini adalah refleksi digital atas semangat perintis. Tidak ada jaminan, tidak ada arahan, tapi ada keberanian untuk mencoba dan mencatat prosesnya.

---

## 📜 Lisensi

MIT License. Bebas digunakan, dimodifikasi, dan dikembangkan.

---

## 🤝 Kontribusi

Terbuka untuk kontribusi! Kirim ide, narasi, atau fitur baru yang bisa memperkaya semangat perintis digital.

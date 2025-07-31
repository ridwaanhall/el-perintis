# 🔥 el-pewaris-oop

_Melanjutkan jejak, menjaga bara, dan memperkuat warisan digital dengan pendekatan OOP._

> “Menjadi perintis adalah menulis takdir sendiri. Menjadi pewaris adalah menjaga bara yang telah menyala.” — Adaptasi filosofi Ryu Kintaro

---

## 🎯 Deskripsi Proyek

**el-pewaris-oop** adalah simulasi berbasis Python yang menggambarkan perjalanan seorang pewaris digital. Proyek ini menggunakan paradigma **Object-Oriented Programming (OOP)** untuk merepresentasikan entitas seperti `Legacy`, `Pewaris`, dan `Simulator`, serta interaksi di antara mereka.

Tujuannya adalah untuk mengeksplorasi bagaimana seseorang dapat melanjutkan dan mengembangkan warisan digital—baik itu proyek open source, platform edukasi, atau konten viral—dengan tantangan dan narasi yang reflektif.

---

## 🧩 Fitur Utama

- 📜 Representasi warisan digital (`Legacy`) dengan tantangan spesifik
- 🧑‍🔧 Pewaris (`Pewaris`) yang mencoba mengadaptasi dan mengembangkan warisan
- 🎬 Simulator (`Simulator`) yang menjalankan proses pewarisan dan mencatat hasil
- 📖 Narasi reflektif berdasarkan hasil adaptasi
- 📝 Logging otomatis ke `log_pewaris.txt`
- 🧪 Unit test untuk validasi alur pewarisan

---

## 📁 Struktur Folder

```txt
el-pewaris-oop/
├── src/
│   ├── legacy.py        # Class Legacy: warisan digital
│   ├── pewaris.py       # Class Pewaris: pewaris yang mengadaptasi legacy
│   ├── simulator.py     # Class Simulator: menjalankan simulasi pewarisan
│   └── run.py           # Entry point utama
├── tests/
│   └── test_pewaris.py  # Unit test
├── README.md
└── requirements.txt
```

---

## 🚀 Cara Menjalankan

```bash
python src/run.py
```

Setiap eksekusi akan menghasilkan satu narasi pewaris dan mencatatnya ke `log_pewaris.txt`.

---

## 🧪 Testing

```bash
python tests/test_pewaris.py # python -m tests.test_pewaris
```

---

## 🧠 Filosofi OOP

- **Encapsulation**: Setiap entitas (`Legacy`, `Pewaris`, `Simulator`) memiliki atribut dan perilaku yang terpisah dan terstruktur.
- **Abstraction**: Detail implementasi disembunyikan di balik antarmuka kelas.
- **Inheritance**: Konsep pewarisan literal dan metaforis—kelas `Pewaris` mewarisi tantangan dari `Legacy`.
- **Polymorphism**: Narasi dan hasil adaptasi dapat bervariasi tergantung konteks warisan.

---

## 🔮 Potensi Pengembangan

- 🌐 Integrasi dengan API Flask untuk menyajikan narasi secara dinamis
- 📊 Visualisasi narasi pewaris vs perintis di dashboard `roneha.dev`
- 🧠 Mode reflektif: pengguna bisa menulis ulang narasi berdasarkan pengalaman pribadi

---

## 📜 Lisensi

MIT License. Bebas digunakan, dimodifikasi, dan dikembangkan.

---

## 🤝 Kontribusi

Buka PR untuk menambah narasi, analogi, atau memperluas simulasi. Mari berdiskusi: mana yang lebih berat, membangun dari nol atau menjaga warisan?

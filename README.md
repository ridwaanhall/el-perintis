# 🔥 el-perintis

> “Menjadi perintis adalah menulis takdir sendiri. Menjadi pewaris adalah menjaga bara yang telah menyala.” — Adaptasi filosofi Ryu Kintaro

Repositori ini mengeksplorasi dua jalur kehidupan digital:

- **Perintis**: membangun dari nol, penuh ketidakpastian dan eksplorasi.  
- **Pewaris**: melanjutkan legacy yang sudah ada, dengan tantangan adaptasi dan keberlanjutan.

Proyek ini menggunakan Python untuk mensimulasikan dua filosofi tersebut, baik dalam bentuk skrip sederhana maupun pendekatan OOP yang terstruktur.

---

## 🌿 Branch Overview

| Branch | Filosofi | Paradigma | Deskripsi Singkat |
|--------|----------|-----------|-------------------|
| [`perintis`](https://github.com/ridwaanhall/el-perintis/tree/perintis) | Membangun dari nol | Non-OOP | Skrip modular yang mensimulasikan ide, eksekusi, dan narasi perintis digital. |
| [`pewaris`](https://github.com/ridwaanhall/el-perintis/tree/pewaris)   | Melanjutkan legacy | OOP | Simulasi berbasis kelas (`Legacy`, `Pewaris`, `Simulator`) untuk menjaga dan mengembangkan warisan digital. |

---

## 🧩 Fitur Utama

- 🔀 Simulasi ide dan hasil (sukses, gagal, viral, pivot)
- 📖 Narasi reflektif berdasarkan hasil eksekusi
- 📝 Logging otomatis ke file (`log_perintis.txt` / `log_pewaris.txt`)
- 🧪 Unit test untuk validasi alur
- 🧠 Filosofi hidup digital: membangun vs melanjutkan

---

## 📁 Struktur Umum

```txt
el-perintis/
├── src/
│   ├── [perintis] run_ryu.py, ide.py, eksekusi.py, narasi.py, log.py
│   ├── [pewaris] legacy.py, pewaris.py, simulator.py, run.py
├── tests/
│   ├── test_perintis.py
│   ├── test_pewaris.py
├── README.md
└── requirements.txt
```

---

## 🚀 Cara Menjalankan

### Branch `perintis`

```bash
git checkout perintis
python src/run_ryu.py
```

### Branch `pewaris`

```bash
git checkout pewaris
python src/run.py
```

---

## 🧪 Testing

```bash
python -m tests.test_perintis     # Untuk perintis
python -m tests.test_pewaris      # Untuk pewaris
```

---

## 🔮 Potensi Pengembangan

- 🌐 Integrasi dengan API Flask untuk narasi dinamis
- 📊 Visualisasi narasi perintis vs pewaris di dashboard
- 🧑‍🤝‍🧑 Mode komunitas: pengguna bisa menyumbang ide atau warisan
- 🧭 Refleksi harian: motivasi dan log perjalanan digital

---

## 📜 Lisensi

MIT License. Bebas digunakan, dimodifikasi, dan dikembangkan.

---

## 🤝 Kontribusi

Buka PR untuk menambah narasi, analogi, atau memperluas simulasi.  
Mari berdiskusi: mana yang lebih berat, membangun dari nol atau menjaga warisan?

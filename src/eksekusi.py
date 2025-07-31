import random
import time

def eksekusi(ide):
    print(f"🚀 Menjalankan ide: {ide}")
    time.sleep(1)
    hasil = random.choices(
        ["Sukses", "Gagal", "Viral", "Pivot"],
        weights=[0.2, 0.5, 0.2, 0.1],
        k=1
    )[0]
    return hasil

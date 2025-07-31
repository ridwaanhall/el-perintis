def buat_narasi(ide, hasil):
    if hasil == "Sukses":
        return f"Ide '{ide}' berhasil menembus pasar. Kamu mulai dikenal sebagai perintis sejati."
    elif hasil == "Gagal":
        return f"Ide '{ide}' gagal total. Tapi kamu belajar banyak dan siap bangkit."
    elif hasil == "Viral":
        return f"Ide '{ide}' viral! Kamu jadi bahan obrolan di TikTok dan YouTube."
    elif hasil == "Pivot":
        return f"Ide '{ide}' mentok, tapi kamu putar arah dan temukan peluang baru."
    else:
        return "Perjalananmu masih panjang..."

import time

def simpan_log(ide, hasil, narasi):
    with open("log_perintis.txt", "a") as f:
        f.write(f"[{time.ctime()}] Ide: {ide} | Hasil: {hasil} | Narasi: {narasi}\n")

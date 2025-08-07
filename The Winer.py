import time
lirik = [
    ("The winner takes it all", 3),
    ("The loser has to fall ", 4),
    ("It's simple and it's plain", 4),
    ("Why should I complain?", 4),
]
waktu_mulai = time.time()  

for i, (teks_lirik, durasi_baris) in enumerate(lirik):
    target_mulai = sum(lirik[j][1] for j in range(i))
    waktu_sekarang = time.time() - waktu_mulai
    waktu_tunggu = target_mulai - waktu_sekarang
    if waktu_tunggu > 0:
        time.sleep(waktu_tunggu)
    
    jumlah_karakter = len(teks_lirik)
    delay_huruf = durasi_baris / jumlah_karakter if jumlah_karakter > 0 else 0
    
    for huruf in teks_lirik:
        print(huruf, end='', flush=True)
        time.sleep(delay_huruf)
    print()  
import time
letter_delay = 0.23
lyrics = [
    ("Duhai rembulan,Tahan dulu matahari datang",8.59),
    ("Malamnya indah, ku tak ingin cepat berakhir sudah",9.87),
    ("Tolong gemintang, senangi hati ini, jangan pulang", 11),
    ("Biar semua, melihat aku kamu", 30),
    ("Berseri, memohon waktu berhenti", 17),
    ("Untuk mengerti aku dan kamu begini, begitu", 17),
]
start_time = time.time()
for line_text, line_start in lyrics:
    current_time = time.time() - start_time
    time_to_wait = line_start - current_time
    if time_to_wait > 0:
        time.sleep(time_to_wait)
    for letter in line_text:
        print(letter, end='', flush=True)
        time.sleep(letter_delay)
    print()
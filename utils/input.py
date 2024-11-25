from datetime import datetime
from utils.times import check_conflict


# Fungsi untuk input data tugas dari pengguna dengan prioritas dan handling error yang lebih baik
def input_tasks():
    tasks = []
    while True:
        task_name = input("Masukkan nama tugas (atau 'selesai' untuk berhenti): ")
        if task_name.lower() == 'selesai':
            break
        while True:
            try:
                task_duration = float(input(f"Estimasi waktu untuk {task_name} (dalam jam): "))
                if task_duration <= 0:
                    print("Durasi harus lebih besar dari 0. Coba lagi.")
                    continue
                break
            except ValueError:
                print("Input tidak valid. Pastikan memasukkan angka untuk durasi.")

        while True:
            try:
                task_priority = int(input(f"Masukkan prioritas untuk {task_name} (5=tertinggi, 1=terendah): "))
                if task_priority < 1 or task_priority > 5:
                    print("Prioritas harus antara 1 dan 5. Coba lagi.")
                    continue
                break
            except ValueError:
                print("Input tidak valid. Pastikan memasukkan angka untuk prioritas (1-5).")
        
        # Tambahkan tugas dengan durasi dan prioritas ke dalam list
        tasks.append((task_name, task_duration, task_priority))  # Prioritas ditambahkan di sini
    return tasks

# Fungsi untuk mendapatkan waktu yang tidak bisa digunakan dari pengguna dengan validasi bentrok
def input_unavailable_periods(day, existing_unavailable_periods):
    unavailable_periods = existing_unavailable_periods[:]
    while True:
        print(f"Apakah ada jam yang tidak bisa dipakai pada hari {day}?")
        print("1. Ya")
        print("2. Tidak")
        print("3. Hari libur dari tugas")
        response = input().lower()

        if response == '2':
            break
        elif response == '3':
            # Tambahkan seluruh hari tidak tersedia
            unavailable_periods.append((datetime.strptime("00:00", "%H:%M"), datetime.strptime("23:59", "%H:%M")))
            break

        while True:
            try:
                start_time_str = input("Masukkan waktu mulai (HH:MM): ")
                end_time_str = input("Masukkan waktu berakhir (HH:MM): ")

                # Konversi input waktu
                start_time = datetime.strptime(start_time_str, "%H:%M")
                end_time = datetime.strptime(end_time_str, "%H:%M")

                # Validasi bahwa waktu berakhir harus setelah waktu mulai
                if end_time <= start_time:
                    print("Waktu berakhir harus setelah waktu mulai. Coba lagi.")
                    continue

                # Cek apakah ada bentrok dengan waktu yang sudah ada
                if check_conflict(unavailable_periods, start_time, end_time):
                    print("Waktu yang dipilih bentrok dengan waktu yang sudah tidak tersedia. Coba lagi.")
                else:
                    unavailable_periods.append((start_time, end_time))  # Tambahkan waktu yang tidak bisa digunakan
                    break

            except ValueError:
                print("Format waktu tidak valid. Coba lagi.")

        # Tanya apakah mau menambahkan waktu lain yang tidak tersedia
        more_unavailable = input("Apakah masih ada jam lain yang ingin dikosongkan di hari ini? (y/n) ").lower()
        if more_unavailable == 'n':
            break

    return unavailable_periods
from datetime import timedelta
from resources.population import get_available_slots, get_next_task


# Fungsi untuk mencetak jadwal lengkap dengan waktu mulai dan selesai
def print_schedule(best_schedule, unavailable_periods_per_day, max_hours_per_day):
    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    current_day_index = 0
    printed_days = set()

    # Lanjutkan penjadwalan hingga semua tugas selesai
    while best_schedule:
        # Dapatkan periode yang tidak tersedia untuk hari saat ini
        unavailable_periods = unavailable_periods_per_day.get(current_day_index % len(days_of_week), [])
        available_slots = get_available_slots(unavailable_periods, day_start=7, day_end=21)

        # Jika tidak ada slot waktu yang tersedia di hari ini
        if not available_slots:
            print(f"--- {days_of_week[current_day_index % len(days_of_week)]} ---")
            print("Tidak ada waktu yang tersedia di hari ini.")
            current_day_index += 1
            continue

        # Cetak header untuk hari yang baru jika belum dicetak
        if current_day_index not in printed_days:
            print(f"--- {days_of_week[current_day_index % len(days_of_week)]} ---")
            printed_days.add(current_day_index)

        # Jadwalkan tugas dalam slot yang tersedia
        for slot_start, slot_end in available_slots:
            current_time = slot_start
            while best_schedule and (current_time + timedelta(hours=best_schedule[0][1])) <= slot_end:
                task = get_next_task(best_schedule, (slot_end - current_time).seconds / 3600)  # Dapatkan tugas sesuai prioritas
                if task:
                    task_name, task_duration, task_priority = task
                    task_end_time = current_time + timedelta(hours=task_duration)
                    print(f"{task_name} ({current_time.strftime('%H:%M')} - {task_end_time.strftime('%H:%M')})")
                    current_time = task_end_time
                    best_schedule.remove(task)  # Hapus tugas dari jadwal setelah dicetak
                else:
                    break

        # Hitung waktu yang tersisa setelah penjadwalan
        remaining_time = sum((slot[1] - slot[0] for slot in available_slots), timedelta())
        print(f"Waktu yang tersisa di hari {days_of_week[current_day_index % len(days_of_week)]}: {remaining_time}")
        print(f"Waktu tidak tersedia di hari {days_of_week[current_day_index % len(days_of_week)]}:")
        for period in unavailable_periods:
            print(f"  {period[0].strftime('%H:%M')} - {period[1].strftime('%H:%M')}")

        # Lanjutkan ke hari berikutnya (loop kembali ke Senin jika sudah sampai Minggu)
        current_day_index += 1
from resources.population import get_available_slots, get_next_task

# Fungsi fitness untuk mengevaluasi seberapa baik solusi berdasarkan prioritas dan jumlah hari yang digunakan
def fitness(chromosome, unavailable_periods_per_day, max_days=7):
    total_priority_duration = 0  # Menyimpan total dari (prioritas * durasi) setiap tugas
    days_used = 0
    current_day_index = 0
    unscheduled_tasks = len(chromosome)
    
    # Lakukan penjadwalan untuk setiap hari
    while unscheduled_tasks > 0:
        available_slots = get_available_slots(unavailable_periods_per_day.get(current_day_index % max_days, []), day_start=7, day_end=21)
        available_hours = sum((slot[1] - slot[0]).seconds / 3600 for slot in available_slots)

        if available_hours > 0:
            tasks_scheduled = False  # Flag untuk mengecek apakah ada tugas yang dijadwalkan
            while available_hours > 0 and unscheduled_tasks > 0:
                task = get_next_task(chromosome, available_hours)
                if task:
                    task_name, task_duration, task_priority = task
                    available_hours -= task_duration
                    total_priority_duration += task_priority * task_duration  # Menghitung total prioritas * durasi
                    chromosome.remove(task)  # Hapus tugas yang sudah dijadwalkan
                    unscheduled_tasks -= 1
                    tasks_scheduled = True  # Set flag jika ada tugas yang dijadwalkan
                else:
                    break  # Tidak ada tugas yang bisa dijadwalkan dalam slot waktu ini

            if tasks_scheduled:
                days_used += 1  # Tambah hari yang digunakan jika ada tugas yang dijadwalkan
        
        current_day_index += 1

    # Menghitung nilai fitness berdasarkan hari yang digunakan
    if days_used > 0:
        return total_priority_duration / days_used
    else:
        return float('inf')  # Jika tidak ada hari yang digunakan, fitness tidak valid
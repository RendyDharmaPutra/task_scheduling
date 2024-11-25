import random
from datetime import datetime

# Fungsi untuk membuat populasi awal (solusi acak)
def generate_initial_population(tasks, population_size):
    population = []
    for _ in range(population_size):
        chromosome = tasks[:]  # Copy daftar tugas
        random.shuffle(chromosome)  # Acak urutan tugas
        population.append(chromosome)
    return population

# Fungsi untuk mendapatkan slot waktu yang tersedia berdasarkan periode tidak tersedia
def get_available_slots(unavailable_periods, day_start=7, day_end=21):
    day_start_dt = datetime.strptime(f"{day_start}:00", "%H:%M")
    day_end_dt = datetime.strptime(f"{day_end}:00", "%H:%M")
    available_slots = []

    if not unavailable_periods:
        available_slots.append((day_start_dt, day_end_dt))
        return available_slots

    # Sort unavailable periods
    sorted_unavailable = sorted(unavailable_periods, key=lambda x: x[0])

    current_time = day_start_dt

    for period_start, period_end in sorted_unavailable:
        if current_time < period_start:
            available_slots.append((current_time, period_start))
        current_time = max(current_time, period_end)

    if current_time < day_end_dt:
        available_slots.append((current_time, day_end_dt))

    return available_slots
# Fungsi untuk mendapatkan tugas-tugas sesuai prioritas dan durasi yang cocok dengan slot waktu
def get_next_task(chromosome, available_hours):
    for priority_level in range(5, 0, -1):  # Mulai dari prioritas tertinggi (5) ke terendah (1)
        for task in sorted(chromosome, key=lambda x: x[2], reverse=True):  # Urutkan berdasarkan prioritas
            task_name, task_duration, task_priority = task
            if task_priority == priority_level and task_duration <= available_hours:
                return task
    return None
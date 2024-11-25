from utils import input as input_lib, output as output_lib
from resources.main_algorithm import genetic_algorithm


# Fungsi utama untuk menjalankan program
def main():
    tasks = input_lib.input_tasks()
    max_hours_per_day = 14  # Misalnya hari kerja dari jam 07:00 sampai 21:00

    unavailable_periods_per_day = {}

    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    for day in days_of_week:
        day_index = days_of_week.index(day)
        unavailable_periods_per_day[day_index] = input_lib.input_unavailable_periods(day, [])

    while True:
        # Jalankan algoritma genetika untuk mendapatkan jadwal terbaik
        best_schedule, best_fitness = genetic_algorithm(tasks[:], unavailable_periods_per_day=unavailable_periods_per_day)

        # Tambahkan pembulatan, pastikan 0,5 ke atas
        if best_fitness % 1 >= 0.5:
            rounded_fitness = int(best_fitness) + 1  # Membulatkan ke atas jika desimal >= 0.5
        else:
            rounded_fitness = int(best_fitness)  # Membulatkan ke bawah jika desimal < 0.5

        print(f"\nJadwal terbaik ditemukan dengan fitness: {best_fitness}")
        print(f"Nilai fitness setelah pembulatan: {rounded_fitness}")
        output_lib.print_schedule(best_schedule.copy(), unavailable_periods_per_day, max_hours_per_day)

        # Tanya pengguna apakah ingin proses ulang atau sudah selesai
        while True:
            print("\nApakah Anda puas dengan jadwal ini?")
            print("1. Proses ulang")
            print("2. Sudah oke")
            choice = input("Masukkan pilihan (1 atau 2): ").lower()
            if choice == '1':
                break  # Proses ulang
            elif choice == '2':
                print("\nJadwal mingguan selesai.")
                return  # Selesai
            else:
                print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")

# Jalankan program utama
if __name__ == "__main__":
    main()
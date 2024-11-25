# Fungsi untuk memeriksa bentrok waktu
def check_conflict(unavailable_periods, start_time, end_time):
    for period in unavailable_periods:
        if (start_time >= period[0] and start_time < period[1]) or \
           (end_time > period[0] and end_time <= period[1]) or \
           (start_time <= period[0] and end_time >= period[1]):
            return True
    return False

# Fungsi untuk mendapatkan waktu yang tersedia berikutnya setelah periode tidak tersedia
def get_next_available_time(unavailable_periods, start_time, end_of_day):
    for period in unavailable_periods:
        if start_time < period[0]:
            return start_time
        elif period[0] <= start_time < period[1]:
            return period[1]
    return start_time if start_time < end_of_day else end_of_day
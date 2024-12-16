import random


def selection(population, fitness_scores, elite_size=2):
    # Urutkan populasi berdasarkan nilai fitness (terbaik ke terburuk)
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), key=lambda pair: pair[0])]

    # Ambil elit terbaik sesuai ukuran elite_size
    elite = sorted_population[:elite_size]

    # Ambil sisa populasi terbaik untuk dipilih crossover
    remaining_population = sorted_population[:len(sorted_population) // 2]

    # Gabungkan elit dengan populasi terpilih untuk crossover
    return elite + remaining_population

# Fungsi crossover: membuat solusi baru dari dua orang tua
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + [task for task in parent2 if task not in parent1[:crossover_point]]
    return child

# Fungsi mutasi: secara acak mengacak urutan tugas di dalam kromosom
def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
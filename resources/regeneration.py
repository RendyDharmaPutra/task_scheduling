import random


# Fungsi seleksi: memilih orang tua untuk crossover
def selection(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), key=lambda pair: pair[0])]
    return sorted_population[:len(sorted_population) // 2]

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
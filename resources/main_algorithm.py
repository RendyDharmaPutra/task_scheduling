import random
from resources import  fitness, regeneration 
from resources.population import generate_initial_population

# Algoritma Genetika
def genetic_algorithm(tasks, population_size=10, generations=100, mutation_rate=0.1, unavailable_periods_per_day=None):
    # Buat populasi awal
    population = generate_initial_population(tasks, population_size)

    for generation in range(generations):
        # Hitung fitness untuk setiap kromosom
        fitness_scores = [fitness.fitness(chromosome[:], unavailable_periods_per_day) for chromosome in population]

        # Menampilkan informasi generasi
        best_fitness_in_generation = min(fitness_scores)
        print(f"Generasi {generation + 1} - Fitness terbaik: {best_fitness_in_generation}")

        # Pembulatan nilai fitness sesuai aturan
        if best_fitness_in_generation % 1 < 0.5:
            rounded_fitness = int(best_fitness_in_generation)  # Dibulatkan ke bawah
        else:
            rounded_fitness = int(best_fitness_in_generation) + 1  # Dibulatkan ke atas

        # Tampilkan nilai fitness asli dan setelah pembulatan
        print(f"Nilai fitness setelah pembulatan: {rounded_fitness}")

        # Jika solusi optimal ditemukan (fitnes terbaik 1), selesai
        if best_fitness_in_generation == 1:
            print(f"Solusi optimal ditemukan di generasi {generation + 1}")
            break

        # Seleksi: pilih individu terbaik untuk generasi berikutnya
        selected_population = regeneration.selection(population, fitness_scores)

        # Crossover: buat generasi baru
        next_population = []
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(selected_population, 2)
            child = regeneration.crossover(parent1, parent2)
            regeneration.mutate(child, mutation_rate)
            next_population.append(child)

        population = next_population  # Update populasi dengan generasi baru

    # Ambil kromosom terbaik dari generasi terakhir
    fitness_scores = [fitness.fitness(chromosome[:], unavailable_periods_per_day) for chromosome in population]
    best_chromosome = population[fitness_scores.index(min(fitness_scores))]
    best_fitness = min(fitness_scores)

    return best_chromosome, best_fitness
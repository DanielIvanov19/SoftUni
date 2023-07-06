population = [int(x) for x in input().split(', ')]

min_population = int(input())

max_population = max(population)
index_of_max = population.index(max_population)
sum_of_lack = 0
count_parts_lacking = 0

for part in population:
    if part < min_population:
        count_parts_lacking += 1
        sum_of_lack += (min_population - part)
difference = max_population - sum_of_lack
if difference >= min_population:
    for i in range(len(population) - 1):
        if population[i] < min_population:
            need = min_population - population[i]
            population[i] += need
            population[index_of_max] -= need
    print(population)
else:
    print("No equal distribution possible")
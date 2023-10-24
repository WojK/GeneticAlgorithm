from Chromosome import Chromosome
from GeneticAlgorithm import GeneticAlgorithm
from Population import Population
import matplotlib.pyplot as plt 


def fun(x):
    return -0.2*pow(x,2) + 6*x + 7

range_from = -1
range_to = 31
population_size = 11
mutation_probability = 0.001
crossover_probability = 1
reproduction_steps = 15



max_abs_range_value = max(abs(range_from), abs(range_to))
chromosome_size = max_abs_range_value.bit_length() + 1

population = Population(population_size, chromosome_size, range_from, range_to, fun)
genetic_algorithm = GeneticAlgorithm(chromosome_size, population_size, range_from, range_to, fun, mutation_probability, crossover_probability)

stats = []
stats.append(population.get_max_min_avg_fitness())

for i in range(reproduction_steps):
    population = genetic_algorithm.generate_new_population(population)
    stats.append(population.get_max_min_avg_fitness())

fittest = population.get_fittest()
fittest_value = fittest.to_decimal(fittest.genes)
print("Najlepiej przystosowany osobnik z populacji to: ", fittest_value )
print("Funkcja przyjmuje dla niego wartosc rowna: ", fun(fittest_value) )

function_graph_p_x = [i for i in range(range_from, range_to+1)]
function_graph_p_y = [fun(i) for i in function_graph_p_x]


plt.xlabel("x") 
plt.ylabel("f(x)") 
plt.grid()
plt.title("Wykres funkcji") 

plt.scatter(function_graph_p_x, function_graph_p_y, color="red") 
plt.savefig("../wykres_funkcji.png")
plt.show()


graph_stats_x = [i for i in range(reproduction_steps+1)]

max_values_y = [i[0] for i in stats]
min_values_y = [i[1] for i in stats]
avg_values_y = [i[2] for i in stats]



plt.xlabel("Populacja") 
plt.ylabel("Przystosowanie") 
plt.title("Wizualizacja wynikow przystosowania kolejnych populacji") 

plt.plot(graph_stats_x, min_values_y, label="Min")
plt.plot(graph_stats_x, max_values_y, label="Max")
plt.plot(graph_stats_x, avg_values_y, label="Avg")

plt.legend() 
plt.savefig("../wyniki_przystosowania.png")
plt.show() 

import random
import numpy as np
from Chromosome import Chromosome
from Population import Population
import math

class GeneticAlgorithm():
    
    def __init__(self, chromosome_size, population_size, range_from, range_to, function, mutation_rate, crossover_probability):
        self.chromosome_size = chromosome_size
        self.population_size = population_size
        self.range_from = range_from
        self.range_to = range_to
        self.function = function
        self.mutation_rate = mutation_rate
        self.crossover_probability = crossover_probability
        

    def reproduce(self, population:Population):
        reproduction = []
        for i in range(len(population.chromosomes)):
            reproduction.append(self.roulete_wheel_selection(population))
        return reproduction
        

    def pop_random(self, parents_list):
        index = random.randrange(0, len(parents_list))
        return parents_list.pop(index)

    def generate_new_population(self, population:Population):
        
        new_population_parents = self.reproduce(population)
        
        parents_pairs = []
        for i in range(math.floor(len(population.chromosomes)/2)):
            parents_pairs.append([self.pop_random(new_population_parents), self.pop_random(new_population_parents)])

        
        crossovered_individuals = []
        for pair in parents_pairs:
            children = self.crossover(pair[0], pair[1])
            crossovered_individuals.append(children[0])
            crossovered_individuals.append(children[1])
        
        if len(new_population_parents) % 2 != 0:
            crossovered_individuals.append(new_population_parents.pop())
         

        new_population_individulas = []
        for individual in crossovered_individuals:
            new_individual = self.mutation(individual)
            new_population_individulas.append(new_individual)


        new_population = Population(self.population_size, self.chromosome_size, self.range_from, self.range_to, self.function, False)
        new_population.chromosomes = new_population_individulas
        new_population.count_chromosomes_fitness()

        return new_population
                                                            
        
    
    def roulete_wheel_selection(self, population:Population):
        sum_of_all_fitness = sum([chromosome.fitness for chromosome in population.chromosomes])
        selection_probs = [chromosome.fitness/sum_of_all_fitness for chromosome in population.chromosomes]
        return population.chromosomes[np.random.choice(len(population.chromosomes), p=selection_probs)]


    def crossover(self, chromosome_1:Chromosome, chromosome_2:Chromosome):
        if random.uniform(0,1) > self.crossover_probability:
           return [chromosome_1, chromosome_2]

        crossover_point = random.randrange(1, self.chromosome_size)
        
        ch1_1_part = chromosome_1.genes[:crossover_point]
        ch1_2_part = chromosome_1.genes[crossover_point:]
        ch2_1_part = chromosome_2.genes[:crossover_point]
        ch2_2_part = chromosome_2.genes[crossover_point:]

            
        child_1_genes = "".join(ch1_1_part + ch2_2_part)
        child_2_genes = "".join(ch2_1_part + ch1_2_part)

        decimal_1 = chromosome_1.to_decimal(child_1_genes)
        decimal_2 = chromosome_1.to_decimal(child_2_genes)

        child_1 = Chromosome(self.chromosome_size, self.range_from, self.range_to, self.function)
        if decimal_1 >= self.range_from and decimal_1 <= self.range_to:
            child_1.add_new_genes(child_1_genes)
            
        child_2 = Chromosome(self.chromosome_size, self.range_from, self.range_to, self.function)
        if decimal_2 >= self.range_from and decimal_2 <= self.range_to:
            child_2.add_new_genes(child_2_genes)
        
        return [child_1, child_2]
    

    def mutation(self, chromosome:Chromosome):
        genes = list(chromosome.genes)
        for i in range(len(genes)):
            if random.uniform(0,1) < self.mutation_rate:
                genes[i] = "0" if genes[i] == "1" else "1"
        
        genes = "".join(genes)
        new_chromosome = Chromosome(self.chromosome_size, self.range_from, self.range_to, self.function)
        decimal_genes = new_chromosome.to_decimal(genes)
        if decimal_genes >= self.range_from and decimal_genes <= self.range_to:
            new_chromosome.add_new_genes(genes)            
        return new_chromosome
            
        

        

        
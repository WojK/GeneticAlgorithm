from Chromosome import Chromosome


class Population():
    def __init__(self, population_size, chromosome_size, range_from, range_to, function, initial_population = True):
        self.chromosomes = []
        if initial_population == True:
            for i in range(population_size):
                self.chromosomes.append(Chromosome(chromosome_size, range_from, range_to, function))
        

    def count_chromosomes_fitness(self):
        for c in self.chromosomes:
            c.count_fitness()
        
        chromosomes_copy = self.chromosomes
        chromosomes_copy.sort(key= lambda x:x.fitness, reverse=True)
        if chromosomes_copy[-1].fitness < 0:
            value = abs(chromosomes_copy[-1].fitness)
            for c in self.chromosomes:
                c.fitness += value
            


    def get_max_min_avg_fitness(self):
        self.count_chromosomes_fitness()
        self.chromosomes.sort(key= lambda x:x.fitness, reverse=True)
        
        total = sum([c.fitness for c in self.chromosomes])
        avg = total/len(self.chromosomes)
        
        return [self.chromosomes[0].fitness, self.chromosomes[-1].fitness, avg]
    
    def get_fittest(self):
        for c in self.chromosomes:
            c.count_fitness()
        
        chromosomes_copy = self.chromosomes
        chromosomes_copy.sort(key= lambda x:x.fitness, reverse=True)
        return chromosomes_copy[0]




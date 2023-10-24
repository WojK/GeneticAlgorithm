import random


class Chromosome:
    

    def __init__(self, chromosome_size, range_from, range_to, function):
        self.chromosome_size = chromosome_size
        self.function = function
        self.genes = self.rand_individual_from_to_range(range_from, range_to)
        self.decimal = self.to_decimal(self.genes)
        self.count_fitness()
     
    def add_new_genes(self, genes):
        self.genes = genes
        self.decimal = self.to_decimal(self.genes)
        
    def to_decimal(self, genes):
        decimal = int(genes[1:], 2)
        if(genes[0] == "0"):
            decimal *= -1
        
        return decimal
    
    def rand_individual_from_to_range(self, range_from, range_to):
        genes = self.rand_individual()
        decimal = self.to_decimal(genes)
        while(decimal < range_from or range_to < decimal):
            genes = self.rand_individual()
            decimal = self.to_decimal(genes)
        
        return genes
            
        
    def rand_individual(self):
        genes = ""
        for i in range(self.chromosome_size):
            genes += str(random.randint(0,1))
        return genes


    def count_fitness(self):
        self.decimal = self.to_decimal(self.genes)
        self.fitness = self.function(self.decimal)

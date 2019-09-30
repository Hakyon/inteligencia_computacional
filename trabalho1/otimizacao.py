import random

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

from pprint import pprint

import numpy

TAM_CROMOSSOMO = 14
TAM_POPULACAO = 200


class Otimizacao(object):
    def __init__(self):
        pass

    def bit_to_dec(self, bits):
        decval = 0
        for i in range(7):
            decval += bits[i] * (2 ** i)

        return decval

    def fitness(self, cromossomo):
        n1 = self.bit_to_dec(cromossomo[:7])
        n2 = self.bit_to_dec(cromossomo[7:])

        # 50x + 24y ≤ 2400
        # 30x + 33y ≤ 2100
        s1 = 50 * n1 + 24 * n2
        s2 = 30 * n1 + 33 * n2

        if s1 > 2400 or s2 > 2100:
            return -999,

        return s1 + s2,

    def start(self):

        # Define a estrategia do fitness
        # - weights: define se o problema é de maximizacao (+1) ou minimizacao (-1)
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))

        # Define a estrutura do cromossomo
        creator.create("Individual", list, fitness=creator.FitnessMax)

        # Define os componentes para configurar a populacao
        toolbox = base.Toolbox()

        # Gerador para os individuos
        toolbox.register("attr_bool", random.randint, 0, 1)

        # Inicializador da populacao
        toolbox.register("individual",
                         tools.initRepeat,
                         creator.Individual,
                         toolbox.attr_bool, TAM_CROMOSSOMO)

        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        # Cria a populacao inicial
        populacao = toolbox.population(n=TAM_POPULACAO)

        # Define os operadores geneticos
        toolbox.register("evaluate", self.fitness)

        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        # toolbox.register("select", tools.selRoulette)
        toolbox.register("select", tools.selTournament, tournsize=3)

        hof = tools.HallOfFame(10)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        pop, log = algorithms.eaSimple(populacao,
                                       toolbox,
                                       cxpb=1,
                                       mutpb=0.1,
                                       ngen=100,
                                       stats=stats,
                                       halloffame=hof,
                                       verbose=True)

        melhor = sorted([(x, x.fitness.values) for x in pop], key=lambda x: x[1], reverse=True)[0][0]

        xVal = self.bit_to_dec(melhor[:7])
        yVal = self.bit_to_dec(melhor[7:])

        print(f'x: {xVal} | y: {yVal}')


if __name__ == "__main__":
    otimizacao = Otimizacao()
    otimizacao.start()

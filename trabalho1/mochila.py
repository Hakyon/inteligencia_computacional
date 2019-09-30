import random

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

from pprint import pprint

import numpy

TAM_CROMOSSOMO = 12
TAM_POPULACAO = 100
ITENS_MOCHILA = [
    ['bug repellent', 12, 2],
    ['camp stove', 5, 4],
    ['canteen (full)', 10, 7],
    ['clothes', 11, 5],
    ['dried food', 50, 3],
    ['first-aid kit', 15, 3],
    ['flashlight', 6, 2],
    ['novel', 4, 2],
    ['rain gear', 5, 2],
    ['sleeping bag', 25, 3],
    ['tent', 20, 11],
    ['water filter', 30, 1],

]


class Mochila(object):

    def __init__(self):
        pass

    # Definição da função de fitness
    def fitness(self, cromossomo):
        """Funcao fitness para maximizar o cromossomo
        Deve retornar uma tupla!!!
        """

        peso = 0
        preferencia = 0
        for i in range(TAM_CROMOSSOMO):
            if cromossomo[i] == 1:
                peso += ITENS_MOCHILA[i][2]
                preferencia += ITENS_MOCHILA[i][1]

        if peso > 20:
            return -1,

        return preferencia

    def reproducao(self, pais, taxa_mutacao):
        """Executa o crossover e a mutacao"""

        filhos = []
        for casal in pais:
            p1 = casal[0][0]
            p2 = casal[1][0]

            # Crossover
            corte = randint(1, len(p1) - 1)

            f1 = p1[:corte] + p2[corte:]
            f2 = p2[:corte] + p1[corte:]

            # Mutacao
            for i in range(len(f1)):
                if random() < taxa_mutacao:
                    f1[i] = 0 if f1[i] == 1 else 1

            for i in range(len(f2)):
                if random() < taxa_mutacao:
                    f2[i] = 0 if f2[i] == 1 else 1

            filhos.append((f1, self.fitness(f1)))
            filhos.append((f2, self.fitness(f2)))

            return filhos

    def gerar_populacao_inicial(self, tam_populacao, tam_cromossomo):
        populacao = []
        for i in range(tam_populacao):
            cromossomo = [randint(0, 1) for _ in range(tam_cromossomo)]
            populacao.append(cromossomo)
        return populacao

    def start(self):

        # define se o problema é de maximizacao (+1) ou minimizacao (-1)
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

        # Define os operadores geneticos
        toolbox.register("evaluate", self.fitness)

        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        # Cria a populacao inicial
        populacao = toolbox.population(n=TAM_POPULACAO)

        pprint(populacao)

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

        melhor = sorted([(x, x.fitness.values) for x in pop], key=lambda x: x[1], reverse=True)

        i = 0
        for cromossomo in melhor[0][0]:
            if (cromossomo == 1):
                pprint(ITENS_MOCHILA[i][0])
            i += 1

        print(melhor[0])


if __name__ == "__main__":
    mochila = Mochila()
    mochila.start()

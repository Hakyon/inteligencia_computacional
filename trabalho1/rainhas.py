import random

from deap import base
from deap import creator
from deap import tools

from pprint import pprint

import numpy

TAM_CROMOSSOMO = 64
TAM_POPULACAO = 100


class ProblemaRainhas(object):
    def __init__(self):
        pass

    def fitness(self, cromossomo):
        """Funcao fitness para maximizar o cromossomo
        Deve retornar uma tupla!!!
        """
        count = 0
        for i in range(TAM_CROMOSSOMO):
            if cromossomo[i] == 1:
                count += 1

        # Máximo 8 rainhas por cromossomo
        if (count != 8):
            return 99999,

        for i in range(TAM_CROMOSSOMO):
            # Separa o tabuleiro por linhas
            fin = 8
            ant = 0
            tabuleiro = []
            for j in range(8):
                tabuleiro.append(cromossomo[ant:fin])
                ant = fin
                fin += 8

        return avalia_tabuleiro(tabuleiro),

    def start(self):
        pass


if __name__ == "__main__":
    rainha = ProblemaRainhas()
    rainha.start()

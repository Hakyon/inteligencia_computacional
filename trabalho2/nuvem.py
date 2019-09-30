from math import e
from random import uniform, random, randint
from pprint import pprint

LIMITES = [
    (0, 40),  # Limite de p
    (0, 30),  # Limite de m
]

VEL_MIN = -0.2
VEL_MAX = 0.2


class NuvemParticulas(object):
    def __init__(self):
        pass

    def funcao_objetivo(self, solucao):
        """
        A funcao objetivo avalia uma solucao e retorna um valor
        indicando se a solucao eh boa ou ruim.
        :param solucao:
        :return:
        """
        x, y = solucao

        # P <= 40
        # M <= 30
        # P e M >= 0
        if (x > 40 or y > 30 or x < 0 or y < 0):
            return -999

    def pso(self, tam_populacao: int,
            max_iteracoes: int,
            c1: float,
            c2: float,
            w: float) -> list:
        """
        Execucao PSO.

        :param tam_populacao:  numero de particulas
        :param c1: coeficiente cognitivo (valor entre 1 e 2)
        :param c2: coeficiente social (valor entre 1 e 2)
        :param w: inercia (valor entre 0.4 e 0.9)
        :return:
        """

        # 1. Define a populacao inicial
        populacao = [criar_solucao() for j in range(tam_populacao)]
        # pprint(populacao)

        # 2. Calcula o fitness da populacao
        velocidade = [[0, 0] for i in range(tam_populacao)]
        fitness = [funcao_objetivo(s) for s in populacao]

    def start(self):
        return


if __name__ == "__main__":
    nuvem = NuvemParticulas()
    nuvem.start()

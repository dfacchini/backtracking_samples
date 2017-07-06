# -*- coding: utf-8 -*-
import random
from itertools import groupby


def valor_valido(mapa, x, y, valor):
    """
    Classe que testa se o valor respeita as regras de repetição no mapa.
    """
    if mapa[x][y] != 0 or valor == 0:
        return False

    for indice in range(0, len(mapa)):
        if mapa[x][indice] == valor:
            return False
        if mapa[indice][y] == valor:
            return False

    return True


def backtracking(mapa):
    for x in range(0, len(mapa)):
        for y in range(0, len(mapa)):
            if mapa[x][y] == 0:
                pass
            else:
                for tester in range(1, 10):
                    if valor_valido(mapa, x, y, tester):
                        mapa[x][y] = tester
                        break


def main():
    mapa = [[5, 3, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0]]

    sub_mapa = [[5, 3, 0],
                [6, 0, 0],
                [0, 9, 8]]

    print '\n'
    for areas in mapa:
        area = ''
        for celula in areas:
            area += '%s  ' % celula
        print area + '\n'
    print '\n'


    print '\n Sub-Mapa\n'
    for areas in sub_mapa:
        area = ''
        for celula in areas:
            area += '%s  ' % celula
        print area + '\n'
    print '\n'


    from IPython import embed; embed()


main()

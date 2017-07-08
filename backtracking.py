# -*- coding: utf-8 -*-


def busca_estado_vazio(mapa):
    for x in range(0, len(mapa)):
        for y in range(0, len(mapa)):
            if mapa[x][y] == 0:
                return (x, y)


def valor_valido(mapa, x, y, valor):
    """
    Classe que testa se o valor respeita as regras de repetição no mapa.
    """
    if mapa[x][y] != 0 or valor == 0:
        return False

    for indice in range(0, len(mapa)):
        if mapa[x][indice] == valor or mapa[indice][y] == valor:
            return False

    quandrante_x = x/3*3
    quandrante_y = y/3*3

    for indice_x in range(quandrante_x, quandrante_x+3):
        for indice_y in range(quandrante_y, quandrante_x+3):
            if mapa[quandrante_x][quandrante_y] == valor:
                return False

    return True


def backtracking(mapa):

    posicao = busca_estado_vazio(mapa)
    if not posicao:
        return True
    for tester in range(1, 10):
        if valor_valido(mapa, posicao[0], posicao[1], tester):
            mapa[posicao[0]][posicao[1]] = tester
            if backtracking(mapa):
                return True
            else:
                mapa[posicao[0]][posicao[1]] = 0


def print_mapa(mapa):
    for areas in mapa:
        area = ''
        for celula in areas:
            area += '%s  ' % celula
        print area + '\n'
    print '\n'


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
    print_mapa(sub_mapa)

    backtracking(sub_mapa)

    print '\n Sub-Mapa Resolvido\n'
    print_mapa(sub_mapa)

    from IPython import embed; embed()


main()

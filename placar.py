vitorias_x = 0
vitorias_o = 0


def adicionar_vitoria(jogador):

    global vitorias_x, vitorias_o

    if jogador == "X":
        vitorias_x += 1

    if jogador == "O":
        vitorias_o += 1


def mostrar_placar():

    return {
        "x": vitorias_x,
        "o": vitorias_o
    }
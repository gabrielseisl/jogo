import random
import placar

tabuleiro = [""] * 9
jogador = "X"
jogo_encerrado = False


def verificar_vencedor():
    if (
        tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != "" or
        tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != "" or
        tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != "" or
        tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != "" or
        tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != "" or
        tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != "" or
        tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != "" or
        tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ""
    ):
        return True

    return False


def jogar(posicao):
    global jogador, jogo_encerrado

    if jogo_encerrado:
        return {
            "tabuleiro": tabuleiro,
            "resultado": "O jogo acabou! Clique em Reiniciar."
        }

    if posicao < 0 or posicao > 8:
        return {
            "tabuleiro": tabuleiro,
            "resultado": "Posição inválida!"
        }

    if tabuleiro[posicao] != "":
        return {
            "tabuleiro": tabuleiro,
            "resultado": ""
        }

    tabuleiro[posicao] = jogador

    if verificar_vencedor():
        jogo_encerrado = True
        placar.adicionar_vitoria(jogador)

        return {
            "tabuleiro": tabuleiro,
            "resultado": jogador + " ganhou!"
        }

    if "" not in tabuleiro:
        jogo_encerrado = True

        return {
            "tabuleiro": tabuleiro,
            "resultado": "Empate!"
        }

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

    return {
        "tabuleiro": tabuleiro,
        "resultado": ""
    }


def jogar_bot(posicao):
    global jogo_encerrado

    if jogo_encerrado:
        return {
            "tabuleiro": tabuleiro,
            "resultado": "O jogo acabou! Clique em Reiniciar."
        }

    if posicao < 0 or posicao > 8:
        return {
            "tabuleiro": tabuleiro,
            "resultado": "Posição inválida!"
        }

    if tabuleiro[posicao] != "":
        return {
            "tabuleiro": tabuleiro,
            "resultado": ""
        }

    tabuleiro[posicao] = "X"

    if verificar_vencedor():
        jogo_encerrado = True
        placar.adicionar_vitoria("X")

        return {
            "tabuleiro": tabuleiro,
            "resultado": "X ganhou!"
        }

    if "" not in tabuleiro:
        jogo_encerrado = True

        return {
            "tabuleiro": tabuleiro,
            "resultado": "Empate!"
        }

    casas_vazias = []

    for i in range(9):
        if tabuleiro[i] == "":
            casas_vazias.append(i)

    posicao_bot = random.choice(casas_vazias)
    tabuleiro[posicao_bot] = "O"

    if verificar_vencedor():
        jogo_encerrado = True
        placar.adicionar_vitoria("O")

        return {
            "tabuleiro": tabuleiro,
            "resultado": "O ganhou!"
        }

    if "" not in tabuleiro:
        jogo_encerrado = True

        return {
            "tabuleiro": tabuleiro,
            "resultado": "Empate!"
        }

    return {
        "tabuleiro": tabuleiro,
        "resultado": ""
    }
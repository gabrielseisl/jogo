import jogo


def reiniciar():
    jogo.tabuleiro[:] = [""] * 9
    jogo.jogador = "X"
    jogo.jogo_encerrado = False

    return {
        "tabuleiro": jogo.tabuleiro,
        "resultado": ""
    }
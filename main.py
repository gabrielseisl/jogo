from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import jogo
import reiniciar
import placar

app = FastAPI()

app.mount("/html", StaticFiles(directory="html"), name="html")
app.mount("/sons", StaticFiles(directory="sons"), name="sons")


@app.get("/")
def home():
    return FileResponse("html/inicio.html")


@app.get("/inicio")
def inicio():
    return FileResponse("html/inicio.html")


@app.get("/jogo")
def jogo_bot():
    reiniciar.reiniciar()

    return FileResponse("html/jogo.html")


@app.get("/jogador")
def jogo_jogador():
    reiniciar.reiniciar()

    return FileResponse("html/index.html")


@app.get("/regras")
def regras():
    return FileResponse("html/regras.html")


@app.get("/Placar")
def placar_jogo():
    return FileResponse("html/placar.html")


@app.get("/placar")
def mostrar_placar():
    return placar.mostrar_placar()


@app.get("/sons.js")
def get_sons_js():
    return FileResponse("sons.js")


@app.post("/jogar/{posicao}")
def fazer_jogada(posicao: int):
    return jogo.jogar(posicao)


@app.post("/jogar-bot/{posicao}")
def fazer_jogada_bot(posicao: int):
    return jogo.jogar_bot(posicao)


@app.post("/reiniciar")
def reiniciar_jogo():
    return reiniciar.reiniciar()
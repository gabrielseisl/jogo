function tocarSomVitoria() {
    let audio = new Audio('/sons/clique.mp3');
    audio.play().catch(error => {
        console.log("Erro ao reproduzir áudio:", error);
    });
}

function tocarSomEmpate() {
    let audio = new Audio('/sons/empate.mp3');
    audio.play().catch(error => {
        console.log("Erro ao reproduzir áudio:", error);
    });

}
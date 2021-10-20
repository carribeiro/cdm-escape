const btn_refresh_status = document.querySelector('#btn-refresh-status')
btn_refresh_status.addEventListener('click', function(){
    requestStatus();
});

// Chamada Ajax para atualizar status dos LEDs

function updateStatus(resposta) {

    // reed bicicleta
    document.querySelector('#status-reed-bicicleta').className = (resposta.bicicleta ? "dot dotVerde" : "dot dotCinza");

}

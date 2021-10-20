const btn_refresh_status = document.querySelector('#btn-refresh-status')
btn_refresh_status.addEventListener('click', function(){
    requestStatus();
});

// Chamada Ajax para atualizar status dos LEDs

function updateStatus(resposta) {


    document.querySelector('#status-reed-bicicleta').className = ((resposta.bicicleta > 0) ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#count-reed-bicicleta').innerHTML = resposta.bicicleta;
    document.querySelector('#status-tomadas-armario').className = (resposta.tomadas_armario ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-mesa-passar').className = ((resposta.mesa_passar > 0) ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#count-mesa-passar').innerHTML = resposta.mesa_passar;
    document.querySelector('#status-quiz-geladeira').className = ((resposta.geladeira > 0) ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#count-quiz-geladeira').innerHTML = resposta.geladeira;
    document.querySelector('#status-botao-aparador').className = (resposta.aparador ? "dot dotVerde" : "dot dotCinza");

}

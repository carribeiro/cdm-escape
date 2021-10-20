const btn_reset_cartao_geladeira = document.querySelector('#btn-reset-cartao-geladeira')
const btn_reset_cartao_microondas = document.querySelector('#btn-reset-cartao-microondas')
const btn_reset_cartao_lavadora = document.querySelector('#btn-reset-cartao-lavadora')

btn_reset_cartao_geladeira.addEventListener('click', function(){ requestResetCartaoGeladeira(); }); 
btn_reset_cartao_microondas.addEventListener('click', function(){ requestResetCartaoMicroondas(); }); 
btn_reset_cartao_lavadora.addEventListener('click', function(){ requestResetCartaoLavadora(); }); 

// Chamada Ajax para atualizar status dos LEDs

function updateStatus(resposta) {
    // sensores de cartão geladeira, microondas e lavadora
    document.querySelector('#status-cartao-geladeira').className = ((resposta.cartao_geladeira > 0) ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-cartao-microondas').className = ((resposta.cartao_microondas > 0) ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-cartao-lavadora').className = ((resposta.cartao_lavadora > 0) ? "dot dotVerde" : "dot dotCinza");

    document.querySelector('#count-cartao-geladeira').innerHTML = resposta.cartao_geladeira;
    document.querySelector('#count-cartao-microondas').innerHTML = resposta.cartao_microondas;
    document.querySelector('#count-cartao-lavadora').innerHTML = resposta.cartao_lavadora;
}

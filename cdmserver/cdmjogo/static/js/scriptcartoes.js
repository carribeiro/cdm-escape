const btn_reset_cartao_geladeira = document.querySelector('#btn-reset-cartao-geladeira')
const btn_reset_cartao_microondas = document.querySelector('#btn-reset-cartao-microondas')
const btn_reset_cartao_lavadora = document.querySelector('#btn-reset-cartao-lavadora')

btn_reset_cartao_geladeira.addEventListener('click', function(){ requestResetCartaoGeladeira(); }); 
btn_reset_cartao_microondas.addEventListener('click', function(){ requestResetCartaoMicroondas(); }); 
btn_reset_cartao_lavadora.addEventListener('click', function(){ requestResetCartaoLavadora(); }); 

// Chamada Ajax para atualizar status dos LEDs

function updateStatus(resposta) {
    // sensores de cartão geladeira, microondas e lavadora
    document.querySelector('#status-cartao-geladeira').className = (resposta.cartao_geladeira ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-cartao-microondas').className = (resposta.cartao_microondas ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-cartao-lavadora').className = (resposta.cartao_lavadora ? "dot dotVerde" : "dot dotCinza");
}

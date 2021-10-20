const btn_abrir_banheiro = document.querySelector('#btn-abrir-banheiro')
btn_abrir_banheiro.addEventListener('click', function(){ requestPulsoBanheiro('ABRIR'); }); 

const btn_fechar_banheiro = document.querySelector('#btn-fechar-banheiro')
btn_fechar_banheiro.addEventListener('click', function(){ requestPulsoBanheiro('FECHAR'); }); 

const btn_pulso_gaveta_banheiro = document.querySelector('#btn-pulso-gaveta-banheiro')
btn_pulso_gaveta_banheiro.addEventListener('click', function(){ requestPulsoGavetaBanheiro(); }); 

// Chamada Ajax para atualizar status dos LEDs

function updateStatus(resposta) {
    // sensores do banheiro
    document.querySelector('#status-ldr-pia').className = (resposta.ldr_pia ? "dot dotVerde" : "dot dotVermelho");
    document.querySelector('#status-ldr-chuveiro').className = (resposta.ldr_chuveiro ? "dot dotVerde" : "dot dotVermelho");
    document.querySelector('#status-seletor-verao').className = (resposta.seletor_verao ? "dot dotVerde" : "dot dotVermelho");
}

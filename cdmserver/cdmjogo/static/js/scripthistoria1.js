//console.log("ok");

var acertosReproduzidos = {
    "l45": false,
    "l6": false,
    "l7": false,
    "l8": false,
    "l9": false,
    "l1011": false,
    "l1213": false
};

const btnIniciarJogo = document.querySelector('#btn-iniciar-jogo');
const btnReiniciarJogo = document.querySelector('#btn-reiniciar-jogo');
const btnDesligarRaspberry = document.querySelector('#btn-desligar-raspberry');
const btnManual = document.querySelector('#btn-manual-acoes');
const btnManualLuzes = document.querySelector('#btn-manual-luzes');
const spanMsg = document.querySelector('#span-msg'); // Span Jogo: Parado, Jogando


const btnCompletarBarraLed = document.querySelector('#btn-completar-barra-led');
const btnAbrirGavetaCozinha = document.querySelector('#btn-abrir-gaveta-cozinha');
const btnAbrirGeladeira = document.querySelector('#btn-abrir-geladeira');
const btnAbrirPortaBanheiro = document.querySelector('#btn-abrir-porta-banheiro');
const btnAbrirGavetaBanheiro = document.querySelector('#btn-abrir-gaveta-banheiro');
const btnAbrirArmarioCozinha = document.querySelector('#btn-abrir-armario-cozinha');
const btnAbrirBau = document.querySelector('#btn-abrir-bau');
const btnAbrirGavetaAparador = document.querySelector('#btn-abrir-gaveta-aparador');
const btnReestabelecerEnergia = document.querySelector('#btn-reestabelecer-energia');


const btnLuzBaixaSala = document.querySelector('#btn-luz-baixa-sala');
const btnLuzBlackout23 = document.querySelector('#btn-luz-blackout-23');
const btnLuzBikeBateria = document.querySelector('#btn-luz-bike-bateria');
const btnLuzGavetaCozinha = document.querySelector('#btn-luz-gaveta-cozinha');
const btnLuzGeladeira  =  document.querySelector('#btn-luz-geladeira');
const btnLuzBanheiro  =  document.querySelector('#btn-luz-banheiro');
const btnLuzLavanderia  =  document.querySelector('#btn-luz-lavanderia');
const btnLuzArmarioCozinha  =  document.querySelector('#btn-luz-armario-cozinha');
const btnLuzBau  =  document.querySelector('#btn-luz-bau');
const btnLuzAparador = document.querySelector('#btn-luz-aparador');
const btnLuzReestabelecerEnergia  =  document.querySelector('#btn-luz-reestabelecer-energia');


const audioBanheiro = document.querySelector('#audio-banheiro');
const btnPlayAudioBanheiro = document.querySelector('#btn-audio-banheiro-play');
const btnStopAudioBanheiro = document.querySelector('#btn-audio-banheiro-stop');
const audioAcerto = document.querySelector('#audio-acerto');
const btnPlayAudioAcerto = document.querySelector('#btn-play-audio-acerto');

// ---- SUB ROTINAS ----

// Chamada Ajax para iniciar o jogo
function requestIniciarJogo() {
    var xhttp = new XMLHttpRequest();
    var url = "ajaxiniciarjogo";
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta);
            if(resposta.retorno == 'rodando')
            {
                //alert('Jogo Iniciado!');
                spanMsg.innerHTML = 'Jogo: Rodando'
            } else
            {
                console.log(resposta.retorno)
                spanMsg.innerHTML = 'Jogo: Erro ao iniciar'
            }
            
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

// Chamada Ajax para atualizar status das logicas (Concluidas ou não)
function requestStatusLogicas() {
    var xhttp = new XMLHttpRequest();
    var url = "ajaxstatus";
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            //console.log(resposta);

            if (resposta.logica1_status == true) {
                var dotlogica1 = document.querySelector('#status-logica1');
                dotlogica1.className = "dot dotVerde";
            }
            if (resposta.logica23_status == true){
                var dotlogica23 = document.querySelector('#status-logica23');
                dotlogica23.className = "dot dotVerde";
            }
            if (resposta.logica45_status == true){
                var dotlogica45 = document.querySelector('#status-logica45');
                dotlogica45.className = "dot dotVerde";
                reproduzirAcertoLogica(45);
            }
            if (resposta.logica6_status == true){
                var dotlogica6 = document.querySelector('#status-logica6');
                dotlogica6.className = "dot dotVerde";
                reproduzirAcertoLogica(6);
            }
            if (resposta.logica7_status == true){
                var dotlogica7 = document.querySelector('#status-logica7');
                dotlogica7.className = "dot dotVerde";
                reproduzirAcertoLogica(7);
            }
            if (resposta.logica8_status == true){
                var dotlogica8 = document.querySelector('#status-logica8');
                dotlogica8.className = "dot dotVerde";
                reproduzirAcertoLogica(8);
            }
            if (resposta.logica9_status == true){
                var dotlogica9 = document.querySelector('#status-logica9');
                dotlogica9.className = "dot dotVerde";
                reproduzirAcertoLogica(9);
            }
            if (resposta.logica1011_status == true){
                var dotlogica1011 = document.querySelector('#status-logica1011');
                dotlogica1011.className = "dot dotVerde";
                reproduzirAcertoLogica(1011);
            }
            if (resposta.logica1213_status == true){
                var dotlogica1213 = document.querySelector('#status-logica1213');
                dotlogica1213.className = "dot dotVerde";
            }

            //console.log([resposta.logica8_registrosFechados,resposta.logica7_status,resposta.logica8_status])

            // A reprodução do audio do banheiro esta sujeita a conclusão da logica anterior. E a atual nao esteje concluida
            if(resposta.logica8_registrosFechados == false && resposta.logica7_status == true && resposta.logica8_status == false){
                reproduzirSomBanheiro(true); // Reproduz o som de agua caindo
            } else {
                reproduzirSomBanheiro(false); // Para o som de agua caindo
            }

            setTimeout(requestStatusLogicas, 1000); // Uma nova atualizacao apos 1 segundo
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

// Chamada Ajax usada pelos botoes de acao
function requestAjaxHistoria1(acao){
    var xhttp = new XMLHttpRequest();
    var url = "ajaxhistoria1?acao=" + acao;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

// ---- ACOES ----

// Inicia a checagem de status das logicas
requestStatusLogicas()

// Acao ao clicar no botao iniciar jogo
btnIniciarJogo.addEventListener('click', function(){
    requestIniciarJogo();
    spanMsg.innerHTML = 'Jogo: Iniciando...'
});

btnReiniciarJogo.addEventListener('click', function(){
    requestAjaxHistoria1('reiniciar-jogo');
});

btnDesligarRaspberry.addEventListener('click', function(){
    requestAjaxHistoria1('desligar-raspberry');
});

btnManual.addEventListener('click', function(){
    requestAjaxHistoria1('manual');
});

btnManualLuzes.addEventListener('click', function(){
    requestAjaxHistoria1('manual-luzes');
});




btnCompletarBarraLed.addEventListener('click', function(){
    requestAjaxHistoria1('completar-barra-led');
});

btnAbrirGavetaCozinha.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-gaveta-cozinha');
});

btnAbrirGeladeira.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-geladeira');
});

btnAbrirPortaBanheiro.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-porta-banheiro');
});

btnAbrirGavetaBanheiro.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-gaveta-banheiro');
});

btnAbrirArmarioCozinha.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-armario-cozinha');
});

btnAbrirBau.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-bau');
});

btnAbrirGavetaAparador.addEventListener('click', function(){
    requestAjaxHistoria1('abrir-gaveta-aparador');
});

btnReestabelecerEnergia.addEventListener('click', function(){
    requestAjaxHistoria1('reestabelecer-energia');
});


// Iluminação

btnLuzBaixaSala.addEventListener('click', function(){
    requestAjaxHistoria1('luz-baixa-sala');
});

btnLuzBlackout23.addEventListener('click', function(){
    requestAjaxHistoria1('luz-blackout');
});

btnLuzBikeBateria.addEventListener('click', function(){
    requestAjaxHistoria1('luz-bike-bateria');
});
 
btnLuzGavetaCozinha.addEventListener('click', function(){
    requestAjaxHistoria1('luz-gaveta-cozinha');
});

btnLuzGeladeira.addEventListener('click', function(){
    requestAjaxHistoria1('luz-geladeira');
});

btnLuzBanheiro.addEventListener('click', function(){
    requestAjaxHistoria1('luz-banheiro');
});

btnLuzLavanderia.addEventListener('click', function(){
    requestAjaxHistoria1('luz-lavanderia');
});

btnLuzArmarioCozinha.addEventListener('click', function(){
    requestAjaxHistoria1('luz-armario-cozinha');
});

btnLuzBau.addEventListener('click', function(){
    requestAjaxHistoria1('luz-bau');
});

btnLuzAparador.addEventListener('click', function(){
    requestAjaxHistoria1('luz-aparador');
});

btnLuzReestabelecerEnergia.addEventListener('click', function(){
    requestAjaxHistoria1('luz-reestabelecer-energia');
});



// Sons

btnPlayAudioBanheiro.addEventListener('click', function(){
    audioBanheiro.play();
    console.log('Play Audio');
});


btnStopAudioBanheiro.addEventListener('click', function(){
    audioBanheiro.pause();
    console.log('Pause Audio');
});

btnPlayAudioAcerto.addEventListener('click', function(){
    audioAcerto.play();
    console.log('Play Acerto');
});

// -- Reproduzir Som Automaticamente --

function reproduzirAcertoLogica(nLogica){
    if (nLogica == 45 && acertosReproduzidos.l45 == false) {
        acertosReproduzidos.l45 = true;
        audioAcerto.play();
    }
    else if (nLogica == 6 && acertosReproduzidos.l6 == false) {
        acertosReproduzidos.l45 = true;
        acertosReproduzidos.l6 = true;
        audioAcerto.play();
    }
    else if (nLogica == 7 && acertosReproduzidos.l7 == false) {
        acertosReproduzidos.l45 = true;
        acertosReproduzidos.l6 = true;
        acertosReproduzidos.l7 = true;
        audioAcerto.play();
        audioBanheiro.play();
    }
    else if (nLogica == 8 && acertosReproduzidos.l8 == false) {
        acertosReproduzidos.l45 = true;
        acertosReproduzidos.l6 = true;
        acertosReproduzidos.l7 = true;
        acertosReproduzidos.l8 = true;
        audioBanheiro.pause();
        audioAcerto.play();
    }
    else if (nLogica == 9 && acertosReproduzidos.l9 == false) {
        acertosReproduzidos.l45 = true;
        acertosReproduzidos.l6 = true;
        acertosReproduzidos.l7 = true;
        acertosReproduzidos.l8 = true;
        acertosReproduzidos.l9 = true;
        audioBanheiro.pause();
        audioAcerto.play();
    }
    else if (nLogica == 1011 && acertosReproduzidos.l1011 == false) {
        // Se esta logica foi concluida, obrigatoriamente as anteriores tambem foram
        acertosReproduzidos.l45 = true;
        acertosReproduzidos.l6 = true;
        acertosReproduzidos.l7 = true;
        acertosReproduzidos.l8 = true;
        acertosReproduzidos.l9 = true;
        acertosReproduzidos.l1011 = true;
        audioBanheiro.pause();
        audioAcerto.play();
    }
}

// Esta função reproduz ou pausa o som de registro aberto(Agua caindo)
function reproduzirSomBanheiro(reproduzir){
    // A reprodução do som exige que o som de acerto da 
    // logica l7 já tenha sido reproduzido e que o som de acerto 
    // da logica l8 não tenha sido reproduzido ainda.
    if (reproduzir == true && acertosReproduzidos.l7 == true && acertosReproduzidos.l8 == false) {
        audioBanheiro.play();
    } else {
        audioBanheiro.pause();
    }
}

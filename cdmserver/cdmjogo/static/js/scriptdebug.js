//console.log("ok");


// const spanMsg = document.querySelector('#span-msg'); // Span Jogo: Parado, Jogando

const btn_set_leds = document.querySelector('#btn-set-leds')
btn_set_leds.addEventListener('click', function(){
    requestSetLeds();
});

const btn_reset_leds = document.querySelector('#btn-reset-leds')
btn_reset_leds.addEventListener('click', function(){
    requestResetLeds();
});

const btn_refresh_status = document.querySelector('#btn-refresh-status')
btn_refresh_status.addEventListener('click', function(){
    requestStatus();
});


const btn_led_37_hi = document.querySelector('#btn-led-37-hi')
const btn_led_37_lo = document.querySelector('#btn-led-37-lo')
const btn_led_35_hi = document.querySelector('#btn-led-35-hi')
const btn_led_35_lo = document.querySelector('#btn-led-35-lo')
const btn_led_21_hi = document.querySelector('#btn-led-21-hi')
const btn_led_21_lo = document.querySelector('#btn-led-21-lo')
const btn_led_23_hi = document.querySelector('#btn-led-23-hi')
const btn_led_23_lo = document.querySelector('#btn-led-23-lo')
const btn_led_29_hi = document.querySelector('#btn-led-29-hi')
const btn_led_29_lo = document.querySelector('#btn-led-29-lo')
const btn_led_24_hi = document.querySelector('#btn-led-24-hi')
const btn_led_24_lo = document.querySelector('#btn-led-24-lo')
const btn_led_15_hi = document.querySelector('#btn-led-15-hi')
const btn_led_15_lo = document.querySelector('#btn-led-15-lo')
const btn_led_19_hi = document.querySelector('#btn-led-19-hi')
const btn_led_19_lo = document.querySelector('#btn-led-19-lo')
const btn_led_12_hi = document.querySelector('#btn-led-12-hi')
const btn_led_12_lo = document.querySelector('#btn-led-12-lo')
const btn_led_10_hi = document.querySelector('#btn-led-10-hi')
const btn_led_10_lo = document.querySelector('#btn-led-10-lo')
const btn_led_18_hi = document.querySelector('#btn-led-18-hi')
const btn_led_18_lo = document.querySelector('#btn-led-18-lo')
const btn_led_16_hi = document.querySelector('#btn-led-16-hi')
const btn_led_16_lo = document.querySelector('#btn-led-16-lo')
const btn_led_38_hi = document.querySelector('#btn-led-38-hi')
const btn_led_38_lo = document.querySelector('#btn-led-38-lo')
const btn_led_40_hi = document.querySelector('#btn-led-40-hi')
const btn_led_40_lo = document.querySelector('#btn-led-40-lo')

btn_led_37_hi.addEventListener('click', function(){ requestSetLedHi(37); }); 
btn_led_37_lo.addEventListener('click', function(){ requestSetLedLo(37); });
btn_led_35_hi.addEventListener('click', function(){ requestSetLedHi(35); }); 
btn_led_35_lo.addEventListener('click', function(){ requestSetLedLo(35); });
btn_led_21_hi.addEventListener('click', function(){ requestSetLedHi(21); }); 
btn_led_21_lo.addEventListener('click', function(){ requestSetLedLo(21); });
btn_led_23_hi.addEventListener('click', function(){ requestSetLedHi(23); }); 
btn_led_23_lo.addEventListener('click', function(){ requestSetLedLo(23); });
btn_led_29_hi.addEventListener('click', function(){ requestSetLedHi(29); }); 
btn_led_29_lo.addEventListener('click', function(){ requestSetLedLo(29); });
btn_led_24_hi.addEventListener('click', function(){ requestSetLedHi(24); }); 
btn_led_24_lo.addEventListener('click', function(){ requestSetLedLo(24); });
btn_led_15_hi.addEventListener('click', function(){ requestSetLedHi(15); }); 
btn_led_15_lo.addEventListener('click', function(){ requestSetLedLo(15); });
btn_led_19_hi.addEventListener('click', function(){ requestSetLedHi(19); }); 
btn_led_19_lo.addEventListener('click', function(){ requestSetLedLo(19); });
btn_led_12_hi.addEventListener('click', function(){ requestSetLedHi(12); }); 
btn_led_12_lo.addEventListener('click', function(){ requestSetLedLo(12); });
btn_led_10_hi.addEventListener('click', function(){ requestSetLedHi(10); }); 
btn_led_10_lo.addEventListener('click', function(){ requestSetLedLo(10); });
btn_led_18_hi.addEventListener('click', function(){ requestSetLedHi(18); }); 
btn_led_18_lo.addEventListener('click', function(){ requestSetLedLo(18); });
btn_led_16_hi.addEventListener('click', function(){ requestSetLedHi(16); }); 
btn_led_16_lo.addEventListener('click', function(){ requestSetLedLo(16); });
btn_led_38_hi.addEventListener('click', function(){ requestSetLedHi(38); }); 
btn_led_38_lo.addEventListener('click', function(){ requestSetLedLo(38); });
btn_led_40_hi.addEventListener('click', function(){ requestSetLedHi(40); }); 
btn_led_40_lo.addEventListener('click', function(){ requestSetLedLo(40); });

const btn_abrir_banheiro = document.querySelector('#btn-trava-banheiro')
btn_abrir_banheiro.addEventListener('click', function(){ requestPulsoBanheiro('ABRIR'); }); 

const btn_fechar_banheiro = document.querySelector('#btn-trava-banheiro')
btn_fechar_banheiro.addEventListener('click', function(){ requestPulsoBanheiro('FECHAR'); }); 

const btn_spot_blackout = document.querySelector('#btn-spot-blackout')
const btn_spot_bike = document.querySelector('#btn-spot-bike')
const btn_spot_gaveta_cozinha = document.querySelector('#btn-spot-gaveta-cozinha')
const btn_spot_geladeira = document.querySelector('#btn-spot-geladeira')
const btn_spot_banheiro = document.querySelector('#btn-spot-banheiro')
const btn_spot_lavanderia = document.querySelector('#btn-spot-lavanderia')
const btn_spot_armario = document.querySelector('#btn-spot-armario')
const btn_spot_bau = document.querySelector('#btn-spot-bau')
const btn_spot_aparador = document.querySelector('#btn-spot-aparador')
const btn_spot_acendimento_gradual = document.querySelector('#btn-spot-acendimento-gradual')

btn_spot_blackout.addEventListener('click', function(){ requestSetSpot('0b1101'); }); 
btn_spot_bike.addEventListener('click', function(){ requestSetSpot('0b0010'); }); 
btn_spot_gaveta_cozinha.addEventListener('click', function(){ requestSetSpot('0b0011'); }); 
btn_spot_geladeira.addEventListener('click', function(){ requestSetSpot('0b0100'); }); 
btn_spot_banheiro.addEventListener('click', function(){ requestSetSpot('0b0101'); }); 
btn_spot_lavanderia.addEventListener('click', function(){ requestSetSpot('0b0110'); }); 
btn_spot_armario.addEventListener('click', function(){ requestSetSpot('0b0111'); }); 
btn_spot_bau.addEventListener('click', function(){ requestSetSpot('0b1000'); }); 
btn_spot_aparador.addEventListener('click', function(){ requestSetSpot('0b1001'); }); 
btn_spot_acendimento_gradual.addEventListener('click', function(){ requestSetSpot('0b1100'); }); 

const btn_bateria_bike_0 = document.querySelector('#btn-bateria-bike-0')
const btn_bateria_bike_1 = document.querySelector('#btn-bateria-bike-1')
const btn_bateria_bike_2 = document.querySelector('#btn-bateria-bike-2')
const btn_bateria_bike_3 = document.querySelector('#btn-bateria-bike-3')
const btn_bateria_bike_4 = document.querySelector('#btn-bateria-bike-4')

btn_bateria_bike_0.addEventListener('click', function(){ requestSetBateria(0); }); 
btn_bateria_bike_1.addEventListener('click', function(){ requestSetBateria(1); }); 
btn_bateria_bike_2.addEventListener('click', function(){ requestSetBateria(2); }); 
btn_bateria_bike_3.addEventListener('click', function(){ requestSetBateria(3); }); 
btn_bateria_bike_4.addEventListener('click', function(){ requestSetBateria(4); }); 

const btn_reset_cartao_geladeira = document.querySelector('#btn-reset-cartao-geladeira')
const btn_reset_cartao_microondas = document.querySelector('#btn-reset-cartao-microondas')
const btn_reset_cartao_lavadora = document.querySelector('#btn-reset-cartao-lavadora')

btn_reset_cartao_geladeira.addEventListener('click', function(){ requestResetCartaoGeladeira(); }); 
btn_reset_cartao_microondas.addEventListener('click', function(){ requestResetCartaoMicroondas(); }); 
btn_reset_cartao_lavadora.addEventListener('click', function(){ requestResetCartaoLavadora(); }); 

// Chamada Ajax para atualizar status dos LEDs

function updateStatus(resposta) {
    // Sequência de LEDs: 37 35 21 23 29 24 15 19 12 10 18 16 38 40            
    document.querySelector('#status-led-37').className = (resposta.leds['37'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-35').className = (resposta.leds['35'] ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-led-21').className = (resposta.leds['21'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-23').className = (resposta.leds['23'] ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-led-29').className = (resposta.leds['29'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-24').className = (resposta.leds['24'] ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-led-15').className = (resposta.leds['15'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-19').className = (resposta.leds['19'] ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-led-12').className = (resposta.leds['12'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-10').className = (resposta.leds['10'] ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-led-18').className = (resposta.leds['18'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-16').className = (resposta.leds['16'] ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-led-38').className = (resposta.leds['38'] ? "dot dotVermelho" : "dot dotCinza");
    document.querySelector('#status-led-40').className = (resposta.leds['40'] ? "dot dotVerde" : "dot dotCinza");

    // reed bicicleta
    document.querySelector('#status-reed-bicicleta').className = (resposta.bicicleta ? "dot dotVerde" : "dot dotCinza");

    // sensores de cartão geladeira, microondas e lavadora
    document.querySelector('#status-cartao-geladeira').className = (resposta.cartao_geladeira ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-cartao-microondas').className = (resposta.cartao_microondas ? "dot dotVerde" : "dot dotCinza");
    document.querySelector('#status-cartao-lavadora').className = (resposta.cartao_lavadora ? "dot dotVerde" : "dot dotCinza");
}

function requestStatus() {
    var xhttp = new XMLHttpRequest();
    var url = "ajaxdebugstatus";
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            //console.log(resposta);
            updateStatus(resposta);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestResetLeds(){
    var xhttp = new XMLHttpRequest();
    var url = "resetleds";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestSetLeds(){
    var xhttp = new XMLHttpRequest();
    var url = "setleds";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestSetLedHi(led){
    var xhttp = new XMLHttpRequest();
    var url = "setledhi?led=" + led;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestSetLedLo(led){
    var xhttp = new XMLHttpRequest();
    var url = "setledlo?led=" + led;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestSetSpot(spotCode){
    var xhttp = new XMLHttpRequest();
    var url = "setspotcode?spot_code=" + spotCode;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestSetBateria(nivel){
    var xhttp = new XMLHttpRequest();
    var url = "setbateria?nivel=" + nivel;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestResetCartaoGeladeira() {
    var xhttp = new XMLHttpRequest();
    var url = "resetcartaogeladeira";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestResetCartaoMicroondas() {
    var xhttp = new XMLHttpRequest();
    var url = "resetcartaomicroondas";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()
}

function requestResetCartaoLavadora() {
    var xhttp = new XMLHttpRequest();
    var url = "resetcartaolavadora";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoBanheiro(operacao) {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_banheiro?" + operacao;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}
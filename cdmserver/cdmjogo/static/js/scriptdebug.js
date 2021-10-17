//console.log("ok");


// const spanMsg = document.querySelector('#span-msg'); // Span Jogo: Parado, Jogando

const btn_reset_leds = document.querySelector('#btn-reset-leds')

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

btn_reset_leds.addEventListener('click', function(){
    requestResetLeds();
});

btn_led_37_hi.addEventListener('click', function(){
    requestSetLedHi(37);
});

btn_led_37_lo.addEventListener('click', function(){
    requestSetLedLo(37);
});

// Chamada Ajax para atualizar status dos LEDs

function requestStatusLeds() {
    var xhttp = new XMLHttpRequest();
    var url = "ajaxdebugstatus";
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            //console.log(resposta);

            // Sequência de LEDs: 37 35 21 23 29 24 15 19 12 10 18 16 38 40            
            document.querySelector('#status-led-37').className = (resposta.leds[37] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-35').className = (resposta.leds[35] ? "dot dotVerde" : "dot dotCinza");
            document.querySelector('#status-led-21').className = (resposta.leds[21] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-23').className = (resposta.leds[23] ? "dot dotVerde" : "dot dotCinza");
            document.querySelector('#status-led-29').className = (resposta.leds[29] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-24').className = (resposta.leds[24] ? "dot dotVerde" : "dot dotCinza");
            document.querySelector('#status-led-15').className = (resposta.leds[15] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-19').className = (resposta.leds[19] ? "dot dotVerde" : "dot dotCinza");
            document.querySelector('#status-led-12').className = (resposta.leds[12] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-10').className = (resposta.leds[10] ? "dot dotVerde" : "dot dotCinza");
            document.querySelector('#status-led-18').className = (resposta.leds[18] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-16').className = (resposta.leds[16] ? "dot dotVerde" : "dot dotCinza");
            document.querySelector('#status-led-38').className = (resposta.leds[38] ? "dot dotVermelho" : "dot dotCinza");
            document.querySelector('#status-led-40').className = (resposta.leds[40] ? "dot dotVerde" : "dot dotCinza");
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

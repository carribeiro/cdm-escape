//console.log("ok");


// const spanMsg = document.querySelector('#span-msg'); // Span Jogo: Parado, Jogando

const btn_reset_leds = document.querySelector('#btn-reset-leds')

const btn_led_37_hi = document.querySelector('#btn-led-37-hi')
const btn_led_37_lo = document.querySelector('#btn-led-37-lo')
const btn_led_35_hi = document.querySelector('#btn-led-37-hi')
const btn_led_35_lo = document.querySelector('#btn-led-37-lo')
const btn_led_21_hi = document.querySelector('#btn-led-37-hi')
const btn_led_21_lo = document.querySelector('#btn-led-37-lo')
const btn_led_23_hi = document.querySelector('#btn-led-37-hi')
const btn_led_23_lo = document.querySelector('#btn-led-37-lo')
const btn_led_29_hi = document.querySelector('#btn-led-37-hi')
const btn_led_29_lo = document.querySelector('#btn-led-37-lo')
const btn_led_24_hi = document.querySelector('#btn-led-37-hi')
const btn_led_24_lo = document.querySelector('#btn-led-37-lo')
const btn_led_15_hi = document.querySelector('#btn-led-37-hi')
const btn_led_15_lo = document.querySelector('#btn-led-37-lo')
const btn_led_19_hi = document.querySelector('#btn-led-37-hi')
const btn_led_19_lo = document.querySelector('#btn-led-37-lo')
const btn_led_12_hi = document.querySelector('#btn-led-37-hi')
const btn_led_12_lo = document.querySelector('#btn-led-37-lo')
const btn_led_10_hi = document.querySelector('#btn-led-37-hi')
const btn_led_10_lo = document.querySelector('#btn-led-37-lo')
const btn_led_18_hi = document.querySelector('#btn-led-37-hi')
const btn_led_18_lo = document.querySelector('#btn-led-37-lo')
const btn_led_16_hi = document.querySelector('#btn-led-37-hi')
const btn_led_16_lo = document.querySelector('#btn-led-37-lo')
const btn_led_38_hi = document.querySelector('#btn-led-37-hi')
const btn_led_38_lo = document.querySelector('#btn-led-37-lo')
const btn_led_40_hi = document.querySelector('#btn-led-37-hi')
const btn_led_40_lo = document.querySelector('#btn-led-37-lo')

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
    var url = "ajaxstatus";
    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            //console.log(resposta);

            // 37 35 21 23 29 24 15 19 12 10 18 16 38 40            
            var status_led_37 = document.querySelector('#status-led-37');
            if (resposta.leds[37] == true) {
                dotlogica1.className = "dot dotVermelho";
            } else {
                dotlogica1.className = "dot dotCinza"
            }

            var status_led_39 = document.querySelector('#status-led-39');
            if (resposta.leds[39] == true) {
                dotlogica1.className = "dot dotVerde";
            } else {}
                dotlogica1.className = "dot dotCinza"
            }

            var status_led_21 = document.querySelector('#status-led-39');
            if (resposta.leds[21] == true) {
                dotlogica1.className = "dot dotVermelho";
            } else {
                dotlogica1.className = "dot dotCinza"
            }

            var status_led_23 = document.querySelector('#status-led-39');
            if (resposta.leds[23] == true) {
                dotlogica1.className = "dot dotVerde";
            } else {}
                dotlogica1.className = "dot dotCinza"
            }

        }
    }
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

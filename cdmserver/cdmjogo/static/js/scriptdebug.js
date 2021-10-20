/* MÉTODOS AJAX DE DEBUG (TODAS AS PÁGINAS) */
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
    var url = "pulso_abrir_banheiro?operacao=" + operacao;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoGeladeira(operacao) {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_geladeira?operacao=" + operacao;

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoGavetaBanheiro() {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_gaveta_banheiro";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoGavetaArmario() {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_gaveta_armario";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoPortaArmario() {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_porta_armario";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoGavetaAparador() {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_gaveta_aparador";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

function requestPulsoBau() {
    var xhttp = new XMLHttpRequest();
    var url = "pulso_abrir_bau";

    xhttp.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            var resposta = JSON.parse(this.responseText);

            console.log(resposta.retorno);
        }
    }
    xhttp.open("GET",url,true);
    xhttp.send()

}

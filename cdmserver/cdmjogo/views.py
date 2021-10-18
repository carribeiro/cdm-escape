## VIEWS.PY

import os # Modulo para comandos shell linux
import time
from django.shortcuts import render
#from django.http import HttpResponse
from django.http import JsonResponse
from cdmjogo.classes.logica_1 import Logica_1
from cdmjogo.classes.logica_23 import Logica_23
from cdmjogo.classes.logica_45 import Logica_45
from cdmjogo.classes.logica_6 import Logica_6
from cdmjogo.classes.logica_7 import Logica_7
from cdmjogo.classes.logica_8 import Logica_8
from cdmjogo.classes.logica_9 import Logica_9
from cdmjogo.classes.logica_1011 import Logica_1011
from cdmjogo.classes.logica_1213 import Logica_1213
from cdmjogo.classes.mcp23017 import MCP23017 as mcp

# View para retornar a pagina index.html para o cliente
def index(request):
    return render(request, 'index/index.html', {})

# View para retornar a pagina historia1.html para o cliente
def historia1(request):
    return render(request, 'historia1/historia1.html', {})

# View para retornar a pagina historia2.html para o cliente
def historia2(request):
    return render(request, 'historia2/historia2.html', {})

# ---------------- AJAX ---------------------
# Views para chamadas em segundo plano AJAX

# View para retorna um objeto Json com dados auxiliares a historia1.html
def ajaxhistoria1(request):
    
    if request.method == 'GET':
        acao = request.GET.get('acao', None)

        #print(request.GET)

        if acao != None:
            if acao == 'luz-baixa-sala': # Iluminação
                Logica_1.luzBaixaSala()

            elif acao == 'luz-blackout': # Iluminação
                Logica_23.blackout()
                
            elif acao == 'luz-bike-bateria': # Iluminação
                Logica_23.acenderSpotBikeBateria()
            
            elif acao == 'completar-barra-led':
                Logica_45.efeitoCarregandoFinal()

            elif acao == 'abrir-gaveta-cozinha':
                Logica_45.abrirGaveta()

            elif acao == 'luz-gaveta-cozinha': # Iluminação
                Logica_45.acenderSpotGavetaCozinha()

            elif acao == 'abrir-geladeira':
                Logica_6.abrirGeladeira()

            elif acao == 'luz-geladeira': # Iluminação
                Logica_6.acenderSpotGeladeira()

            elif acao == 'abrir-porta-banheiro':
                Logica_7.abrirPortaBanheiro()

            elif acao == 'luz-banheiro': # Iluminação
                Logica_7.acenderSpotsBanheiro()

            elif acao == 'abrir-gaveta-banheiro':
                Logica_8.abrirGavetaBanheiro()

            elif acao == 'luz-lavanderia': # Iluminação
                Logica_8.acenderSpotLavanderia()

            elif acao == 'abrir-armario-cozinha':
                Logica_9.abrirArmario()

            elif acao == 'luz-armario-cozinha':  # Iluminação
                Logica_9.acenderSpotArmario()

            elif acao == 'abrir-bau':
                Logica_1011.abrirBau()

            elif acao == 'luz-bau': # Iluminação
                Logica_1011.acenderSpotBau()

            elif acao == 'abrir-gaveta-aparador':
                Logica_1213.abrirGavetaAparador()

            elif acao == 'reestabelecer-energia':
                Logica_1213.reestabelecerEnergia()

            elif acao == 'luz-aparador': # Iluminação
                Logica_1213.rotinaBlackout()

            elif acao == 'luz-reestabelecer-energia': # Iluminação
                Logica_1213.acenderTodasLuzes()
            
            elif acao == 'reiniciar-jogo':
                mcp.confRegistradoresLuzes() # GPA como output
                mcp.escreverBinarioLuzes(0b1110) # Codigo de reles desativados
                os.system('sudo fuser -k 8000/tcp && sleep 4 && . /home/pi/cdmescape/escapeiniciar.sh')

            elif acao == 'desligar-raspberry':
                os.system('sudo shutdown -h now')

            elif acao == 'manual':
                mcp.confRegistradores()
            
            elif acao == 'manual-luzes':
                mcp.confRegistradoresLuzes() # GPA como output
                mcp.escreverBinarioLuzes(0b0000) # Codigo de reles desativados
            
            
    dicionario_json = {
        'retorno': 'ajax historia 1, OK!'
    }

    return JsonResponse(dicionario_json)

# View para retorna um objeto Json com dados auxiliares a historia2.html
def ajaxhistoria2(request):
    dicionario_json = {
        'retorno': 'ajax historia 2, OK!'
    }

    return JsonResponse(dicionario_json)

def ajaxiniciarjogo(request):
    print('Iniciando Jogo...')

    mcp.confRegistradores()
    mcp.confRegistradoresLuzes() # GPA como output
    mcp.escreverBinarioLuzes(0b1110) # Codigo de reles desativados
    time.sleep(0.5)

    Logica_1.iniciarThread()


    msgRetorno = 'rodando'
    dicionario_json = {
        'retorno': msgRetorno,
    }

    return JsonResponse(dicionario_json)

def ajaxstatus(request):

    dicionario_json = {
        'logica1_status': Logica_1._concluida,
        'logica23_status': Logica_23._concluida,
        'logica45_status': Logica_45._concluida,
        'logica6_status': Logica_6._concluida,
        'logica7_status': Logica_7._concluida,
        'logica8_status': Logica_8._concluida,
        'logica9_status': Logica_9._concluida,
        'logica1011_status': Logica_1011._concluida,
        'logica1213_status': Logica_1213._concluida,
        'logica8_registrosFechados': Logica_8.registrosFechados,
    }

    return JsonResponse(dicionario_json)


# ------------- FIM AJAX ------------------

# View para DEBUG do projeto
def desenvolvimento(request):
    return render(request, 'desenvolvimento/desenvolvimento.html', {})

def ajaxdesenvolvimento(request):
    dicionario_json = {
        'retorno': 'ajax desenvolvimento, OK!'
    }

    return JsonResponse(dicionario_json)

import RPi.GPIO as GPIO # Modulo de controle GPIO
from cdmjogo.classes.mcp23017 import MCP23017 as mcp

# LEDs: 37 35 21 23 29 24 15 19 12 10 18 16 38 40   

lista_leds = [37, 35, 21, 23, 29, 24, 15, 19, 12, 10, 18, 16, 38, 40]

status_leds = {
    '37': False, # Divisoria Vermelho (37)
    '35': False, # Divisoria Verde (35)
    '21': False, # Gaveta Inferior Vermelho (21)
    '23': False, # Gaveta Inferior Verde (23)
    '29': False, # Acima Microondas Vermelho (29)
    '24': False, # Acima Microondas Verde (24)
    '15': False, # Pia Vermelho (15)
    '19': False, # Pia Verde = (19)
    '12': False, # Aparador Vermelho (12)
    '10': False, # Aparador Verde (10)
    '18': False, # Baú Vermelho (18)
    '16': False, # Baú Verde (16)
    '38': False, # Geladeira Vermelho (38)
    '40': False, # Geladeira Verde (40)
}

def read_status_reed_bicicleta():
    gp_reedSwitchBicicleta = 0 # GPB0 (MCP23017)
    mcp.setup(gp_reedSwitchBicicleta, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Reed Switch bicicleta
    return mcp.input(gp_reedSwitchBicicleta, mcp.GPB, mcp.ADDRESS1)    

def read_status_cartoes():
    # lê os três cartões RFID; cada um possui uma leitura com um arduíno interno que comunica por 
    # um único pino com o Raspberry Pi, indicando que tem o cartão certo ou não.

    gpio_etiquetaGeladeira = 36 # sinal GPIO 36 Raspberry
    gpio_etiquetaMicroondas = 33 # sinal GPIO 33 Raspberry
    gp_etiquetaMaquina = 4 # sinal GPB4 da expansão MCP23017

    GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
    GPIO.setwarnings(False) # Desativa avisos
    GPIO.setup(gpio_etiquetaGeladeira, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
    GPIO.setup(gpio_etiquetaMicroondas, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
    mcp.setup(gp_etiquetaMaquina, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Etiqueta maquina

    cartao_geladeira = GPIO.input(cls.gpio_etiquetaGeladeira)
    cartao_microondas = GPIO.input(cls.gpio_etiquetaMicroondas)
    cartao_lavadora = mcp.input(cls.gp_etiquetaMaquina, mcp.GPB, mcp. ADDRESS1)

    return cartao_geladeira, cartao_microondas, cartao_lavadora

def ajaxdebugstatus(request):
    cartao_geladeira, cartao_microondas, cartao_lavadora = read_status_cartoes()
    dicionario_json = { 
        'leds': status_leds, 
        'bicicleta': read_status_reed_bicicleta(), 
        'cartao_geladeira': cartao_geladeira,
        'cartao_microondas': cartao_microondas,
        'cartao_lavadora': cartao_lavadora,
    }
    return JsonResponse(dicionario_json)

def resetleds(request):
    if request.method == 'GET':
        # Configura as GPIOs como BOARD, Contagem de 0 a 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for led in lista_leds:
            status_leds[str(led)] = False
            GPIO.setup(led, GPIO.OUT)
            GPIO.output(led, GPIO.LOW)            

    dicionario_json = {
        'retorno': 'resetleds, OK!'
    }

    return JsonResponse(dicionario_json)

def setledhi(request):
    dicionario_json = {        'retorno': 'setledhi = FAIL!'
    }
    if request.method == 'GET':
        led = request.GET.get('led', None)

        if led in status_leds:
            # Configura as GPIOs como BOARD, Contagem de 0 a 40
            led_num = int(led)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(led_num, GPIO.OUT)
            GPIO.output(led_num, not(GPIO.HIGH) # atenção, saída invertida; HIGH apaga, LOW acende (veja o 'not()')
            status_leds[led] = True

            dicionario_json = {
                'retorno': 'setledhi = PASSED!'
            }

    return JsonResponse(dicionario_json)

def setledlo(request):
    dicionario_json = {
        'retorno': 'setledlo = FAIL!'
    }
    if request.method == 'GET':
        led = request.GET.get('led', None)

        if led in status_leds:
            # Configura as GPIOs como BOARD, Contagem de 0 a 40
            led_num = int(led)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(led_num, GPIO.OUT)
            GPIO.output(led_num, not(GPIO.LOW) # atenção, saída invertida; HIGH apaga, LOW acende (veja o 'not()')
            status_leds[led] = False

            dicionario_json = {
                'retorno': 'setledlo = PASSED!'
            }

    return JsonResponse(dicionario_json)

spot_codes = {
    '0b1101': 0b1101, # blackout
    '0b0010': 0b0010, # sppot bike
    '0b0011': 0b0011, # spot gaveta gozinha
    '0b0100': 0b0100, # spot geladeira
}

def setspotcode(request):
    dicionario_json = {
        'retorno': 'setspotcode = FAIL!'
    }
    if request.method == 'GET':
        spot_code = request.GET.get('spot_code', None)

        if spot_code in spot_codes:
            mcp.escreverBinarioLuzes(spot_codes[spot_code])
            dicionario_json = {
                'retorno': 'setspotcode = PASSED!'
            }

    return JsonResponse(dicionario_json)

def setbateria(request):
    dicionario_json = {
        'retorno': 'setbateria = FAIL!'
    }
    if request.method == 'GET':
        nivel = request.GET.get('nivel', None)

        if nivel in ['0','1','2','3','4']]:
            gp_barraLed = [2,3,4,5] # GPA5, GPA4, GPA3, GPA2 (MCP23017)
            nivel_leds = {
                '0': [mcp.HIGH, mcp.HIGH, mcp.HIGH, mcp.HIGH], 
                '1': [mcp.LOW,  mcp.HIGH, mcp.HIGH, mcp.HIGH], 
                '2': [mcp.LOW,  mcp.LOW,  mcp.HIGH, mcp.HIGH], 
                '3': [mcp.LOW,  mcp.LOW,  mcp.LOW,  mcp.HIGH], 
                '4': [mcp.LOW,  mcp.LOW,  mcp.LOW,  mcp.LOW], 
            }

            mcp.setup(gp_barraLed[0], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
            mcp.setup(gp_barraLed[1], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
            mcp.setup(gp_barraLed[2], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
            mcp.setup(gp_barraLed[3], mcp.GPA, mcp.OUT, mcp.ADDRESS2)

            mcp.output(gp_barraLed[0], mcp.GPA, nivel_bateria[nivel], mcp.ADDRESS2)
            mcp.output(gp_barraLed[1], mcp.GPA, nivel_bateria[nivel], mcp.ADDRESS2)
            mcp.output(gp_barraLed[2], mcp.GPA, nivel_bateria[nivel], mcp.ADDRESS2)
            mcp.output(gp_barraLed[3], mcp.GPA, nivel_bateria[nivel], mcp.ADDRESS2)

            dicionario_json = {
                'retorno': 'setbateria = PASSED!'
            }

    return JsonResponse(dicionario_json)

def pulso_abrir_gaveta():

    # trava da gaveta do armário é o sinal 4 da GPB (MCP23017)
    gp_travaGaveta = 4 #GPB4 (MCP23017)

    # Garantir que o pino esta como OUTPUT
    mcp.setup(gp_travaGaveta , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
    
    # Pulsa nível LOW para abrir a gaveta, espera 1 segundo, retorna para nível HIGH
    # TODO: este tempo de 1s não é ideal de ocorrer no meio de um request HTTP, deveria ser movido para uma thread separada
    mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
    time.sleep(1)
    mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

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
import os # Modulo para comandos shell linux
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
import time

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


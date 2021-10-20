from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_9 import Logica_9

""" CLASSE das LOGICAs 8
Esta classe faz todo o controle dos itens relacionados a Logica 8

8 -> Dentro do banheiro, os jogadores terão os seguintes desafios:
      i. Fechar registro da torneira
     ii. Fechar registro do chuveiro
    iii. Colocar chuveiro em modo verão

b. Na torneira da pia, deverá ter um LED azul que indicará a torneira aberta, ao
fechar, o LED apagará.

c. Na parede, deverá ter informações e textos que indique o tempo de banho do
menino (plotado) e frases sobre consumo de água.

d. Enquanto o chuveiro estiver ligado e a torneira aberta, deverá ter um som de
chuveiro ligado e água sendo desperdiçada.

e. Resolvendo os desafios do banheiro, deverá abrir uma gaveta ou armario (definir)
"""

class Logica_8(Logica_geral):
    
    # GPIO's
    gpio_registroTorneira = 13 # Pino para leitura do estado do registro (rasperry)
    gpio_registroChuveiro = 7 # Pino do estado do registro chuveiro (rasperry)
    gpio_veraoChuveiro = 11 # Pino para leitura do estado do verão do chuveiro (rasperry)
    ledPiaVermelho = 15
    ledPiaVerde = 19

    # Relés
    gp_travaGaveta = 2 # GPB2 (MCP23017 0x24)
    gp_fitaLedPia = 1 # GPB1 (MCP23017 0x24)
    gp_fitaLedChuveiro = 1 # GPA1 (MCP23017 0x24)
    gp_ledVermelhoChuveiro = 0 # GPB0 (MCP23017 0x24)

    # Variavel de sincronismo do som de registro aberto(Agua caindo)
    registrosFechados = False # Inicialmente False

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradoresBanheiroAberto()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos

        GPIO.setup(cls.gpio_registroTorneira, GPIO.IN) # Pino como PULL-DOWN interno
        GPIO.setup(cls.gpio_registroChuveiro, GPIO.IN) # Pino como PULL-DOWN interno
        GPIO.setup(cls.gpio_veraoChuveiro, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno

        GPIO.setup(cls.ledPiaVermelho, GPIO.OUT)
        GPIO.setup(cls.ledPiaVerde, GPIO.OUT)
        

        # Configurando GPIO's do Extensor 0x24
        mcp.setup(cls.gp_travaGaveta, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_fitaLedPia, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_fitaLedChuveiro, mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_ledVermelhoChuveiro, mcp.GPB, mcp.OUT, mcp.ADDRESS2)

        # Inicialmente somente led vermelho acesso
        GPIO.output(cls.ledPiaVermelho, not(GPIO.HIGH))
        GPIO.output(cls.ledPiaVerde, not(GPIO.LOW))
        

        # Inicialmente em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)
        # Leds Acessos
        mcp.output(cls.gp_fitaLedPia, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_fitaLedChuveiro, mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_ledVermelhoChuveiro, mcp.GPB, mcp.LOW, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b0101) # Codigo do Spot do banheiro

    # Metodo para destravar a gaveta do banheiro
    @classmethod
    def abrirGavetaBanheiro(cls):
        
        # Marca a logica como concluida
        cls._concluida = True

        # Garantir que o pino esta como OUTPUT
        mcp.setup(cls.gp_travaGaveta , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        # Em nivel Baixo acionando o Rele
        mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
        time.sleep(1)
        # Em nivel Alto desacionando o Rele
        mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)
        
        # Garantir que estao como output
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        GPIO.setup(cls.ledPiaVermelho, GPIO.OUT)
        GPIO.setup(cls.ledPiaVerde, GPIO.OUT)
        # Led verde Acesso
        GPIO.output(cls.ledPiaVermelho, not(GPIO.LOW))
        GPIO.output(cls.ledPiaVerde, not(GPIO.HIGH))

    @classmethod
    def apagarFitaLedTorneira(cls):
        mcp.setup(cls.gp_fitaLedPia, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_fitaLedPia, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

    @classmethod
    def acenderFitaLedTorneira(cls):
        mcp.setup(cls.gp_fitaLedPia, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_fitaLedPia, mcp.GPB, mcp.LOW, mcp.ADDRESS2)

    @classmethod
    def apagarFitaLedChuveiro(cls):
        mcp.setup(cls.gp_fitaLedChuveiro, mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_fitaLedChuveiro, mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
    
    @classmethod
    def acenderFitaLedChuveiro(cls):
        mcp.setup(cls.gp_fitaLedChuveiro, mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_fitaLedChuveiro, mcp.GPA, mcp.LOW, mcp.ADDRESS2)

    @classmethod
    def apagarLedVermelhoChuveiro(cls):
        mcp.setup(cls.gp_ledVermelhoChuveiro, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_ledVermelhoChuveiro, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

    @classmethod
    def acenderLedVermelhoChuveiro(cls):
        mcp.setup(cls.gp_ledVermelhoChuveiro, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_ledVermelhoChuveiro, mcp.GPB, mcp.LOW, mcp.ADDRESS2)


    # Metodo para acender o spots da lavanderia
    @classmethod
    def acenderSpotLavanderia(cls):
        mcp.escreverBinarioLuzes(0b0110) # Codigo do Spot da lavanderia e pia do banheiro


    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        passosConcluidos = [False, False, False] # Armazena quais passos foram concluidos

        while cls.isConcluida() == False:
            leitura = [
                GPIO.input(cls.gpio_registroTorneira),
                GPIO.input(cls.gpio_registroChuveiro),
                GPIO.input(cls.gpio_veraoChuveiro)
            ]
            # Se o registro da torneira for fechado e o passo ainda não foi concluido
            if leitura[0] == 0:
                # Marca este passo como concluido
                passosConcluidos[0] = True
                # Apaga o led do registro da torneira
                cls.apagarFitaLedTorneira()
            else:
                # Marca o passo como Não Concluido
                passosConcluidos[0] = False
                cls.acenderFitaLedTorneira()

            # Se o registro do chuveiro for fechado e o passo ainda não foi concluido
            if leitura[1] == 0:
                # Marca este passo como concluido
                passosConcluidos[1] = True
                # Apaga o led do registro do chuveiro
                cls.apagarFitaLedChuveiro()
            else:
                # Marca o passo como Não Concluido
                passosConcluidos[1] = False
                cls.acenderFitaLedChuveiro()

            # Se o chuveiro estiver no modo verao e o passo ainda não foi concluido
            if leitura[2] == 0:
                # Marca este passo como concluido
                passosConcluidos[2] = True
                # Apaga o led do modo verão do chuveiro
                cls.apagarLedVermelhoChuveiro()
            else:
                # Marca o passo como Não Concluido
                passosConcluidos[2] = False
                cls.acenderLedVermelhoChuveiro()
            
            # Sicronismo do som, Se a etapa da torneira ainda não foi concluida ou a etapa do chuveiro não foi concluida
            if passosConcluidos[0] == False or passosConcluidos[1] == False:
                # Os registros não estão fechados, o som de agua caindo deve tocar.
                cls.registrosFechados = False 
            else:
                # Os registros estão fechados, o som de agua caindo deve parar.
                cls.registrosFechados = True
            
            # Se todos os passos foram concluidos, libera a gaveta
            if passosConcluidos[0] == True and passosConcluidos[1] == True and passosConcluidos[2] == True:
                # Marca a logica como concluida para tocar o som
                cls._concluida = True
                time.sleep(3)
                # Luzes
                cls.acenderSpotLavanderia()
                time.sleep(3)
                # Acao
                cls.abrirGavetaBanheiro()

            # Pausa de 100ms no loop
            time.sleep(0.1)
            #print('8ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('8ª Logica - Finalizada')
            #cls.acenderSpotLavanderia()
            time.sleep(5)
            Logica_9.iniciarThread()

# ------ FIM DA LOGICA 7 ---------
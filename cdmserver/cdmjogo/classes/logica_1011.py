from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_1213 import Logica_1213

""" CLASSE das LOGICAs 10 e 11
Esta classe faz todo o controle dos itens relacionados a Logica 10 e 11

10 -> Dentro do armário terá um beijamin (T) com varias tomadas, ao lado varias tomadas
vazias, o objetivo do jogador é retirar as tomadas do "T" e direcionar para as tomadas
vazias, dentro do armario deverá ter uma mensagem "Cuidado com a segurança, não
ultilize mais de um equipamento na mesma tomada". Completando o desafio o baú da
sala abrirá.

11 -> Neste momento inicia a parte final do jogo, a musica mudará, clima de emoção. No
som o "repórter" iniciará as falas informando que a cidade já está sendo eficientizada,
que já é possivel ver mudanças nos comportamentos das pessoas (elaborar texto).
"""

class Logica_1011(Logica_geral):
    
    # GPIO's
    gpio_tomadas = 31 # Pino para leitura das tomadas ligadas em serie (raspberry)
    gpio_ledVermelho = 18
    gpio_ledVerde = 16

    # Relés
    gp_travaBau = 6 # GPA6 (MCP23017)

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradoresBanheiroAberto()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_tomadas, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)

        # Configurando GPIO's do Extensor 0x24
        mcp.setup(cls.gp_travaBau, mcp.GPA, mcp.OUT, mcp.ADDRESS2)

        # Inicialmente somente led vermelho acesso
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.HIGH))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.LOW))

        # Inicialmente em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_travaBau, mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b0111) # Codigo do spot das tomadas do armario

    # Metodo para destravar o Bau
    @classmethod
    def abrirBau(cls):

        # Marca a logica como concluida
        cls._concluida = True

        # Garantir que o pino esta como OUTPUT
        mcp.setup(cls.gp_travaBau , mcp.GPA, mcp.OUT, mcp.ADDRESS2)

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)

        # Acender led verde
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.LOW))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.HIGH))

        # Acender Spot Bau
        #cls.acenderSpotBau()

        for i in range(6):    
            # Em nivel Baixo acionando o Rele
            mcp.output(cls.gp_travaBau, mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            time.sleep(1)
            # Em nivel Alto desacionando o Rele
            mcp.output(cls.gp_travaBau, mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            time.sleep(2)


    # Metodo para acender o spot do bau
    @classmethod
    def acenderSpotBau(cls):
        mcp.escreverBinarioLuzes(0b1000) # Codigo do spot do bau

    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        while cls.isConcluida() == False:
            # Se for detectado a conexão das tomadas abre o bau
            leitura = GPIO.input(cls.gpio_tomadas)

            # Checa tambem a cada intervalo de tempo se o sinal continua em nivel alto
            if leitura == 1:
                time.sleep(0.125)
                leitura = GPIO.input(cls.gpio_tomadas)

                if leitura == 1:
                    time.sleep(0.125)
                    leitura = GPIO.input(cls.gpio_tomadas)

                    if leitura == 1:
                        # Marca a logica como concluida para tocar o som
                        cls._concluida = True
                        time.sleep(3)
                        # Luzes
                        cls.acenderSpotBau()
                        time.sleep(3)
                        # Acao
                        cls.abrirBau()

            # Pausa de 100ms no loop
            time.sleep(0.1)
            #print('10 e 11ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('10 e 11ª Logica - Finalizada')
            time.sleep(5)
            Logica_1213.iniciarThread()

# ------ FIM DA LOGICA 10 e 11 ---------
from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_1011 import Logica_1011

""" CLASSE da LOGICA 9
Esta classe faz todo o controle dos itens relacionados a Logica 9

9 -> Dentro da gaveta que abrirá, terá uma peça de roupa, que se juntará as demais peças
encontradas durante o jogo, essas peças serão em MDF e serão colocadas em cima
da mesa, onde haverá um baixo relevo e as peças encaixarão individualmente.

a. Imagem ilustrativa (peças de roupa)
b. Ao encaixar todas as peças abrirá o armário da cozinha, em cima do Micro-ondas
"""

class Logica_9(Logica_geral):
    
    # GPIO's
    gp_pinoSinalMesaPassar = 2 # Sinal 3.3v , GPB2 (MCP23017 0x22)
    ledAcimaMicroondasVermelho = 29 # (raspberry)
    ledAcimaMicroondasVerde = 24 # (raspberry)

    # Relés
    gp_travaPortaArmario = 5 # GPB5 (MCP23017 0x24)

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradoresBanheiroAberto()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        mcp.setup(cls.gp_pinoSinalMesaPassar, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Reed Switch bicicleta

        GPIO.setup(cls.ledAcimaMicroondasVermelho, GPIO.OUT)
        GPIO.setup(cls.ledAcimaMicroondasVerde, GPIO.OUT)

        # Configurando GPIO's do Extensor 0x24
        mcp.setup(cls.gp_travaPortaArmario, mcp.GPB, mcp.OUT, mcp.ADDRESS2)

        # Inicialmente somente led vermelho acesso
        GPIO.output(cls.ledAcimaMicroondasVermelho, not(GPIO.HIGH))
        GPIO.output(cls.ledAcimaMicroondasVerde, not(GPIO.LOW))

        # Inicialmente em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_travaPortaArmario, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b0110) # Codigo do Spot da lavanderia e pia do banheiro

    # Metodo para destravar o armario
    @classmethod
    def abrirArmario(cls):
        
        # Marca a logica como concluida
        cls._concluida = True

        # Garantir que o pino esta como OUTPUT
        mcp.setup(cls.gp_travaPortaArmario , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        
        # Em nivel Baixo acionando o Rele
        mcp.output(cls.gp_travaPortaArmario, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
        time.sleep(1)
        # Em nivel Alto desacionando o Rele
        mcp.output(cls.gp_travaPortaArmario, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.ledAcimaMicroondasVermelho, GPIO.OUT)
        GPIO.setup(cls.ledAcimaMicroondasVerde, GPIO.OUT)

        # Acender led verde
        GPIO.output(cls.ledAcimaMicroondasVermelho, not(GPIO.LOW))
        GPIO.output(cls.ledAcimaMicroondasVerde, not(GPIO.HIGH))


    # Metodo para acender o spot das tomadas do armario
    @classmethod
    def acenderSpotArmario(cls):
        mcp.escreverBinarioLuzes(0b0111) # Codigo do spot das tomadas do armario


    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        while cls.isConcluida() == False:
            # Se receber um sinal Baixo na porta, abre o armario (Sinal de 500ms em baixo)
            sinal = mcp.input(cls.gp_pinoSinalMesaPassar, mcp.GPB, mcp.ADDRESS1)

            # Checa tambem a cada intervalo de tempo se o sinal continua em nivel baixo
            if sinal == 0:
                time.sleep(0.125)
                sinal = mcp.input(cls.gp_pinoSinalMesaPassar, mcp.GPB, mcp.ADDRESS1)

                if sinal == 0:
                    time.sleep(0.125)
                    sinal = mcp.input(cls.gp_pinoSinalMesaPassar, mcp.GPB, mcp.ADDRESS1)
                    
                    if sinal == 0:
                        # Marca a logica como concluida para tocar o som
                        cls._concluida = True
                        time.sleep(3)
                        # Luzes
                        cls.acenderSpotArmario()
                        time.sleep(3)
                        # Acao
                        cls.abrirArmario()

            # Pausa de 100ms no loop
            time.sleep(0.1)
            #print('9ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('9ª Logica - Finalizada')
            #cls.acenderSpotArmario()
            time.sleep(5)
            Logica_1011.iniciarThread()

# ------ FIM DA LOGICA 9 ---------
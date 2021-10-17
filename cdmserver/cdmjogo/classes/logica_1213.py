from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp

""" CLASSE das LOGICAs 12 e 13
Esta classe faz todo o controle dos itens relacionados a Logica 12 e 13

12 -> No bau, terá alguns quadros que indicarão o caminho da energia, esses quadros
deverão ser colocados na sala na ordem correta. Os quadros poderão ter indicativos de
cores oun não (dependendo da dificuldade aplicada), colocados na ordem correta,
acontecerá um novo blackout (5%)

13 -> Logo após o blackout acenderá uma luz em cima de um aparador (mesa central),
dentro deste aparador, uma chave liga e desliga (pensar em chave faca ou algo de expressão)

a. Imagem ilustrativa
b. Ao acionar a chave, uma musica intensa (vitória), reestabelecimento da
energia e inicio do encerramento do jornal.
"""

class Logica_1213(Logica_geral):
    
    # GPIO's
    gpio_sinal = 8 # Sinal 3.3v vindo do arduino quadros (raspberry)
    gp_chave = 5 # Botao GPB5 (MCP23017)

    gpio_ledVermelho = 12
    gpio_ledVerde = 10

    # Relés
    #gp_luzAparador = x #  (MCP23017)
    gp_travaAparador = 7 # GPA7 (MCP23017)

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradoresBanheiroAberto()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_sinal, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)

        mcp.setup(cls.gp_chave, mcp.GPB, mcp.IN, mcp.ADDRESS1)

        # Configurando GPIO's do Extensor 0x24
        #mcp.setup(cls.gp_luzAparador, mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_travaAparador, mcp.GPA, mcp.OUT, mcp.ADDRESS2)

        # Inicialmente somente led vermelho acesso
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.HIGH))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.LOW))

        # Inicialmente em nivel Baixo (Rele acionado - Luz apagada)
        #mcp.output(cls.gp_luzAparador, mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        
        # Inicialmente desativada a trava
        mcp.output(cls.gp_travaAparador, mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b1000) # Codigo do spot do bau


    # Metodo para acender a Luz do aparador
    @classmethod
    def acenderLuzAparador(cls):
        mcp.escreverBinarioLuzes(0b1001) # Codigo do aparador

    # Rotina para blackou e acender acender luz aparador
    @classmethod
    def rotinaBlackout(cls):
        mcp.escreverBinarioLuzes(0b1101) # Codigo do blackout
        time.sleep(3)
        cls.acenderLuzAparador()

    # Metodo para acender todas as luzes
    @classmethod
    def acenderTodasLuzes(cls):
        mcp.escreverBinarioLuzes(0b1101) # Codigo de Blackout
        time.sleep(2)
        mcp.escreverBinarioLuzes(0b1100) # Codigo de Acendimento Gradual

    # Rotina para acender as luzes da sala
    @classmethod
    def reestabelecerEnergia(cls):
        cls.acenderTodasLuzes()
        # Marca a logica como concluida
        cls._concluida = True
        # Toca som de vitoria

    # Rotina destravar gaveta botao
    @classmethod
    def abrirGavetaAparador(cls):
        mcp.setup(cls.gp_travaAparador, mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.output(cls.gp_travaAparador, mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        time.sleep(1)
        mcp.output(cls.gp_travaAparador, mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)

        # Acender led verde
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.LOW))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.HIGH))


    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        gavetaAberta = False
        
        while cls.isConcluida() == False:

            if GPIO.input(cls.gpio_sinal) == 1 and gavetaAberta == False:
                # Nao possui som esta etapa
                # Luzes
                cls.rotinaBlackout()
                time.sleep(3)
                # Acao
                cls.abrirGavetaAparador()
                gavetaAberta = True

            # Se o botao for pressionado
            if mcp.input(cls.gp_chave, mcp.GPB, mcp.ADDRESS1) == 1:
                # reestabele energia
                cls.reestabelecerEnergia()

            # Pausa de 250ms no loop
            #time.sleep(0.25)
            #print('12 e 13ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('10 e 13ª Logica - Finalizada')

# ------ FIM DA LOGICA 12 e 13 ---------
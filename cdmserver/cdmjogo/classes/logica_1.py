from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle GPIO
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_23 import Logica_23

""" CLASSE da LOGICA 1
Esta classe faz todo o controle dos itens relacionados a Logica 1

1 -> Jogadores entram na sala, com uma luz baixa, que ilumine somente a sala
(somente a sala acessa). Os jogadores assistiram ao video introdutório.
"""

class Logica_1(Logica_geral):

    # GPIO's
    ledDivisoriaVermelho = 37 # Divisora
    ledDivisoriaVerde = 35
    ledGavetaInferiorVermelho = 21 # Gaveta inferior
    ledGavetaInferiorVerde = 23
    ledAcimaMicroondasVermelho = 29 # Porta acima do microondas
    ledAcimaMicroondasVerde = 24
    ledPiaVermelho = 15 # Pia banheiro
    ledPiaVerde = 19
    ledAparadorVermelho = 12 # Aparador
    ledAparadorVerde = 10
    ledBauVermelho = 18 # Bau
    ledBauVerde = 16
    ledGeladeiraVermelho = 38 # Geladeira 40 e 38
    ledGeladeiraVerde = 40

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configura as GPIOs como BOARD, Contagem de 0 a 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        ledsVermelhos = [
            cls.ledDivisoriaVermelho,
            cls.ledGavetaInferiorVermelho,
            cls.ledAcimaMicroondasVermelho,
            cls.ledPiaVermelho,
            cls.ledAparadorVermelho,
            cls.ledBauVermelho,
            cls.ledGeladeiraVermelho
        ]

        ledsVerdes = [
            cls.ledDivisoriaVerde,
            cls.ledGavetaInferiorVerde,
            cls.ledAcimaMicroondasVerde,
            cls.ledPiaVerde,
            cls.ledAparadorVerde,
            cls.ledBauVerde,
            cls.ledGeladeiraVerde
        ]

        leds = ledsVermelhos + ledsVerdes

        # configura todos os pinos de LED para saída (GPIO.OUT)
        for pino in leds:
            GPIO.setup(pino, GPIO.OUT)

        # acende os leds vermelhos, apaga os leds verdes
        for i in range(len(ledsVermelhos)):
            GPIO.output(ledsVermelhos[i], not(GPIO.HIGH))
            GPIO.output(ledsVerdes[i], not(GPIO.LOW))

    # Metodo para acender somente a luz da sala
    @classmethod
    def luzBaixaSala(cls):
        # Codigo binario para manter apenas a luz da sala Acessa
        mcp.escreverBinarioLuzes(0b0001)
        cls._concluida = True

    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        while cls.isConcluida() == False:
            #print('1ª Logica Rodando')
            time.sleep(0.15)
            pass
            
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('1ª Logica - Finalizada')
            time.sleep(5)
            Logica_23.iniciarThread()

# ------ FIM DA LOGICA 1 ---------
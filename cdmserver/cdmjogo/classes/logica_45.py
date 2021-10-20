from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_6 import Logica_6

""" CLASSE das LOGICAs 4 e 5
Esta classe faz todo o controle dos itens relacionados a Logica 4 e 5

4 -> Ao pedalar, um painel ao lado da Bike iniciará e será completado(barra de LED), junto
a este painel uma frase "cada pessoa pode gerar a própria energia".

5 -> Ao completar a barra de "energia", a luz da casa aumentará para (50%) e a gaveta da
cozinha abrirá, fazendo barulho e ascendendo o LED indicando a gaveta liberada.
"""

class Logica_45(Logica_geral):

    # Portas nativas
    gpio_ledGavetaVermelho = 21 # Led indicador de gaveta fechada (raspberry)
    gpio_ledGavetaVerde = 23 # Led indicador de gaveta aberta (raspberry)

    # Portas extendidas MCP23017 0x24
    gp_reedSwitchBicicleta = 0 # GPB0 (MCP23017 0x22)
    gp_barraLed = [2,3,4,5] # GPA5, GPA4, GPA3, GPA2 (MCP23017 0x24)
    gp_travaGaveta = 4 #GPB4 (MCP23017 0x24)
    #gp_luzCasa = 0 # GPA0 (MCP23017 0x24)

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradores()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_ledGavetaVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledGavetaVerde, GPIO.OUT)

        mcp.setup(cls.gp_reedSwitchBicicleta, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Reed Switch bicicleta

        # Configurando GPIO's do Extensor 0x24
        mcp.setup(cls.gp_barraLed[0], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[1], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[2], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[3], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        #mcp.setup(cls.gp_luzCasa    , mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_travaGaveta, mcp.GPB, mcp.OUT, mcp.ADDRESS2)

        # Led gaveta verde apagado e vermelho acesso
        GPIO.output(cls.gpio_ledGavetaVermelho, not(GPIO.HIGH))
        GPIO.output(cls.gpio_ledGavetaVerde, not(GPIO.LOW))
        
        # Inicialmente em nivel Baixo (Rele Acionado - Abre o circuito das luzes)
        #mcp.output(cls.gp_luzCasa    , mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        # Inicialmente em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b0010) # Codigo de acender spot bike e bateria

    # Metodo para acender o barra de Leds
    # Nivel = 0 --> Acessa 1ª Barra
    # Nivel = 1 --> Acessa 1ª e 2ª Barra
    # Nivel = 2 --> Acessa 1ª,2ª e 3ª Barra
    # Nivel = 3 --> Acessa 1ª,2ª,3ª e 4ª Barra
    # Se não especificar o nivel, será armazenado 0 na variavel
    @classmethod
    def acenderBarraLedNivel(cls, nivel = 0):
        # Garantir que os pinos estao como OUTPUT
        mcp.setup(cls.gp_barraLed[0], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[1], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[2], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[3], mcp.GPA, mcp.OUT, mcp.ADDRESS2)

        # Acender a 1ª Barra
        if nivel == 0 or nivel < 0:
            mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW , mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

        # Acender 1ª e 2ª Barra
        elif nivel == 1:
            mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW , mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

        # Acender 1ª,2ª e 3ª Barra
        elif nivel == 2:
            mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW , mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

        # Acender 1ª,2ª,3ª e 4ª Barra
        else:
            mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW , mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.LOW, mcp.ADDRESS2)

    # Metodo para apagar a barra de led
    @classmethod
    def apagarBarraLed(cls):
        # Garantir que os pinos estao como OUTPUT
        mcp.setup(cls.gp_barraLed[0], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[1], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[2], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[3], mcp.GPA, mcp.OUT, mcp.ADDRESS2)

        # Em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)

    @classmethod
    # Efeito Bateria carregando final
    def efeitoCarregandoFinal(cls):
        intervalo = 0.25

        # Garantir que os pinos estao como OUTPUT
        mcp.setup(cls.gp_barraLed[0], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[1], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[2], mcp.GPA, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_barraLed[3], mcp.GPA, mcp.OUT, mcp.ADDRESS2)

        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        time.sleep(intervalo)
        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        time.sleep(intervalo)
        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        time.sleep(intervalo)
        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        time.sleep(intervalo)
        mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
        time.sleep(intervalo)

        for i in range(2):
            mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.HIGH, mcp.ADDRESS2)
            time.sleep(intervalo)
            mcp.output(cls.gp_barraLed[0], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[1], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[2], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            mcp.output(cls.gp_barraLed[3], mcp.GPA, mcp.LOW, mcp.ADDRESS2)
            time.sleep(intervalo)


    # Metodo para abrir a gaveta
    @classmethod
    def abrirGaveta(cls):

        # Marca a logica como concluida
        cls._concluida = True

        # Garantir que o pino esta como OUTPUT
        mcp.setup(cls.gp_travaGaveta , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        
        # Em nivel Baixo acionando o Rele
        mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
        time.sleep(1)
        # Em nivel Alto desacionando o Rele
        mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

        # Acende o led indicativo
        # Garantindo que o pino estará como OUTPUT
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        GPIO.setup(cls.gpio_ledGavetaVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledGavetaVerde, GPIO.OUT)

        GPIO.output(cls.gpio_ledGavetaVermelho, not(GPIO.LOW))
        GPIO.output(cls.gpio_ledGavetaVerde, not(GPIO.HIGH))



    # Metodo para acender Spot Gaveta Cozinha
    @classmethod
    def acenderSpotGavetaCozinha(cls):
        mcp.escreverBinarioLuzes(0b0011) # Codigo do Spot Gaveta cozinha
    

    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        contadorPulso = 0 # Conta quantos pulsos a raspberry recebeu
        leituraAnterior = 1 # Inicialmente leitura e nivel Alto

        while cls.isConcluida() == False:

            leitura = mcp.input(cls.gp_reedSwitchBicicleta, mcp.GPB, mcp.ADDRESS1)

            if leitura == 1 and leituraAnterior == 0:
                contadorPulso += 1
                leituraAnterior = 1

                if contadorPulso == 1:
                    cls.acenderBarraLedNivel(0)

                elif contadorPulso == 5:
                    cls.acenderBarraLedNivel(1)

                elif contadorPulso == 10:
                    cls.acenderBarraLedNivel(2)
                    
                elif contadorPulso == 15:
                    cls.acenderBarraLedNivel(3)
                    time.sleep(0.25)
                    cls.efeitoCarregandoFinal()
                    
                    # Marca a logica como concluida para tocar o som
                    cls._concluida = True
                    time.sleep(3)
                    # Altera a luz
                    cls.acenderSpotGavetaCozinha()
                    time.sleep(3)
                    # Em seguida abre a gaveta
                    cls.abrirGaveta()

            elif leitura == 0 and leituraAnterior == 1:
                # leitura difente
                leituraAnterior = 0
                    

                # Pausa de 250ms no loop
                #time.sleep(0.25)
                #print('4ª e 5ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('4ª e 5ª Logica - Finalizada')
            #cls.acenderSpotGavetaCozinha()
            time.sleep(5)
            Logica_6.iniciarThread()

# ------ FIM DA LOGICA 4 e 5 ---------

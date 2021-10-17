from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_7 import Logica_7

""" CLASSE das LOGICAs 6
Esta classe faz todo o controle dos itens relacionados a Logica 6

6 -> Dentro da gaveta¹ terá 3 etiquetas ENCE com bordas coloridas, que deverá ser
colocado na Geladeira, Micro-ondas e Maquina de lavar, nos equipamentos, já haverá
uma etiqueta não eficiente, as novas etiquetas serão colocadas em cima das antigas
adequando a etiqueta correta e a cor indicada, o que dará uma ideia de substituição de
equipamentos. Será ideal ascender uma luz verde ao inserir a etiqueta correta.
Colocando as etiquetas corretas, a geladeira deverá abrir.
"""

class Logica_6(Logica_geral):

    # GPIO's
    gpio_etiquetaGeladeira = 36 # 36 Raspberry
    gpio_etiquetaMicroondas = 33 # 33 Raspberry
    gp_etiquetaMaquina = 4 # GPB4 (MCP23017)

    ## Geladeira 40 e 38
    gpio_ledVermelho = 38
    gpio_ledVerde = 40

    # Relés
    gp_travaGeladeira = 6 # GPB6 (MCP23017)

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradoresGeladeiraAberta()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)

        GPIO.setup(cls.gpio_etiquetaGeladeira, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
        GPIO.setup(cls.gpio_etiquetaMicroondas, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
        mcp.setup(cls.gp_etiquetaMaquina, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Etiqueta maquina

        # Configurando GPIO's do Extensor 0x24
        mcp.setup(cls.gp_travaGeladeira, mcp.GPB, mcp.OUT, mcp.ADDRESS2)

        # Led gaveta verde apagado e vermelho acesso
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.HIGH))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.LOW))

        # Inicialmente em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_travaGeladeira, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b0011) # Codigo do Spot Gaveta cozinha

    # Metodo para destravar a geladeira
    @classmethod
    def abrirGeladeira(cls):
        
        # Marca a logica como concluida
        cls._concluida = True

        # Loop pois a trava causa disturbio no sistema
        for i in range(1):
            # Garantir que o pino esta como OUTPUT
            mcp.setup(cls.gp_travaGeladeira , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
            
            # Em nivel Baixo acionando o Rele
            mcp.output(cls.gp_travaGeladeira, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
            time.sleep(0.75)
        
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)
        # Led gaveta verde apagado e vermelho acesso
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.LOW))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.HIGH))


    # Metodo para acender o spot da geladeira
    @classmethod
    def acenderSpotGeladeira(cls):
        mcp.escreverBinarioLuzes(0b0100) # Codigo do Spot da geladeira

    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        rfidsOk = [0,0,0]

        while cls.isConcluida() == False:

            leituraGel = GPIO.input(cls.gpio_etiquetaGeladeira)
            leituraMic = GPIO.input(cls.gpio_etiquetaMicroondas)
            leituraMaq = mcp.input(cls.gp_etiquetaMaquina, mcp.GPB, mcp. ADDRESS1)

            # leituraMaq = 0 # JUMPER NO CODIGO

            if leituraGel == 0:
                rfidsOk[0] = 1

            if leituraMic == 0:
                rfidsOk[1] = 1

            if leituraMaq == 0:
                rfidsOk[2] = 1

            
            if rfidsOk == [1,1,1]:
                # Marca a logica como concluida para tocar o som
                cls._concluida = True
                time.sleep(3)
                # Altera a luz
                cls.acenderSpotGeladeira()
                time.sleep(3)
                # Em seguida faz ação
                cls.abrirGeladeira()

            print(rfidsOk)

            # Pausa de 150ms no loop
            #time.sleep(0.15)
            #print('6ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('6ª Logica - Finalizada')
            #cls.acenderSpotGeladeira()
            time.sleep(5)
            Logica_7.iniciarThread()

# ------ FIM DA LOGICA 6 ---------
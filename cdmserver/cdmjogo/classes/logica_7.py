from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
import RPi.GPIO as GPIO # Modulo de controle da GPIOs
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_8 import Logica_8

""" CLASSE das LOGICAs 7
Esta classe faz todo o controle dos itens relacionados a Logica 7

7 -> Dentro da geladeira, no espaço destinado as prateleiras deverá ter um jogo de
perguntas sobre dicas de eficiencia para a geladeira, cada frase terá uma botoeira de
giro, indicando a resposta correta. Ex:

a. "Nunca" ou "Sempre" coloque panela quente dentro da geladeira
b. "Nunca" ou "Sempre" deixe um espaço entre a parede e o fundo da geladeira
c. Imagem ilustrativa de uma geladeira
d. Inserir uma mensagem na geladeira, "Não forçar, geladeira abrirá automaticamente"
e. Verificar possibilidade de botão que valida as opções (Star)
f. Após responder corretamente a porta do banheiro abrirá.
"""

class Logica_7(Logica_geral):

    # GPIO's
    gpio_pinoSinal = 32 # Botoeiras ligadas em serie usando somente um pino (raspberry)
    gpio_ledVermelho = 37 # Led vermelho indicando ordem incorreta
    gpio_ledVerde = 35 # Led verde indicando ordem correta

    # Relés
    gp_ledsJogoGeladeira = 7 #GPB7
    gp_travaPortaBanheiro = 3 # GPB3 (MCP23017)

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):

        # Configurar os registradores
        mcp.confRegistradoresBanheiroAberto()

        # Configurado GPIO's do raspberry
        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        
        GPIO.setup(cls.gpio_pinoSinal, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
        
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT) # Pino como PULL-DOWN interno
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT) # Pino como PULL-DOWN interno

        # Configurando GPIO's do Extensor 0x24
        mcp.setup(cls.gp_ledsJogoGeladeira, mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        mcp.setup(cls.gp_travaPortaBanheiro, mcp.GPB, mcp.OUT, mcp.ADDRESS2)

        # Inicialmente somente led vermelho acesso
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.HIGH))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.LOW))

        # Inicialmente em nivel Alto (Rele desacionado - Sem corrente circulando)
        mcp.output(cls.gp_ledsJogoGeladeira, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)
        mcp.output(cls.gp_travaPortaBanheiro, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)

        # Luzes ao inicio da Logica
        mcp.confRegistradoresLuzes() # GPA como output
        mcp.escreverBinarioLuzes(0b0100) # Codigo do Spot da geladeira

    
    # Methodo para piscar fita de leds da geladeira
    @classmethod
    def piscarLedsGeladeira(cls):
        
        mcp.setup(cls.gp_ledsJogoGeladeira, mcp.GPB, mcp.OUT, mcp.ADDRESS2)

        for i in range(3):
            mcp.output(cls.gp_ledsJogoGeladeira, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
            time.sleep(0.25)
            mcp.output(cls.gp_ledsJogoGeladeira, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)
            time.sleep(0.25)

        #mcp.output(cls.gp_ledsJogoGeladeira, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
    
    # Metodo para destravar a porta do banheiro
    @classmethod
    def abrirPortaBanheiro(cls):

        # Marca a logica como concluida
        cls._concluida = True

        # Loop pois a trava causa disturbio no sistema
        for i in range(1):
            # Garantir que o pino esta como OUTPUT
            mcp.setup(cls.gp_travaPortaBanheiro , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
            
            # Em nivel Baixo acionando o Rele
            mcp.output(cls.gp_travaPortaBanheiro, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
            time.sleep(0.75)

        GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
        GPIO.setwarnings(False) # Desativa avisos
        GPIO.setup(cls.gpio_ledVermelho, GPIO.OUT)
        GPIO.setup(cls.gpio_ledVerde, GPIO.OUT)
        # Led gaveta verde apagado e vermelho acesso
        GPIO.output(cls.gpio_ledVermelho, not(GPIO.LOW))
        GPIO.output(cls.gpio_ledVerde, not(GPIO.HIGH))

    # Metodo para acender o spots do banheiro
    @classmethod
    def acenderSpotsBanheiro(cls):
        mcp.escreverBinarioLuzes(0b0101) # Codigo do Spot do banheiro

    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        # Repete enquanto esta logica não for concluida
        while cls.isConcluida() == False:
            # Se o botão for pressionado, checa o estado das botoeiras
            if GPIO.input(cls.gpio_pinoSinal) == 0:
                
                # Marca a logica como concluida para tocar o som juntamente com piscar dos leds
                cls._concluida = True
                cls.piscarLedsGeladeira()
                time.sleep(1.5)
                # Luzes
                cls.acenderSpotsBanheiro()
                time.sleep(3)
                # Acao
                cls.abrirPortaBanheiro()
                    
            # Pausa de 150ms no loop
            #time.sleep(0.15)
            #print('7ª Logica Rodando')
        
        else:
            # Ao finalizar o loop, ou seja, concluir a logica, Imprime uma mensagem
            print('7ª Logica - Finalizada')
            #cls.acenderSpotsBanheiro()
            time.sleep(1)
            Logica_8.iniciarThread()

# ------ FIM DA LOGICA 7 ---------
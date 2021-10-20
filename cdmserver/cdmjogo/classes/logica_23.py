from .logica_geral import Logica_geral # Classe pai para herança
import time # Modulo para delays e contagem de tempo
from cdmjogo.classes.mcp23017 import MCP23017 as mcp
from cdmjogo.classes.logica_45 import Logica_45

""" CLASSE da LOGICA 2 e 3
Esta classe faz todo o controle dos itens relacionados a Logica 2 e 3

2 -> Após o video, acontecerá o Blackout (somente luz da bicicleta que acenderá após 3
segundos) e na tela da TV aparecerá uma imagem de um marcador de consumo, onde
no seu máximo estará vermelho, no meio laranja e nno minimo verde. O objetivo é que
em cada ação de eficiência o marcador reduza para a posição verde(positivo)

3 -> Após o blackout ascenderá uma luz em cima da bicicleta com 2 focos, uma na bicicleta e
outra no quadro ao lado da bicicleta, essa luz direcionará os jogadores a pedalar a bike.
"""

class Logica_23(Logica_geral):

    # Sobreescrevendo metodo setup() da classe pai
    @classmethod
    def setup(cls):
        pass

    # Metodo para blackout
    @classmethod
    def blackout(cls):
        mcp.escreverBinarioLuzes(0b1101) # Codigo do Blackout
        time.sleep(5)
        cls.acenderSpotBikeBateria()

    # Metodo para acender a luz do bateria
    @classmethod
    def acenderSpotBikeBateria(cls):
        mcp.escreverBinarioLuzes(0b0010) # Codigo de acender spot bike e bateria
        cls._concluida = True

    # Sobreescrevendo metodo threadLogica() da classe pai
    @classmethod
    def threadLogica(cls):
        
        while cls.isConcluida() == False:
            #print('2ª Logica Rodando')
            time.sleep(0.15)
            pass
        else:
            print('2ª Logica - Finalizada')
            time.sleep(5)
            Logica_45.iniciarThread()

# ------ FIM DA LOGICA 2 e 3 ---------
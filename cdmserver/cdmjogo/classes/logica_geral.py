"""Modulo com os metodos e atributos comuns de todas as logicas.
"""

import time # Modulo para delays e contagem de tempo
import threading # Modulo para trabalhar com treads

class Logica_geral(object):
    """Classe Logica_geral, usada como classe Pai para herancas nas classes Logica_n do jogo.
    
    * Não serão criadas instancias das classes(Logica_n) herdadas desta classe(Logica_geral),
      pois a logica de programação desenvolvida prevê o uso de metodos de classe.
    Atributos da classe:
        _concluida (bool): Armazena o status da logica, False = Não Concluida e True = Concluida
        _thread (Thread): Armazena a Thread da classe que faz a checagem dos estados dos sensores
    """

    _concluida = False
    _thread = None

    # METODOS DA CLASSE

    @classmethod
    def setup(cls):
        """Metodo Setup
        Neste metodo serão configurados as GPIOS da raspberry e as GPIOS do MCP23017, pode-se incluir outras configurações
        * Deve ser implementado na classe filha, se não gerará uma exceção `NotImplementedError`
        """
        raise NotImplementedError('É necessário implementar o metodo setup() na classe filha! ')

    @classmethod
    def isConcluida(cls):
        return cls._concluida

    @classmethod
    def iniciarThread(cls):
        # Se o atributo _thread é Vazio cria uma tread
        if cls._thread == None:
            cls._thread = threading.Thread(target=cls.threadLogica)
        
        # Verifica se a tread não esta em execucao e se ainda nao foi concluida
        # Senão Se a logica esta em execução, Imprime no terminal uma mensagem informando que a thread da logica esta em execucao
        # Senão, Imprime no terminal uma mensagem informando que a thread da logica já foi concluida
        # O cls.__name__ pega o nome da classe onde esta funcao foi chamada
        if cls._thread.isAlive() == False and cls.isConcluida() == False:
            cls.setup() # Executa o metodo setup()
            #time.sleep(1) # Delay de 1 segundo
            cls._thread.start() # Inicia a thread

        elif (cls._thread.isAlive() == True):
            print('Thread da ' + str(cls.__name__) + ' em execução, é necessario reinicia-la para executar do inicio.')
        
        else:
            print('Thread da ' + str(cls.__name__) + ' já concluida, é necessario reinicia-la para executar novamente.')

    @classmethod
    def threadLogica(cls):
        """Thread threadLogica()
        Este metodo(Tarefa) ficará em loop checando os sensores
        * Deve ser implementado na classe filha, se não gerará uma exceção `NotImplementedError`
        """
        raise NotImplementedError('É necessário implementar o metodo threadLogica() na classe filha! ')

# ------ FIM CLASSE Logica_geral ------
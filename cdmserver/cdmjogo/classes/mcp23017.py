import smbus2 # Importar modulo para acesso de registradores de dispositivos I2C

""" CLASSE MCP23017
Esta classe faz a comunicacao I2C com os extensores de porta MCP23017
Conectados ao barramento I2C do raspberry
"""
class MCP23017(object):
    """
    O MCP23017 é um expansor de IO com uma interface serial i2C ou SPI. Cada chip possui dois
    bancos de pinos de IO: GPA0-GPA7 e GPB0-GPB7. Três linhas de endereço permitem selecionar 
    o chip desejado em um barramento; desta forma, até 8 MCP23017 podem estar ligados ao mesmo
    barramento.

    O endereço é repassado nas mensagens i2C. O campo de endereço tem 4 bits com um ID fixo 
    padrão 0b0100, que é um código que identifica um MCP23017. Desta forma ao endereçar o 
    MCP23017, a identificação será entre 0b0100000 e 0b0100111, ou seja: 0x20 até 0x27.

    O chip possui três pinos A0/A1/A2 que são setados por hardware no projeto da placa para 
    responder nos endereços de 0 a 7.

    A placa de controle da CDM possui dois chips MCP23017, sendo que um opera no endereço 0x22 
    (ADDRESS1) e o outro no endereço 0x24 (ADDRESS2).

    No total, a placa de expansão da CDM possui até 32 bits de IO disponíveis, além dos bits
    da GPIO interna do Raspberry Pi.

    As operações de leitura e escrita sempre operam em todos os 8 bits ao mesmo tempo; a 
    máscara aplicada via IODIR especifica se o pino será usado para leitura ou para escrita 
    naquela operação.

    Desta forma, a cada operação, é necessário sempre fazer um "setup" dos pinos para em 
    seguida usar uma mensagem de leitura e/ou escrita.

    Referências:
    - https://www.best-microcontroller-projects.com/mcp23017.html
    - https://www.raspberrypi-spy.co.uk/2013/07/how-to-use-a-mcp23017-i2c-port-expander-with-the-raspberry-pi-part-2/
    """

    # ATRIBUTOS DE CLASSE
    n_barramento = 0x01 # Numero do Barramento I2C do raspberry (No nosso caso é 1)
    ADDRESS1 = 0x22 # Endereco do primeiro chip MC23017 (Definido pela configuracao A0,A1,A2)
    ADDRESS2 = 0x24 # Endereco do segundo chip MC23017 (Definido pela configuracao A0,A1,A2)
    barramento = None # Atributo que guarda a instancia do barramento

    # Enderecos de alguns registradores do chip MCP23017 em hexadecimal

    # IODIR é o registro de configuração dos pinos para OUTPUT (bit 0) e INPUT (bit 1)
    IODIRA = 0x00  
    IODIRB = 0x01  
    # Protecao contra oscilacao de pinos configurados como INPUT,
    # 1=Resistor de 100k interno habilitado, 0=Desabilitado
    GPPUA = 0x0C   
    GPPUB = 0x0D   
    # Configuracao dos pino de INPUT como PULL UP ou PULL DOWN
    # 0=PULL DOWN , 1=PULL UP
    IPOLA = 0x02
    IPOLB = 0x03
    # Configuracao dos pinos de OUTPUT, similar ao digitalWrite do arduino
    # 0=LOW e 1=HIGH
    OLATA = 0x14
    OLATB = 0x15
    # Leitura dos pinos INPUT e OUTPUT, similar ao digitalRead do arduino
    # Obs: confirmar se permite ler o status de um pino que foi escrito
    GPIOA = 0x12
    GPIOB = 0x13

    # ------ FIM REGISTRADORES ------
    IN = 'IN' # Constante de entrada
    OUT = 'OUT' # Constante de saida
    LOW = 0 # Constante de nivel baixo
    HIGH = 1 # Constante de nivel alto
    GPA = 'GPA'
    GPB = 'GPB'

    # ------ FIM CONSTANTES

    # Este metodo instancia o barramento
    @classmethod
    def instanciarBarramento(cls):
        # Instancia o barramento se ele ainda nao foi instanciado
        if cls.barramento == None:
            cls.barramento = smbus2.SMBus(cls.n_barramento)
        pass


    # Este metodo escolhe qual metodo chamar, setando a gpio como OUTPUT ou INPUT
    # Chamada: MCP23017.setup(7, MCP23017.GPA, MCP23017.IN, MCP23017.ADDRESS1)
    @classmethod
    def setup(cls, gpio, GPA_B, IN_OUT, address):
        cls.instanciarBarramento()
        if IN_OUT == 'IN':
            #cls.setup_in(gpio, GPA_B, address)
            pass
        elif IN_OUT == 'OUT':
            #cls.setup_out(gpio, GPA_B, address)
            pass
        else:
            print('Erro no Mcp23017.setup()')
        pass

    # Este metodo configura o bit da gpio como output escrevendo 0 nele
    # O metodo setup que chama ele
    @classmethod
    def setup_out(cls, gpio, GPA_B, address):
        cls.instanciarBarramento()
        # Verifica qual registrador usar
        if GPA_B == 'GPA':
            registrador = cls.IODIRA
        elif GPA_B == 'GPB':
            registrador = cls.IODIRB
        else:
            print('Erro no Mcp23017.setup_out(), GPA_B invalida')
        
        if gpio <= 7: # Evita uso de GPIO inexistentes
            status_registrador = cls.barramento.read_byte_data(address, registrador) # Le o valor atual do registrador
            byte_comparador = 0b00000001 << gpio
            novo_status_registrador = status_registrador | byte_comparador # Realiza uma operacao OR com 1
            if status_registrador == novo_status_registrador:
                novo_status_registrador = status_registrador ^ byte_comparador # Realiza uma operacao XOR e inverte o bit
                # Escreve no registrador do extensor
                cls.barramento.write_byte_data(address, registrador, novo_status_registrador)
            else:
                pass # Nao executa nada pois o bit ja esta como output
        else:
            print('Erro no Mcp23017.setup_out(), gpio invalida')
        pass

    
    # Este metodo configura o bit da gpio como INPUT escrevendo 1 nele
    # O metodo setup que chama ele
    @classmethod
    def setup_in(cls, gpio, GPA_B, address):
        cls.instanciarBarramento()
        # Verifica qual registrador usar
        if GPA_B == 'GPA':
            registrador = cls.IODIRA
            #registrador_2 = cls.GPPUA
            #registrador_3 = cls.IPOLA
        elif GPA_B == 'GPB':
            registrador = cls.IODIRB
            #registrador_2 = cls.GPPUB
            #registrador_3 = cls.IPOLB
        else:
            print('Erro no Mcp23017.setup_in(), GPA_B invalida')
        
        if gpio <= 7: # Evita uso de GPIO inexistentes
            status_registrador = cls.barramento.read_byte_data(address, registrador) # Le o valor atual do registrador
            byte_comparador = 0b00000001 << gpio
            novo_status_registrador = status_registrador | byte_comparador # Realiza uma operacao 'OR'
            # Escreve no registrador do extensor
            cls.barramento.write_byte_data(address, registrador, novo_status_registrador) # IODIR
            #cls.barramento.write_byte_data(address, registrador_2, novo_status_registrador) #GPPU
        else:
            print('Erro no Mcp23017.setup_in(), gpio invalida')
        pass

    # Escreve 0 ou 1 na GPIO
    # Chamada: MCP23017.output(7, MCP23017.GPA, MCP23017.HIGH, MCP23017.ADDRESS1)
    @classmethod
    def output(cls, gpio, GPA_B, LOW_HIGH, address):
        cls.instanciarBarramento()
        # Verifica qual registrador usar
        if GPA_B == 'GPA':
            registrador = cls.OLATA
        elif GPA_B == 'GPB':
            registrador = cls.OLATB
        else:
            print('Erro no Mcp23017.output(), GPA_B invalida')

        if gpio <= 7: # Evita uso de GPIO inexistentes
            status_registrador = cls.barramento.read_byte_data(address, registrador)
            byte_comparador = 0b00000001 << gpio
            novo_status_registrador = status_registrador | byte_comparador
            if LOW_HIGH == cls.HIGH:
                cls.barramento.write_byte_data(address, registrador, novo_status_registrador) # OLAT
            elif LOW_HIGH == cls.LOW:
                if status_registrador == novo_status_registrador: # Se forem iguais inverte o estado do bit
                    novo_status_registrador = status_registrador ^ byte_comparador # Inverte o estado do bit com XOR
                    cls.barramento.write_byte_data(address, registrador, novo_status_registrador) # OLAT
                else:
                    pass # Nao faz nada pois o bit ja esta em 0
        pass


    # Este metodo le o valor do BIT referente a GPIO recebida como argumento
    @classmethod
    def input(cls, gpio, GPA_B,address):
        cls.instanciarBarramento()
        # Verifica qual registrador usar
        if GPA_B == 'GPA':
            registrador = cls.GPIOA
        elif GPA_B == 'GPB':
            registrador = cls.GPIOB
        else:
            status_gpio = -1 # Retorna -1 para ressaltar um erro
        
        if gpio <= 7: # Evita uso de GPIO inexistentes
            status_registrador = cls.barramento.read_byte_data(address, registrador) # Le o valor atual do registrador GPIOA(12) ou GPIOB(13)
            #print("Leitura HEX: " + str(hex(status_registrador)) + " BIN: " + str(bin(status_registrador)) + " INT:" + str(status_registrador))
            # Gera um byte comparador deslocando o 1 para o bit correspondente a GPIO e os demais bits recebem 0
            byte_comparador = 0b00000001 << gpio
            # Faz uma operacao logica 'and' do status_registrador com o byte_comparador
            status_gpio = status_registrador & byte_comparador
            # Se a operacao 'and' retorna um byte igual ao comparador significa que tem 1 na GPIO, se nao 0
            if status_gpio == byte_comparador:
                status_gpio = 1
            else:
                status_gpio = 0
        else:
            status_gpio = -2 # Retorna -2 para ressaltar um erro
        return status_gpio

    @classmethod
    def confRegistradores(cls):
        print('Escrevendo 0x00 em todos os registradores...')
        cls.instanciarBarramento()

        #--------------------------------------------------------------
        # MCP23017 #01 
        # Extensor 0x22

        # GPA7 GPA6 GPA5 GPA4 GPA3 GPA2 GPA1 GPA0 = 0x0F
        # out  out  out  out  in   in   in   in
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRA, 0xF)

        # GPB7 GPB6 GPB5 GPB4 GPB3 GPB2 GPB1 GPB0 = 0x0F
        # in   in   in   in   in   in   in   in
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRB, 0xFF)

        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.GPPUA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.GPPUB, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.IPOLA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.IPOLB, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.OLATA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.OLATB, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.GPIOA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS1, cls.GPIOB, 0x00)

        #--------------------------------------------------------------
        # MCP23017 #02 
        # Extensor 0x24

        # GPA7 GPA6 GPA5 GPA4 GPA3 GPA2 GPA1 GPA0 = 0x00
        # out  out  out  out  out  out  out  out
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.IODIRA, 0x00)

        # GPB7 GPB6 GPB5 GPB4 GPB3 GPB2 GPB1 GPB0 = 0x00
        # out  out  out  out  out  out  out  out
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.IODIRB, 0x00)

        # configura todos os "output latches" no modo HIGH (bits 1)
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.OLATA, 0xFF)
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.OLATB, 0xFF)

        # cls.barramento.write_byte_data(cls.ADDRESS2, cls.GPPUA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS2, cls.GPPUB, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS2, cls.IPOLA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS2, cls.IPOLB, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS2, cls.GPIOA, 0x00)
        # cls.barramento.write_byte_data(cls.ADDRESS2, cls.GPIOB, 0x00)
        print('Escrita concluida!')


    @classmethod
    def confRegistradoresGeladeiraAberta(cls):
        print('Escrevendo 0xBF em todos os registradores...')
        cls.instanciarBarramento()
        # Extensor 0x22
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRA, 0xF)
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRB, 0xFF)

        # Extensor 0x24
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.IODIRA, 0x00)
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.IODIRB, 0x00)

        cls.barramento.write_byte_data(cls.ADDRESS2, cls.OLATA, 0xFF)
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.OLATB, 0xBF)

        print('Escrita concluida!')

    @classmethod
    def confRegistradoresBanheiroAberto(cls):
        print('Escrevendo 0xB7 em todos os registradores...')
        # 0xB7 = 0b10110111 -> desliga os bits GPB6 e GPB3
        cls.instanciarBarramento()
        # Extensor 0x22
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRA, 0xF)
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRB, 0xFF)

        # Extensor 0x24
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.IODIRA, 0x00)
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.IODIRB, 0x00)

        cls.barramento.write_byte_data(cls.ADDRESS2, cls.OLATA, 0xFF)
        cls.barramento.write_byte_data(cls.ADDRESS2, cls.OLATB, 0xB7)

        print('Escrita concluida!')

    @classmethod
    def confRegistradoresLuzes(cls):
        # Registrador 0x22 (GPA)
        print('Escrevendo 0xF no MCP 0x22')
        cls.instanciarBarramento()
        
        # Configura o MCP 0x22 para entrada em 4 bits
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.IODIRA, 0xF)

    @classmethod
    def escreverBinarioLuzes(cls, codigoBin):
        # Registrador 0x22 (GPA)
        print("MCP: " + str(hex(codigoBin << 4)) + " - Arduino: " + str(bin(codigoBin)))
        cls.instanciarBarramento()
        
        # nos exemplos do código, esta chamada vem DEPOIS de um confRegistradoresLuzes, 
        # que seta os 4 bits altos do MCP 0x22 para saída. O códigoBin é então deslocado 
        # 4 bits para a esquerda, ou seja -> ele sai nos bits GPA7-GPA4 do MCP 0x22.

        # estes 4 bits são transmitidos para a caixa de controle de iluminação, que 
        # possui um módulo interno com um Arduino Nano, que converte cada código de 
        # estado de luz (4 bits, de 0b0000 a 0b1111) em uma configuração de spots
        # acessos ou apagados. A consequência é que para mexer na sequência de luzes, 
        # precisa reprogramar este Arduíno.

        # Obs: não tem nenhum "bom motivo" pra usar representação binária pra ler 
        # este valor, a não ser que seja para debugar com um multimetro o status dos 
        # pinos de comunicação com o Arduíno do painel de iluminação.

        # Desloca o codigoBin em 4 bits para a direita e escreve no registrador
        # Código é enviado para o Arduíno do painel de iluminação
        cls.barramento.write_byte_data(cls.ADDRESS1, cls.OLATA, (codigoBin << 4))



# ------ FIM DO MCP23017 ---------
# HARDWARE.md

Parte das saídas do sistema está ligada na GPIO, e parte no MCP.

Os leds estão na GPIO.
As tomadas em série do armário estão na GPIO

São dois conjuntos no MCP; GPA e GPB

Existem alguns sistemas Arduino independentes que se comunicam com a central de automação.
Entre eles, a caixa de automação do sistema de iluminação tem um arduíno e bancos próprios
de relés com chaves em paralelo para comando de cada luz. O Raspberry Pi se comunica por
meio de 4 bits apenas, para setar combinações de luzes para cada estágio do jogo. Isso foi 
uma das pequenas surpresas do processo de "engenharia reversa" do jogo.

## TABELA DE CONEXÕES

| Porta            | Nº do Cabo conectado | Descrição                                                             |
|------------------|----------------------|-----------------------------------------------------------------------|
| PINO 7           | 2.1                  | LDR Registro Chuveiro                                                 |
| PINO 11          | 1.1                  | Chave Verão/Inverno                                                   |
| PINO 13          | 4.1                  | LDR Registro Torneira                                                 |
| PINO 15          | 3.2                  | Gaveta Banheiro - LED Vermelho                                        |
| PINO 19          | 3.1                  | Gaveta Banheiro - LED Verde                                           |
| PINO 21          | 5.2                  | Gaveta Cozinha - LED Vermelho                                         |
| PINO 23          | 5.1                  | Gaveta Cozinha - LED Verde                                            |
| PINO 24          | 6.1                  | Armario Cozinha - LED Verde                                           |
| PINO 29          | 6.2                  | Armario Cozinha - Led Vermelho                                        |
| PINO 31          | 7.1                  | Tomadas do armario em serie                                           |
| PINO 33          | 8.2                  | Modulo Etiqueta RFID Microondas (Apos divisor de tensão 3.3V Arduino) |
| PINO 35          | 9.2                  | Divisoria - LED Verde                                                 |
| PINO 37          | 9.1                  | Divisoria - LED Vermelho                                              |
| PINO 40          | 10.2                 | Geladeira - LED Verde                                                 |
| PINO 38          | 10.1                 | Geladeira - LED Vermelho                                              |
| PINO 36          | 11.1                 | Modulo Etiqueta RFID Geladeira (Apos divisor de tensão 3.3V Arduino)  |
| PINO 32          | 12.2                 |                                                                       |
| PINO 26          | DESCONECTADO         | -                                                                     |
| PINO 22          | DESCONECTADO         | -                                                                     |
| PINO 18          | 13.1                 |                                                                       |
| PINO 16          | 13.2                 |                                                                       |
| PINO 12          | 14.1                 |                                                                       |
| PINO 10          | 14.2                 |                                                                       |
| PINO 8           | 15.2                 |                                                                       |
| GPB 0 (MCP 0x22) | 16.1                 |                                                                       |
| GPB 1 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPB 2 (MCP 0x22) | 19.2                 |                                                                       |
| GPB 3 (MCP 0x22) | DESCONECTADO         |                                                                       |
| GPB 4 (MCP 0x22) | 18.2                 |                                                                       |
| GPB 5 (MCP 0x22) | CONECTADO (Nº?)      | Botão Reestabelecer Energia                                           |
| GPB 6 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPB 7 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPA 0 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPA 1 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPA 2 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPA 3 (MCP 0x22) | DESCONECTADO         | -                                                                     |
| GPA 4 (MCP 0x22) | Modulo Iluminação    | BIT 0 (Pino 2 Arduino)                                                |
| GPA 5 (MCP 0x22) | Modulo Iluminação    | BIT 1 (Pino 3 Arduino)                                                |
| GPA 6 (MCP 0x22) | Modulo Iluminação    | BIT 2 (Pino 4 Arduino)                                                |
| GPA 7 (MCP 0x22) | Modulo Iluminação    | BIT 3 (Pino 5 Arduino)                                                |

# Lógica 1

Constantes para acionar cada um dos LEDs da GPIO

```
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
```
# Lógica 23

Não entendi ainda a lógica, mas existem várias constantes que controlam as luzes todas.

```
        mcp.escreverBinarioLuzes(0b1101) # Codigo do Blackout
        mcp.escreverBinarioLuzes(0b0010) # Codigo de acender spot bike e bateria

```

# Lógica 45

```
    # GPIO's 
    gp_reedSwitchBicicleta = 0 # GPB0 (MCP23017)
    gpio_ledGavetaVermelho = 21 # Led indicador de gaveta fechada (raspberry)
    gpio_ledGavetaVerde = 23 # Led indicador de gaveta aberta (raspberry)
    # Relés
    gp_barraLed = [2,3,4,5] # GPA5, GPA4, GPA3, GPA2 (MCP23017)
    #gp_luzCasa = 0 # GPA0 (MCP23017)
    gp_travaGaveta = 4 #GPB4 (MCP23017)
 
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
```


Código para ler o reed

```
def status_reed_bicicleta():
    gp_reedSwitchBicicleta = 0 # GPB0 (MCP23017)
    mcp.setup(gp_reedSwitchBicicleta, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Reed Switch bicicleta
    leitura = mcp.input(gp_reedSwitchBicicleta, mcp.GPB, mcp.ADDRESS1)    
```


Código para controlar a gaveta do armário

```
def pulso_abrir_gaveta():

    # trava da gaveta do armário é o sinal 4 da GPB (MCP23017)
	gp_travaGaveta = 4 #GPB4 (MCP23017)

    # Garantir que o pino esta como OUTPUT
    mcp.setup(gp_travaGaveta , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
    
    # Em nivel Baixo acionando o Rele
    mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
    time.sleep(1)
    # Em nivel Alto desacionando o Rele
    mcp.output(cls.gp_travaGaveta, mcp.GPB, mcp.HIGH, mcp.ADDRESS2)
```


```
    def acenderSpotGavetaCozinha(cls):
        mcp.escreverBinarioLuzes(0b0011) # Codigo do Spot Gaveta cozinha
```



    # GPIO's
    gpio_tomadas = 31 # Pino para leitura das tomadas ligadas em serie (raspberry)
    gpio_ledVermelho = 18
    gpio_ledVerde = 16

    # Relés
    gp_travaBau = 6 # GPA6 (MCP23017)


# Lógica 6

```
    # GPIO's
    gpio_etiquetaGeladeira = 36 # 36 Raspberry
    gpio_etiquetaMicroondas = 33 # 33 Raspberry
    gp_etiquetaMaquina = 4 # GPB4 (MCP23017)

    GPIO.setmode(GPIO.BOARD) # Contagem de (0 a 40)
    GPIO.setwarnings(False) # Desativa avisos
    GPIO.setup(cls.gpio_etiquetaGeladeira, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
    GPIO.setup(cls.gpio_etiquetaMicroondas, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pino como PULL-DOWN interno
    mcp.setup(cls.gp_etiquetaMaquina, mcp.GPB, mcp.IN, mcp.ADDRESS1) # Etiqueta maquina

    leituraGel = GPIO.input(cls.gpio_etiquetaGeladeira)
    leituraMic = GPIO.input(cls.gpio_etiquetaMicroondas)
    leituraMaq = mcp.input(cls.gp_etiquetaMaquina, mcp.GPB, mcp. ADDRESS1)
```

```
    # Relés
    gp_travaGeladeira = 6 # GPB6 (MCP23017)

    # Loop pois a trava causa disturbio no sistema
    for i in range(1):
        # Garantir que o pino esta como OUTPUT
        mcp.setup(cls.gp_travaGeladeira , mcp.GPB, mcp.OUT, mcp.ADDRESS2)
        
        # Em nivel Baixo acionando o Rele
        mcp.output(cls.gp_travaGeladeira, mcp.GPB, mcp.LOW, mcp.ADDRESS2)
        time.sleep(0.75)

```

# Lógica 7

```
mcp.escreverBinarioLuzes(0b0101) # Codigo do Spot do banheiro
```

# Lógica 8

```
mcp.escreverBinarioLuzes(0b0110) # Codigo do Spot da lavanderia e pia do banheiro
```

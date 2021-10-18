# HARDWARE.md

Parte das saídas do sistema está ligada na GPIO, e parte no MCP.

Os leds estão na GPIO.
As tomadas em série do armário estão na GPIO

São dois conjuntos no MCP; GPA e GPB

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


# HARDWARE.md

O ambiente do caminhão possui uma controladora Raspbery Pi com duas extensões de IO (MCP23017). 
O controle do jogo é feito pela interface Web a partir de um notebook externo, conectado pelo cabo.
Internamente, o Raspberry Pi acessa diversos sensores e atuadores através do conjunto de pinos de 
IO da porta GPIO interna e das portas de extensão de IO do MCP23017.

Adicionalmente, existem vários subsistemas independentes com microcontroladores Arduíno dentro do 
caminhão, cuidando de uma parte específica do jogo. Estes sistemas Arduíno se comunicam por meio 
de pinos de sinal digital que vão para as GPIOs do Raspberry Pi. Entre eles temos:

- Um Arduino Nano em cada caixa de leitura RFID.
- Um Arduino Nano no módulo da mesa de passar (identifica a colocação das 7 roupas no lugar certo)


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

| Porta            | Nº do Cabo         | Setor      | Fase      | Nome do sinal                      | Descrição                                                             |
|------------------|--------------------|------------|-----------|------------------------------------|-----------------------------------------------------------------------|
| PINO 7           | 2.1                | Banheiro   | 8         | gpio_registroChuveiro              | LDR Registro Chuveiro                                                 |
| PINO 8           | 15.2               | Sala       | 1213      | gpio_pinoSinalQuadros              |                                                                       |
| PINO 10          | 14.2               | Sala       | 1 1213    | ledAparadorVerde                   |                                                                       |
| PINO 11          | 1.1                | Banheiro   | 8         | gpio_veraoChuveiro                 | Chave Verão/Inverno                                                   |
| PINO 12          | 14.1               | Sala       | 1 1213    | ledAparadorVermelho                |                                                                       |
| PINO 13          | 4.1                | Banheiro   | 8         | gpio_registroTorneira              | LDR Registro Torneira                                                 |
| PINO 15          | 3.2                | Banheiro   | 1 8       | ledPiaVermelho                     | Gaveta Banheiro - LED Vermelho                                        |
| PINO 16          | 13.2               | Sala       | 1 1011    | ledBauVerde                        |                                                                       |
| PINO 18          | 13.1               | Sala       | 1 1011    | ledBauVermelho                     |                                                                       |
| PINO 19          | 3.1                | Banheiro   | 1 8       | ledPiaVerde                        | Gaveta Banheiro - LED Verde                                           |
| PINO 21          | 5.2                | Cozinha    | 1         | ledGavetaInferiorVermelho          | Gaveta Cozinha - LED Vermelho                                         |
| PINO 22          | DESCONECTADO       |            |           |                                    | -                                                                     |
| PINO 23          | 5.1                | Cozinha    | 1         | ledGavetaInferiorVerde             | Gaveta Cozinha - LED Verde                                            |
| PINO 24          | 6.1                | Cozinha    | 1 9       | ledAcimaMicroondasVerde            | Armario Cozinha - LED Verde                                           |
| PINO 26          | DESCONECTADO       |            |           |                                    | -                                                                     |
| PINO 29          | 6.2                | Cozinha    | 1 9       | ledAcimaMicroondasVermelho         | Armario Cozinha - Led Vermelho                                        |
| PINO 31          | 7.1                | Cozinha    | 1011      | gpio_pinoSinalTomadas              | Tomadas do armario em serie                                           |
| PINO 32          | 12.2               |            | 7         | gpio_pinoSinalGeladeira            | Pino que indica o resultado das questões dentro da geladeira          |
| PINO 33          | 8.2                | Cartões    | 6         | gpio_etiquetaMicroondas            | Modulo Etiqueta RFID Microondas (div. tensão 3.3V Arduino, pull down interno ) |
| PINO 35          | 9.2                | Banheiro   | 1 7       | ledDivisoriaVerde                  | Divisoria - LED Verde                                                 |
| PINO 36          | 11.1               | Cartões    | 6         | gpio_etiquetaGeladeira             | Modulo Etiqueta RFID Geladeira (div. tensão 3.3V Arduino, pull down interno ) |
| PINO 37          | 9.1                | Banheiro   | 1 7       | ledDivisoriaVermelho               | Divisoria - LED Vermelho                                              |
| PINO 38          | 10.1               | Geladeira  | 1 6       | ledGeladeiraVermelho               | Geladeira - LED Vermelho                                              |
| PINO 40          | 10.2               | Geladeira  | 1 6       | ledGeladeiraVerde                  | Geladeira - LED Verde                                                 |
| GPA 0 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPA 1 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPA 2 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPA 3 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPA 4 (MCP 0x22) | Modulo Iluminação  | Iluminação |           |                                    | BIT 0 (Pino 2 Arduino)                                                |
| GPA 5 (MCP 0x22) | Modulo Iluminação  | Iluminação |           |                                    | BIT 1 (Pino 3 Arduino)                                                |
| GPA 6 (MCP 0x22) | Modulo Iluminação  | Iluminação |           |                                    | BIT 2 (Pino 4 Arduino)                                                |
| GPA 7 (MCP 0x22) | Modulo Iluminação  | Iluminação |           |                                    | BIT 3 (Pino 5 Arduino)                                                |
| GPB 0 (MCP 0x22) | 16.1               | Bicicleta  | 45        | gp_reedSwitchBicicleta             |                                                                       |
| GPB 1 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPB 2 (MCP 0x22) | 19.2               | Lavanderia | 9         | gp_pinoSinalMesaPassar             |                                                                       |
| GPB 3 (MCP 0x22) | DESCONECTADO       |            |           |                                    |                                                                       |
| GPB 4 (MCP 0x22) | 18.2               | Cartões    | 6         | gp_etiquetaMaquina                 |                                                                       |
| GPB 5 (MCP 0x22) | CONECTADO (Nº?)    | Sala       | 1213      | gp_chaveVitoria                    | Botão Reestabelecer Energia                                           |
| GPB 6 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPB 7 (MCP 0x22) | DESCONECTADO       |            |           |                                    | -                                                                     |
| GPA 0 (MCP 0x24) |                    |            |           |                                    |                                                                       |
| GPA 1 (MCP 0x24) | ?                  | Banheiro   | 8         | gp_fitaLedChuveiro                 |                                                                       |
| GPA 2 (MCP 0x24) | ?                  | Bicicleta  | 45        |                                    | Nível de carga da bateria                                             |
| GPA 3 (MCP 0x24) | ?                  | Bicicleta  | 45        |                                    | Nível de carga da bateria                                             |
| GPA 4 (MCP 0x24) | ?                  | Bicicleta  | 45        |                                    | Nível de carga da bateria                                             |
| GPA 5 (MCP 0x24) | ?                  | Bicicleta  | 45        |                                    | Nível de carga da bateria                                             |
| GPA 6 (MCP 0x24) | ?                  | Sala       | 1011      | gp_travaBau                        |                                                                       |
| GPA 7 (MCP 0x24) | ?                  | Sala       | 1213      | gp_travaAparador                   |                                                                       |
| GPB 0 (MCP 0x24) | ?                  | Banheiro   | 8         | gp_ledVermelhoChuveiro             |                                                                       |
| GPB 1 (MCP 0x24) | ?                  | Banheiro   | 8         | gp_fitaLedPia                      |                                                                       |
| GPB 2 (MCP 0x24) | ?                  | Banheiro   | 8         | gp_travaGavetaBanheiro             |                                                                       |
| GPB 3 (MCP 0x24) | ?                  | Banheiro   | 7         | gp_travaPortaBanheiro              |                                                                       |
| GPB 4 (MCP 0x24) | ?                  | Cozinha    | 45        | gp_travaGavetaArmario              |                                                                       |
| GPB 5 (MCP 0x24) | ?                  | Cozinha    | 9         | gp_travaPortaArmario               |                                                                       |
| GPB 6 (MCP 0x24) | ?                  | Geladeira  | 6         | gp_travaGeladeira                  |                                                                       |
| GPB 7 (MCP 0x24) | ?                  | Banheiro   | 7         | gp_ledsJogoGeladeira               |                                                                       |

# cdmescape

Servidor Django do Escape Game da CDM (Cooperação para o Desenvolvimento e Morada Humana), com parte do contrato de ações educativas para o programa de Eficiência Energética da CEMIG.

## DESCRIÇÃO GERAL

Jogo de sala de escape, composto de uma sequência de atividades (puzzles) que devem ser resolvidos pela equipe para conclusão do jogo e abertura da sala.

A sala está montada em um caminhão e simula uma residência com vários ambientes. Cada ambiente possui uma atividade que precisa ser resolvida. As atividades remetem ao conhecimento da equipe sobre o tema da eficiência energética e principalmente, do consumo consciente de energia.

Os jogadores são apoiados durante todo processo através de luzes que guiam o foco de ação dentro do ambiente, iluminando a área onde está atividade que precisa ser resolvida. Também são utilizados efeitos sonoros diversos. Luzes indicadoras complementam o jogo permitindo que a equipe visualize se uma determinada parte do jogo está resolvida (luz verde) ou não (luz vermelha).

## SEQUÊNCIA DE ATIVIDADES

1. **Abertura do jogo**, com apagamento das luzes por alguns segundos (efeito "black out") seguido do foco na primeira atividade, que é a bicicleta.

2. **Bicicleta com carregador de bateria**. Uma bicicleta montada em uma estação fixa fica no fundo do caminhão em uma área que simula uma parte externa da casa (quintal ou varanda). Ao pedalar a bicicleta, um carregador montado na parede indica a carga gradual até que a bateria seja totalmente preenchida.

3. **Gaveta da cozinha**. A gaveta se abre; uma luz verde se acende na gaveta indicando que a mesma está aberta. O spot da gaveta ilumina o local. Abrindo a gaveta, a equipe encontra três cartões com indicadores de consumo de energia para três equipamentos: (1) Forno de Microondas, (2) Geladeira e (3) Máquina de lavar. Cada uma delas possui uma pequena caixa com um slot para inserção do cartão. O objetivo desta etapa é identificar o cartão correto para cada equipamentos. Todos eles indicam que são equipamentos de alta eficiência energética (categoria A).

4. **Geladeira**. Ao completar a atividade dos três equipamentos, o spot da geladeira se acende, e a porta da mesma é destravada. Abrindo a geladeira, a equipe encontra um "quiz" com quatro questões, cada uma com uma chave seletora de três posições: uma posição central "neutra", e duas posições de lados opostos para indicar a resposta "SIM" ou "NÃO". As questões do puzzle podem variar, mas as respostas são sempre as mesmas, de cima para baixo: SIM, NÃO, NÃO, SIM. Os jogadores irão encontrar inicialmente as quatro chaves na posição neutra. Assim que responderem a todas, eles devem pressionar um botão abaixo para que o jogo confirme as respostas. Se estiverem certas, as luzes internas da geladeira vão piscar e a próxima atividade será liberada.

5. **Banheiro**. Há uma salinha fechada no fundo do caminhão, do lado da bicicleta, onde está instalado o banheiro, que possui uma pia e um chuveiro. A porta do banheiro possui uma trava magnética e fica fechada no começo do jogo, até ser destravada quando a atividade da **Geladeira** é concluída. Ao abrir o banheiro a equipe irá encontrar a torneira da pia aberta (fluxo de água representado por uma fita de LED azul acesa, instalada na torneira); a torneira do chuveiro aberta (fluxo de água representado por uma fita de LED azul instalada ao redor do chuveiro); e o chuveiro estará operando no modo "inverno", o que é representado por um LED vermelho aceso dentro do chuveiro. Um efeito de áudio indica que as torneiras estão abertas. Para resolver esta atividade a equipe precisa (1) fechar a torneira da pia, (2) fechar a torneira do chuveiro e (3) mudar a chave do chuveiro para o modo "verão" (menor consumo). Assim que concluem as três tarefas, a porta de uma gaveta na pia do banheiro se abre, permitindo que a equipe encontre um kit com 7 cartões de MDF representando roupas variadas.

6. **Mesa de Passar**. Há uma mesa com um ferro de passar instalado, com uma caixa preta com slots recortados no formato das peças de roupa. Ao concluir a atividade do **Banheiro** a luz de foco ilumina a mesa. O objetivo é colocar as peças no local correto para destravar a próxima etapa.

7. **Armário da Cozinha**. Uma porta do armário da cozinha se abre, com um spot iluminando o local. Dentro do armário há cinco tomadas na parede, com vários plugues ligados em um "benjamim" ou "T". A solução da atividade é ligar todos os plugues diretamente nas tomadas da parede sem o uso do "benjamim" ou "T". Ao solucionar esta atividade, a luz dos spots ilumina um baú que fica abaixo da TV, destravando a tampa do baú.

8. **Caminho da Energia**. Dentro do baú existem 4 cartões que representam partes de um quadro que mostra o caminho da energia desde a geração, passando pela transmissão e distribuição, até a casa do consumidor. Os cartões precisam ser colocados no local correto para destravar a última parte do jogo.

9. **Botão de FIM**. Ao concluir a montagem do quadro do "Caminho da Energia", será destravada a gaveta do aparador. Dentro do aparador há um botão que pode ser acionado para indicar que a equipe atingiu o fim do jogo com sucesso.

## DESCRIÇÃO DO SISTEMA

O ambiente do caminhão é controlado por uma central de automação, que utiliza um Raspberry Pi como central de processamento. O Raspberry Pi está conectado a uma placa de expansão de IO (breakout board) que permite conectar os sensores instalados em vários pontos do caminhão, bem como atuar através de um banco de 16 relés para comandar acendimento de LEDs e acionamento de travas magnéticas que comandam as portas.

A lógica do jogo está implementada como uma aplicação Web escrita em Django, com a linguagem Python. A cada partida o servidor Web é reinicializado. A tela principal do jogo (`historia1.html`) apresenta uma tela interativa que mostra o progresso do jogo e possui alguns comandos que podem ser acionados manualmente pelo operador. Os principais comandos são:

1. **INICIAR**. Roda os primeiros estágios da máquina do jogo, preparando o setup para início do mesmo.

2. **REINICIAR**. Código simples que reinicializa o servidor Web e garante que o jogo seja recarregado. TODO: permitir que o jogo seja reiniciado sem ter que dar um "reboot" no servidor Web.

3. **DESLIGAR**. Dá um comando de "shutdown" no Raspberry Pi. Deve ser usado no fim do uso do caminhão, antes de desligar o mesmo, para garantir que não haverá dano ao sistema de arquivos do Raspberry Pi por ligar e desligar o mesmo sem fechar os arquivos corretamente.

## ARQUITETURA DO PROJETO DJANGO

Na terminologia do Django, o sistema é composto por "projeto" Django (de nome `cdmserver`), dentro do qual existe um "aplicativo" Django chamado `cdmjogo`. Toda lógica do jogo está no aplicativo, e o projeto apenas serve como "esqueleto" para sua execução.

### PÁGINAS DO JOGO

O aplication `cdmjogo` possui as seguintes páginas, com templates próprios:

1. `historia1.html`. Página que possui a interface principal do jogo conforme descrito neste documento.

2. `historia2.html`. Página em branco, não foi utilizada. TODO: retirar do sistema.

3. `desenvolvimento.html`. Página com algumas ferramentas de desenvolvimento, está sendo ampliada para suportar o modo de "debug".

### URLs DO JOGO

Além das páginas Web, existem também algumas URLs que são usadas para chamadas do tipo "Ajax" (código assíncrono em Javascript), para permitir atualização da interface e comunicação com o engine de jogo sem dar um refresh na página. As URLs do tipo "ajaxXXXXXX" não possuem templates e retornam objetos JSON que são apresentados pelas páginas por meio de um código Javascript interno.

1. `ajaxiniciarjogo`. Inicializa as luzes do jogo e dispara a thread da `logica_1`. A partir deste momento o jogo estará rodando, até que a última thread seja finalizada.

2. `ajaxstatus`. Retorna um objeto JSON com indicadores de conclusão para cada uma das etapas do jogo. Os indicadores são utilizados pelo código Javascript que roda dentro da página do jogo para atualizar o indicador de conclusão das fases. O efeito sonoro que acompanha as torneiras do banheiro também é controlado por uma das variáveis de status.

3. `historia1`. Abre a página `historia1.html`, que apresenta a interface completa do jogo e carrega também os scripts Javascript que interagem em segundo plano com a lógica de jogo (ações chamadas através da URL `ajaxhistoria1`) e atualização de status (chamadas periódicas a `ajaxstatus`).

4. `ajaxhistoria1`. Callback das ações Ajax da página `historia1.html`. Recebe um parâmetro de ação; todos os comandos que tem efeito durante o jogo, incluindo algumas possibilidades de pular etapas, são executados dentro dessa chamada. Executa diretamente ações dentro das classes de lógica (que são multithreaded), e portanto tem como interferir no sequenciamento das ações.

5. `historia2`. Abre a página `historia2.html` (que está vazia). TODO: remover do jogo.

6. `ajaxhistoria2`. Callback das ações Ajax da página `historia2.html` (sem efeito). TODO: remover do jogo.

7. `desenvolvimento`. Abre a página `desenvolvimento.html`, que apresenta o ambiente de testes.

8. `ajaxdesenvolvimento`. Callback das ações Ajax da página `desenvolvimento.html`. 

Finalmente, a URL de índice é gerada automaticamente com chamadas para as páginas indicadas acima.

## CÓDIGO DE "MULTITHREADING"

A lógica do jogo roda em segundo plano com uso de "multithreading". A implementação em si é bastante simples, mas a arquitetura é um pouco confusa. Existe uma classe "mãe" chamada `logica_geral.py`, que define uma classe de multithreading com uma estrutura padronizada, que é usada a cada estágio do jogo. A cada momento do jogo, somente uma thread estará rodando em loop infinito enquanto estiver ativa. Assim que uma condição de encerramento da thread é atingida, uma nova thread é criada e a thread atual é encerrada.

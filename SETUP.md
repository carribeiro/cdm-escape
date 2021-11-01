# INSTRUÇÕES PARA CONFIGURAR O RASPBERRY PI

## Habilitar o VNC para acesso pela rede local

Como o acesso inicial é pela linha de comando via SSH, seguir as instruções do segundo link.

https://magpi.raspberrypi.com/articles/vnc-raspberry-pi
https://forums.raspberrypi.com/viewtopic.php?t=216590

Editar o script de inicialização de serviços locais:
```
sudo nano /etc/rc.local
```

Adicionar a linha abaixo antes da linha 
```
sudo -u pi vncserver
```

Da primeira vez é bom fazer manualmente, para gerar a chave:

```
pi@raspberrypi:~ $ sudo -u pi vncserver &
[1] 929
pi@raspberrypi:~ $ VNC(R) Server 6.4.1 (r40826) ARMv6 (Mar 13 2019 16:35:06)
Copyright (C) 2002-2019 RealVNC Ltd.
RealVNC e VNC são marcas registradas da RealVNC Ltd que estão protegidas por
registros de marca e/ou pedidos pendentes de marca registrada na União
Europeia, nos Estados Unidos da América e em outras jurisdições.
Marcas protegidas pela patente 2481870 no Reino Unido, 8760366 nos EUA e
2652951 na União Europeia.
Consulte https://www.realvnc.com para obter informações sobre o VNC.
Para ver reconhecimentos de terceiros, consulte:
https://www.realvnc.com/docs/6/foss.html
OS: Raspbian GNU/Linux 10, Linux 4.19.57, armv7l

Gerando chave privada... concluído
Em algumas distribuições (particularmente no Red Hat), você pode ter uma
experiência melhor executando o vncserver-virtual juntamente com o servidor Xorg
do sistema, em vez da versão antiga integrada ao Xvnc. Outros ambientes e
aplicativos de desktop provavelmente serão compatíveis. Para obter mais
informações sobre essa implementação alternativa, consulte:
https://www.realvnc.com/doclink/kb-546

Executando aplicativos em /etc/vnc/xstartup

Frase do VNC Server: "Stone Arnold maestro. Cave outside theory."
         assinatura: de-dc-30-42-59-aa-c4-70

O arquivo de log é /home/pi/.vnc/raspberrypi:1.log
O novo desktop é raspberrypi:1 (192.168.10.151:1)

[1]+  Concluído              sudo -u pi vncserver
```

## Habilitar a interface WiFi

Um detalhe: o AP que está sendo usado do galpão da CDM usa a mesma rede LAN (192.168.10.0) que está sendo usada no link ponto a ponto Ethernet.
Isso pode causar interferências ou funcionamento intermitente. Eu acredito que a máquina esteja usando um processo de roteamento "round robin" o que
faz com que queries de DNS falhem de vez em quando e a performance seja ruim.

WiFi habilitado através da interface gráfica via VNC.

SSID: WIFI-QUADRA

Senha: $$cdmquadra$$

## Setar DNS corretamente

O DNS dos Raspberry Pi estava apontando para IPs internos da rede, mas não funciona quando está no WiFi. Provavelmente é um resto de configuração do ambiente de desenvolvimento original.

https://pimylifeup.com/raspberry-pi-dns-settings/

Editar o arquivo de configuração do serviço DHCPCD (cliente DHCP):
```
sudo nano /etc/dhcpcd.conf
```

Editar a linha do `domain_name_servers` (deve estar comentada):
```
static domain_name_servers=8.8.4.4 8.8.8.8
```

Salvar o arquivo e reiniciar o serviço DHCPCD (cliente DHCP):
```
sudo service dhcpcd restart
```

## Sincronizar relógio

Como os caminhões ficam muto tempo desconectados da Internet, a hora fica totalmente perdida. No meu teste, bastou pedir o status do `timedatectl` para atualizar, mas se não der certo, seguir as instruções do link abaixo.

https://raspberrytips.com/time-sync-raspberry-pi/

```
timedatectl status
```

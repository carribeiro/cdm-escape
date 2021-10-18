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

## Habilitar a interface WiFi

Um detalhe: o AP que está sendo usado do galpão da CDM usa a mesma rede LAN (192.168.10.0) que está sendo usada no link ponto a ponto Ethernet.
Isso pode causar interferências ou funcionamento intermitente. Eu acredito que a máquina esteja usando um processo de roteamento "round robin" o que
faz com que queries de DNS falhem de vez em quando e a performance seja ruim.

WiFi habilitado através da interface gráfica via VNC.

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

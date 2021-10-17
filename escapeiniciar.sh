#!/bin/bash

# Limpa o terminal
#clear

echo "Iniciando o ambiente virtual..."
# Executando o script activate que inicia a venv (cdmvenv)
. /home/pi/cdmescape/cdmvenv/bin/activate
echo "--> (cdmvenv) Iniciado!"

echo "Iniciando o servidor Django"
echo "192.168.10.151:8000/"
# Inicia o servidor usando o manage.py, no IP 192.168.10.151:8000
python3 /home/pi/cdmescape/cdmserver/manage.py runserver 192.168.10.151:8000
echo ""

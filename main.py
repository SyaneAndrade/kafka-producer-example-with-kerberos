#!/usr/bin/env python
#-*- coding: utf-8 -*-
from dados.dadosio import DadosIO
from producer import Producer
from time import sleep
from random import randint
import gssapi


"""
Modulo responsavel por gerenciar chamadas das funções e do envio
dos dados.
"""

def main(prod):
    """
    Funcao principal
    :param prod: flag para rodar localmente ou em outro endereço que seja homolog ou producao
    :return: None
    """
    server = ""
    if prod:
        server = "prod:9092"
    else:
        server = "localhost:9092"
    dados1 = DadosIO("dados/mock_producer/dados1.json")
    dados2 = DadosIO("dados/mock_producer/dados2.json")

    dados1.lerArquivo()
    dados2.lerArquivo()
    """
    O protocolo de segurança só é necessário caso aja alguma proteção no seu ambiente,
    nesse caso os valores já setados são para ambientes que possui Kerberos
    """
    params = { 'bootstrap_servers': [server],
               'security_protocol': 'SASL_PLAINTEXT',
               'sasl_mechanism': 'GSSAPI'}


    viaunica_cli = Producer("topic1", params)
    viaunica_contatos = Producer("topic2", params)

    while True:
        for index in range(0, 1000):
            print str(dados1.json[index])
            print str(dados2.json[index])
            sec = randint(0, 10)
            print sec
            sleep(sec)

            viaunica_cli.enviar(str(dados1.json[index]))
            viaunica_contatos.enviar(str(dados2.json[index]))


if __name__ == '__main__':
    main(True)

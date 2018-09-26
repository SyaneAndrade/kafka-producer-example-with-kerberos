# -*- coding: utf-8 -*-
from kafka import KafkaProducer

"""
Class responsável por inicializar um objeto Producer do kafka
recebendo uma lista de parametros
"""


class Producer():

    def __init__(self, nome, param):
        self.producer = KafkaProducer(**param)
        self.topic = nome

    def enviar(self, msg):
        self.producer.send(self.topic, bytes(msg))

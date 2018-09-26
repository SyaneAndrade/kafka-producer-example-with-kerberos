# -*- coding: utf-8 -*-

import json

"""
Classe responsável por abrir os arquivos com as informações a serem enviados para os topicos
"""

class DadosIO():

    json = None

    def __init__(self, caminho):
        self.caminho = caminho


    def lerArquivo(self):
        conteudo = open(self.caminho).read()
        self.json = json.loads(conteudo, object_hook=self._decode_dict)


    def _decode_dict(self, data):
        rv = {}
        for key, value in data.iteritems():
            if isinstance(key, unicode):
                key = key.encode('utf-8')
            if isinstance(value, unicode):
                value = value.encode('utf-8')
            elif isinstance(value, list):
                value = self._decode_list(value)
            elif isinstance(value, dict):
                value = self._decode_dict(value)
            rv[key] = value
        return rv
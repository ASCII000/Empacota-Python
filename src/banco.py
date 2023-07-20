import json, requests
from typing import Literal, Type

class Banco():

    def __init__(self, nome_do_banco: Type[str]):
        self._data = nome_do_banco
        self._produtos = None

    def adicionar(self, nome_do_produto):
        pass

    def remover(self, nome_do_produto):
        pass

    def update(self):
        pass

    @property
    def produtos(self):

        if self._produtos:
            return self._produtos
        
        else:
            raise ValueError(f'O banco está vazio {self}')

banco = Banco('teste')
banco.produtos


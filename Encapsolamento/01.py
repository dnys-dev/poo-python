#!/usr/bin/env python3

"""Exemplo de encapsolamento de um método
"""

__version__ = 1.0
__autor__ = 'daviny'
__license__ = "GNU v3"

class Funcionario:

    def __init__(self, nome: str, cargo: str, valor_hora_trabalhada: int) -> int:
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario: int):
        raise ValueError ("Imposivel Alterar")

    def registroHoraTrabalhada(self):
        self.registroHoraTrabalhada =+ 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada


maria = Funcionario('Pedro', 'Gerente de Vendas', 50)
print(maria.salario)

# entrada não permitida
maria.salario = 100000
print(maria.salario)
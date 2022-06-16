#!/usr/bin/env python3

"""exemplo 02
Encapsolamento
"""

__autor__ = 'Daviny'
__version__ = 1.0
__license__ = 'GNU v3'

class Visitas:

    def __init__(self, quantidade: int, valor_visita: int ) -> int:
        self.quantidade = quantidade
        self.valor_visita = valor_visita
        self.__resultado = 0

    @property
    def resultado(self):
        return self.__resultado
    
    @resultado.setter
    def resultado(self, novo_value: int):
        raise ValueError ('Entranda não permitida')

    def somatoriaVisita(self):
        self.__resultado = self.quantidade * self.valor_visita


maria = Visitas(10, 2)

print(maria.quantidade)

# entrada não permitida
maria.resultado = 100

print(maria.resultado)
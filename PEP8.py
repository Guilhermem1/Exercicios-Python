""""
PEP 8 - PYHTON ENHANCEMENT PROPOSAL
PROPOSTAS DE MELHORIA PARA PYTHON
ZEM OF PYTHON
[1] Utilize Camel Case para nomes de classes

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] Utilize nome minúsuclo, separados por underline para funções ou variáveis

def soma():
    pass


def soma_dois():
    pass

[3] Utilize 4 espaços para identação!
if 'a' in 'banana':
    print("tem")

[4] Import
#Errado
import sys,os

#Certo
import sys
import os

#Certo
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
"""
#age=input("QUal sua idade ")
#print(f'Voce nasceu em {2018-int(age)} anos')
#print("Voce nasceu em", 2018-int(age),"anos")
nome = 'Geek University'
print(nome[:2:])

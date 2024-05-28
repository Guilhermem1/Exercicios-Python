'''
Pacotes

Módulo é apenas um arquivo Python que pode ter diversas funcoes para utilizarmos
Pacote -> è um diretorio que apresenta um conjunto de modulos

OBS:  Nas versoes 2.x do Python deveria conter dentro dele um arquivo chamado __init__.py
Nas versoes 3.x não é mais obrigado, mas normalmente ainda é utlizado para manter a compatibilidade

from geek import geek1, geek2
from geek.university import geek3, geek4

print (geek1.pi)
print(geek1.funcao1(5,6))
print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())
'''

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4
print(funcao1(2,1))
print(funcao4())
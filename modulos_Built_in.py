'''
Modulos Bult-in

#Utlizando alias (apelidos) para módulos/funcoes
import random as rdm
print(rdm.random())

from random import randint as rdi, random as rdm
print(rdi(2,5))
print(rdm())

#Podemos importar todas as funções de um modulo utilizando o *
from random import *
print(random())
'''
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo modulo
from random import (
    randint,
    random,
    shuffle,
    choice)
print(random)
print(randint(1,6)
      )

# MAIS MODULOS
https://docs.python.org/3/py-modindex.html


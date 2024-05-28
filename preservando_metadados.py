"""
Preservando metadatas com wraps

Metadados -> São dados intrísecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.



# Problema

def ver_logar(funcao):
    def logar(*args,**kwargs):
        #Eu sou uma funcao(logar) dentro de outra
        print(f'Voce esta chamando a funcao {funcao.__name__}')
        print(f'Aqui está a documentação {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar

@ver_logar
def soma(a,b):
    #Soma de dois numeros
    return a+b

print(soma(5,6))

# Problema:
print(soma.__name__)  #soma, mas dá: logar
print(soma.__doc__)  #Soma de dois numeros, mas da: Eu sou uma funcao(logar) dentro de outra
"""

#Resolução do Problema

from functools import wraps
def ver_logar(funcao):
    @wraps(funcao)
    def logar(*args,**kwargs):
        '''Eu sou uma funcao(logar) dentro de outra'''
        print(f'Voce esta chamando a funcao {funcao.__name__}')
        print(f'Aqui está a documentação {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar

@ver_logar
def soma(a,b):
    '''Soma de dois numeros'''
    return a+b

print(soma(5,6))

# Problema:
print(soma.__name__)  #soma, mas dá: logar
print(soma.__doc__)  #Soma de dois numeros, mas da: Eu sou uma funcao(logar) dentro de outra

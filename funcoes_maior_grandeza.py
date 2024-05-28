'''
Funções de maior grandeza - Higher Order Fuctions - HOF
-> Quando uma linguagem de programação suporta HOF indica que podemos ter funções que
retornam outras funções como resultado ou mesmo que podemos passar funções como
argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.
Em python, as funcoes sao Cidadoes de Primeira Classe,, First Class Citizin


# Exemplo -Definindo funcoes
def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def calcular(a,b,funcao):
    return funcao(a,b)

print(calcular(4,3,somar))
print(calcular(4,3,subtrair))
print(calcular(4,3,multiplicar))
print(calcular(4,3,dividir))
'''

# Nested Fuctions - Funcoes aninhadas
'''
Em python podemos ter funções dentro de funcoes, que sao conhecidos como Nested Fuctions
ou também Inner Fuctions (Funções Internas)


# Exemplo
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("E ai ","Suma daqui ", "Gosto de voce "))
    return humor() + pessoa

print(cumprimento('Angelina '))
print(cumprimento("Felix"))


# retornando funcoes de outras funcoes
from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahaha','kkkkkkkkk','yayayyayyaya'))
    return rir

rindo = faz_me_rir()
print(rindo())
'''

# inner functions (Funcoes Internas / Nested Fuctional) podem acessar o escopo de funcoes mais externas
from random import choice

def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(('hahahaha','kkkkkkkk','yayayayaya'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir('Fernanda')

print(rindo())
print(rindo())
print(rindo())
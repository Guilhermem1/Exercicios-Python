'''
    Funções com retorno

def quadrado_7():
    print(7*7)

ret = quadrado_7()
print(f'Retorno: {ret}')
#Def quadrado_7() esta somente imprimindo, porém não está retornando
#Vamos modificar o codigo para retornar

def quadrado_retornado_7():
    return 7*7

#criando uma variavel para receber o retorno da função
ret_2 = quadrado_retornado_7()
print(f'Retorno: {ret_2}')

print(f'Retorno :  {quadrado_retornado_7()+1}')

#Vantagem de return
def diz_oi():
    return 'Oi '
alguem = "Joao"
print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores

Exemplo 1:

def diz_oi():
    print("Estou sendo executada antes do Return")
    return ("OI")
    print("Estou sendo executada após o Return")

print(diz_oi())


# Exemplo 2:

def nova_funcao():
    variavel = None
    if variavel:
        return 'A'
    elif variavel is None:
        return "B"
    else:
        return "C"
print(nova_funcao())


#Exemplo 3
def outra_funcao():
    return 1,3,5,7

num1, num2, num3, num4 = outra_funcao() #Desempacotando tupla
print(num1, num2, num3, num4)

print(outra_funcao()) #tupla
'''
#Criando funcao para jogar moeda
from random import random
from random import randint
def joga_moeda():
    #Random gera um valor entre 0 e 1
    # valor = randint(0,1)
    valor = random()
    if valor > 0.5:
        return 'Cara'
    else:
        return "Coroa"
    
print(joga_moeda())
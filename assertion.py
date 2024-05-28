'''
Assertion (checagens/questionamentos)

Em python, utilizamos a palavra reservada 'assert' para realizar simples afirmações
utilizadas nos testes

Utilizamos o 'assert' em uma expressao que queremos checar se é valida ou não.
Se a expressfor verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizado

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nossso ...  não precisa
ser exclusivamente nos testes

# ALERTA: Cuidado ao utilizar 'assert'
Se um programa Python for executado com parâmtero -O, nenhum assertion será valdiado. Ou seja, todas as validações
já eram
'''

def soma_positivos(a,b):
    assert a>0 and b>0, 'ambos precisam ser positivos'
    return a+b

ret = soma_positivos(4,6)
print(ret)
# ret = soma_positivos(-4,6)
# print(ret)

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'hamburguer',
        'batata frita',
        'cachorro quente'
    ] , 'a comida precisa ser fast food'

    return f'Estou comendo {comida}'

comida = input("Informe a comida: ")
print(comer_fast_food(comida))


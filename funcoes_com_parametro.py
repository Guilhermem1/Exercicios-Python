'''
Funções com parâmetro (de entrada)
- Funções que recebem entrada da mesma
Se a gente pensar em um programa qualquer há: entrada, processamente , saída
Se a gente pensar em função, há:
Nao possuem entrada
Nao possuem saida
Possuem entrada mas nao possuem saida
Não possuem entrada mas possuem saida
Nao possuem entrada e saida

#Refatorando uma função
def quadrado(num):
    return num*num
print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

def cantar_parabens(aniversariante):
    print("Parabens pra voce")
    print("Muitos anos de vida")
    print("Parabens", aniversariante)

cantar_parabens('joao')

#Funcoes com mais parametros
def soma(a,b):
    return a+b

#Nomeando parametros
def nome(str1,str2):
    return (f'Seu nome completo: {str1} {str2}')

stg = input("Digite seu nome completo ")
palavra = stg.split()
print(nome(palavra[0], palavra[1]))

#Argumentos nomeados
print(nome(str1='Neymar', str2='Junior'))


#Erros Comuns
def soma_impares(numeros):
    total=0
    for num in numeros:
        if num%2 == 1:
            total = num + total
        return total
lista = [1,2,3,4,5,6,7]
print(soma_impares(lista))   #Observe que Return irá acabar no primeiro elemento, e
                            # uma vez executado, ele nao irá entrar no laço de repetição dnv.

#MANEIRA CORRETA
def soma_impares(numeros):
    total=0
    for num in numeros:
        if num%2 == 1:
            total = num + total
    return total
lista = [1,2,3,4,5,6,7]
print(soma_impares(lista))
'''
#MANEIRA CORRETA
def soma_impares(numeros):
    total=0
    for num in numeros:
        if num%2 == 1:
            total = num + total
    return total
if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7]
    print(soma_impares(lista))
else:
    print("O programa funcoes_com_parametro foi importado")
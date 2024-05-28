'''
    Funções com paramtetro padrao (Default Parameters)
- Funções onde a passagem de parametros seja opcional
#Exemplo onde a passagem de parametro seja opcional
print()

#Exemplo de função com parametro que seja obrigatorio
def quadrado(num):
    return num**2
print() #Type error

def exponencial(base,potencia=2):
    return base**potencia

print(exponencial(4,3))
print(exponencial(5)) #Por padrao eleva ao ^2

#OBS: Em funções Python, os parâmetros com valores default DEVEM sempre estar no final
#ERRADo
def teste(num=2,potencia):
    return num**potencia

print(teste(3))

#CORRETO
def teste(potencia,num=2):
    return num**potencia

print(teste(3))

#Exemplo mais complexo
def mostra_inf(nome='geek',instrutor = False):
    if nome == 'geek' and instrutor:
        return ("Bem vindo instrutor Geek")
    elif nome == 'geek':
        return ("Pensei que voce fosse o instrutor")
    return f'Ola {nome}'

print(mostra_inf())
print(mostra_inf(instrutor=True))
print(mostra_inf(True))
print(mostra_inf("Ozil"))
print(mostra_inf(nome="Sthefani"))

#Exemplos
def soma(num1, num2):
    return num1 + num2

def mat(num1,num2,funcao=soma): #Por padrao ele vai pra funcao soma
    return funcao(num1,num2)

def subtracao(num1,num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,3,subtracao))

#ATENÇÃO com  variaveis globais
total = 0
# def incremento():  #ERRO
#     total = total + 1         #A variavel total nao foi inicializada
#     return total
def incremento():
    global total
    total =total +1
    return total

print(incremento())

#Podemos ter funcoes que sao declaradas dentro de funcoes, e tambem tem uma forma especial
#de escopo de variaveis

def fora():
    contador=0
    def dentro():
        nonlocal contador  #A variavel nao eh local, mas como tambem nao é global, significa
        contador = contador +1  #que ela esta na funcao anterior, na linha 75
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
'''


